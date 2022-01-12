from rest_framework import serializers

from bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('__all__')

    room_code = serializers.CharField(source='room.code_room', required=False)
    client_name = serializers.CharField(source='client.name', required=False)
    client_dni = serializers.CharField(source='client.dni', required=False)
