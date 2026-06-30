from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from events.models import Event
from bookings.models import Booking
from payments.models import Payment
from openpyxl import Workbook
from django.http import HttpResponse
from payments.models import Payment

from reportlab.pdfgen import canvas

from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
)

from .models import UserProfile


# -------------------------
# Register
# -------------------------
def register_user(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            phone = form.cleaned_data['phone']

            UserProfile.objects.create(
                user=user,
                phone=phone
            )

            login(request, user)

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


# -------------------------
# Login
# -------------------------
def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

    return render(request, 'login.html')


# -------------------------
# Logout
# -------------------------
def logout_user(request):

    logout(request)

    return redirect('home')


# -------------------------
# Profile
# -------------------------
@login_required
def profile(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            return redirect('profile')

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=profile
        )

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# -------------------------
# Admin PDF Report
# -------------------------
@login_required
def admin_report(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="admin_report.pdf"'
    )

    p = canvas.Canvas(response)

    # Title
    p.setFont(
        "Helvetica-Bold",
        18
    )

    p.drawString(
        170,
        800,
        "EVENT MANAGEMENT REPORT"
    )
    

    # Statistics
    total_users = User.objects.count()
    total_events = Event.objects.count()
    total_bookings = Booking.objects.count()

    revenue = sum(
        payment.amount
        for payment in Payment.objects.all()
    )

    p.setFont(
        "Helvetica",
        12
    )

    p.drawString(
        50,
        740,
        f"Total Users : {total_users}"
    )

    p.drawString(
        50,
        710,
        f"Total Events : {total_events}"
    )

    p.drawString(
        50,
        680,
        f"Total Bookings : {total_bookings}"
    )

    p.drawString(
        50,
        650,
        f"Total Revenue : ₹{revenue}"
    )

    # Booking Table
    y = 590

    p.setFont(
        "Helvetica-Bold",
        12
    )

    p.drawString(
        50,
        y,
        "User"
    )

    p.drawString(
        180,
        y,
        "Event"
    )

    p.drawString(
        360,
        y,
        "Status"
    )

    y -= 25

    p.setFont(
        "Helvetica",
        11
    )

    for booking in Booking.objects.all():

        p.drawString(
            50,
            y,
            booking.user.username
        )

        p.drawString(
            180,
            y,
            booking.event.title
        )

        p.drawString(
            360,
            y,
            booking.status
        )

        y -= 20

        if y < 50:
            p.showPage()
            y = 800

    p.save()



    return response

    # -------------------------
# Export Excel Report
# -------------------------
@login_required
def export_excel_report(request):

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Payments Report"

    # Heading Row
    sheet.append([
        "Transaction ID",
        "User",
        "Amount",
        "Status",
        "Date"
    ])

    payments = Payment.objects.all()

    for payment in payments:

        sheet.append([

            payment.transaction_id,
            payment.user.username,
            float(payment.amount),
            payment.status,
            str(payment.paid_at)

        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="payments_report.xlsx"'

    workbook.save(response)

    return response
    
    