from django.shortcuts import render
from rest_framework import generics
from bookings.models import Seat, Ticket
from bookings.serializers import SeatSerializer, BookTicketSerailizer
# Create your views here.


class SeatList(generics.ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        filters = {}
        filters['theatre__theatre_id'] = self.kwargs['theatre_id']
        filters['show__id'] = self.kwargs['show_id']
        seat_list = Seat.objects.filter(**filters)
        return seat_list


class BookTicket(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = BookTicketSerailizer
