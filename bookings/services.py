from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def MailTickets(ticket, seats):
    email = EmailMessage(
        subject="Booking Conformed!",
        body=f'Ticket Details :\n Ticket id = {ticket.ticket_id}\n Seats : {seats} \n Booking Time : {ticket.booking_time.strftime("%c")}',
        from_email=settings.EMAIL_HOST_USER,
        to=[ticket.email]
    )
    email.send(fail_silently=False)
