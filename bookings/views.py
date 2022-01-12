from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from bookings.models import Booking
from bookings.serializers import BookingSerializer

# Create your views here.


@csrf_exempt
def list_booking(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pay_booking(request, pk):
    if request.method == 'PUT':

        try:
            booking = Booking.objects.get(pk=pk)
            if booking.state != Booking.PENDING:
                error = {
                    "error": "El estado de la reserva debe ser Pendiente"
                }
                return JsonResponse(error, status=400)
            else:
                booking.state = Booking.PAID_OUT
                booking.save()
                return HttpResponse(status=200)
        except Booking.DoesNotExist:
            return HttpResponse(status=404)

    else:
        return HttpResponse(status=404)


@csrf_exempt
def cancel_booking(request, pk):
    if request.method == 'PUT':

        try:
            booking = Booking.objects.get(pk=pk)
            if booking.state != Booking.PENDING:
                error = {
                    "error": "El estado de la reserva debe ser Pendiente"
                }
                return JsonResponse(error, status=400)
            else:
                booking.state = Booking.DELETED
                booking.save()
                return HttpResponse(status=200)
        except Booking.DoesNotExist:
            return HttpResponse(status=404)

    else:
        return HttpResponse(status=404)
