from django.shortcuts import render
from django.contrib.auth.models import User

from bookings.models import Booking
from events.models import Event
from payments.models import Payment
from django.http import HttpResponse
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

import openpyxl

def admin_dashboard(request):

    total_users = User.objects.count()

    total_events = Event.objects.count()

    total_bookings = Booking.objects.filter(
        status='confirmed'
    ).count()

    confirmed = Booking.objects.filter(
        status='confirmed'
    ).count()

    cancelled = Booking.objects.filter(
        status='cancelled'
    ).count()

    pending = Booking.objects.filter(
        status='pending'
    ).count()

    revenue = total_bookings * 500

    # Payment Statistics

    total_payments = Payment.objects.count()

    paid_payments = Payment.objects.filter(
        status='Paid'
    ).count()

    refunded_payments = Payment.objects.filter(
        status='Refunded'
    ).count()

    # Recent Data

    recent_bookings = Booking.objects.order_by(
        '-booked_at'
    )[:5]

    latest_users = User.objects.order_by(
        '-date_joined'
    )[:5]

    latest_events = Event.objects.order_by(
        '-date'
    )[:5]

    # Category Wise Bookings

    category_bookings = Booking.objects.filter(
        status='confirmed'
    ).select_related(
        'user',
        'event'
    )

    # Category Wise Event Counts

    concerts = Event.objects.filter(
        category='Concerts & Live Music Performances'
    ).count()

    corporate = Event.objects.filter(
        category='Corporate & Business Events'
    ).count()

    social = Event.objects.filter(
        category='Social & Private Events'
    ).count()

    community = Event.objects.filter(
        category='Community & Cultural Events'
    ).count()

    sports = Event.objects.filter(
        category='Sports & Wellness'
    ).count()

    workshops = Event.objects.filter(
        category='Educational & Workshop Events'
    ).count()

    # Category Wise Revenue

    concert_revenue = sum(
        payment.amount
        for payment in Payment.objects.filter(
            booking__event__category='Concerts & Live Music Performances',
            status='Paid'
        )
    )

    corporate_revenue = sum(
        payment.amount
        for payment in Payment.objects.filter(
            booking__event__category='Corporate & Business Events',
            status='Paid'
        )
    )

    social_revenue = sum(
        payment.amount
        for payment in Payment.objects.filter(
            booking__event__category='Social & Private Events',
            status='Paid'
        )
    )

    community_revenue = sum(
        payment.amount
        for payment in Payment.objects.filter(
            booking__event__category='Community & Cultural Events',
            status='Paid'
        )
    )

    sports_revenue = sum(
        payment.amount
        for payment in Payment.objects.filter(
            booking__event__category='Sports & Wellness',
            status='Paid'
        )
    )

    workshops_revenue = sum(
        payment.amount
        for payment in Payment.objects.filter(
            booking__event__category='Educational & Workshop Events',
            status='Paid'
        )
    )

    context = {

        'total_users': total_users,
        'total_events': total_events,
        'total_bookings': total_bookings,
        'revenue': revenue,

        'confirmed': confirmed,
        'cancelled': cancelled,
        'pending': pending,

        'total_payments': total_payments,
        'paid_payments': paid_payments,
        'refunded_payments': refunded_payments,

        'recent_bookings': recent_bookings,
        'latest_users': latest_users,
        'latest_events': latest_events,

        'category_bookings': category_bookings,

        'concerts': concerts,
        'corporate': corporate,
        'social': social,
        'community': community,
        'sports': sports,
        'workshops': workshops,

        'concert_revenue': concert_revenue,
        'corporate_revenue': corporate_revenue,
        'social_revenue': social_revenue,
        'community_revenue': community_revenue,
        'sports_revenue': sports_revenue,
        'workshops_revenue': workshops_revenue,
    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )
    # ==========================================
# PDF REPORT FUNCTION
# PASTE HERE
# ==========================================

def admin_report(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="admin_report.pdf"'
    )

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Event Management System Report",
            styles['Title']
        )
    )

    elements.append(
        Spacer(1,20)
    )

    data = [[
        'User',
        'Event',
        'Category',
        'Seats',
        'Amount'
    ]]

    bookings = Booking.objects.filter(
        status='confirmed'
    )

    for booking in bookings:

        amount = 0

        if hasattr(booking, 'payment'):
            amount = booking.payment.amount

        data.append([

            booking.user.username,
            booking.event.title,
            booking.event.category,
            str(booking.quantity),
            str(amount)

        ])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ('BACKGROUND',(0,0),(-1,0),colors.grey),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('GRID',(0,0),(-1,-1),1,colors.black),

        ])

    )

    elements.append(table)

    doc.build(elements)

    return response
def export_excel_report(request):
 
    workbook = openpyxl.Workbook()

    sheet = workbook.active

    sheet.title = "Bookings Report"

    sheet.append([
        'User',
        'Event',
        'Category',
        'Seats',
        'Amount Paid'
    ])

    bookings = Booking.objects.filter(
        status='confirmed'
    )

    for booking in bookings:

        amount = 0

        if hasattr(booking, 'payment'):
            amount = booking.payment.amount

        sheet.append([
            booking.user.username,
            booking.event.title,
            booking.event.category,
            booking.quantity,
            amount
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = (
        'attachment; filename="admin_report.xlsx"'
    )

    workbook.save(response)

    return response