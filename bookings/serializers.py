from rest_framework import serializers
from bookings.models import Seat, Ticket
from theatres.models import Theatre, Show
from bookings.services import MailTickets


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret['seat_code']


class BookTicketSerailizer(serializers.ModelSerializer):
    seats = serializers.ListField(write_only=True)
    email = serializers.EmailField()
    theatre_id = serializers.IntegerField(write_only=True)
    show_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        seat_filters = {}
        seat_filters['theatre__theatre_id'] = validated_data.get('theatre_id')
        seat_filters['show__id'] = validated_data.get('show_id')

        for seat_code in validated_data.get('seats'):
            try:
                seat_filters['seat_code'] = seat_code
                seat = Seat.objects.filter(**seat_filters)
                if len(seat) > 0:
                    raise serializers.ValidationError(
                        "Selected Tickets were booked!", code=400)
            except Exception as e:
                raise serializers.ValidationError(e)

        # Till now no one booked those selected tickets.
        # critical Section starts here...

        try:
            theatre = Theatre.objects.get(
                pk=validated_data.get('theatre_id'))
            show = Show.objects.get(
                pk=validated_data.get('show_id'))
        except Exception as e:
            raise serializers.ValidationError(e)

        ticket = Ticket.objects.create(email=validated_data['email'])

        for seat_code in validated_data.get('seats'):
            try:
                seat = Seat.objects.create(
                    seat_code=seat_code, theatre=theatre, show=show)
                ticket.seats.add(seat)
            except Exception as e:
                raise serializers.ValidationError(e)
        ticket.save()
        MailTickets(ticket=ticket, seats=", ".join(validated_data['seats']))
        return ticket
