from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from bookings.models import Booking
from payments.models import Payment

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

import qrcode
from io import BytesIO


def download_ticket(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    payment = get_object_or_404(
        Payment,
        booking=booking
    )

    # QR Data
    qr_data = f"""
Booking ID: {booking.id}
Event: {booking.event.title}
User: {booking.user.username}
Seats: {booking.quantity}
Amount Paid: ₹{payment.amount}
Transaction ID: {payment.transaction_id}
"""

    qr = qrcode.make(qr_data)

    buffer = BytesIO()
    qr.save(buffer)
    buffer.seek(0)

    qr_image = ImageReader(buffer)

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = f'attachment; filename="ticket_{booking.id}.pdf"'

    p = canvas.Canvas(response)

    # Title
    p.setFont(
        "Helvetica-Bold",
        18
    )

    p.drawString(
        190,
        800,
        "EVENT TICKET"
    )

    p.line(
        50,
        780,
        550,
        780
    )

    p.setFont(
        "Helvetica",
        12
    )

    # Ticket Details
    p.drawString(
        50,
        740,
        f"Event : {booking.event.title}"
    )

    p.drawString(
        50,
        710,
        f"User : {booking.user.username}"
    )

    p.drawString(
        50,
        680,
        f"Booking ID : {booking.id}"
    )

    p.drawString(
        50,
        650,
        f"Transaction ID : {payment.transaction_id}"
    )

    p.drawString(
        50,
        620,
        f"Status : {booking.status}"
    )

    p.drawString(
        50,
        590,
        f"Date : {booking.event.date}"
    )

    p.drawString(
        50,
        560,
        f"Location : {booking.event.location}"
    )

    p.drawString(
        50,
        530,
        f"Seats : {booking.quantity}"
    )

    p.drawString(
        50,
        500,
        f"Amount Paid : ₹{payment.amount}"
    )

    # QR Code
    p.drawImage(
        qr_image,
        380,
        500,
        width=120,
        height=120
    )

    # Footer line
    p.line(
        50,
        460,
        550,
        460
    )

    p.setFont(
        "Helvetica-Bold",
        13
    )

    p.drawString(
        50,
        430,
        "Thank you for booking!"
    )

    p.drawString(
        50,
        405,
        "Please carry this ticket while attending the event."
    )

    p.showPage()
    p.save()

    return response