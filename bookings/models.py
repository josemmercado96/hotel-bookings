from django.db import models
from room.models import Room
from clients.models import Client

# Create your models here.


class Booking(models.Model):

    CREDIT_CARD = 'CC'
    CASH = 'CASH'
    WIRE_TRANSFER = 'WT'

    PAYMENT_METHOD_CHOICES = [
        (CREDIT_CARD, 'Credit Card'),
        (CASH, 'Cash'),
        (WIRE_TRANSFER, 'Wire Transfer'),
    ]

    PENDING = 'P'
    PAID_OUT = 'P0'
    DELETED = 'D'

    STATES_BOOKING = [
        (PENDING, 'Pending'),
        (PAID_OUT, 'Paid Out'),
        (DELETED, 'Deleted'),
    ]

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    start_date = models.DateField('start date',null=False)
    amount = models.DecimalField('amount', null=False, blank=False, decimal_places=2, max_digits=10)
    days = models.PositiveIntegerField('days', null=False, blank=False, default=1)
    payment_method = models.CharField(
        'payment method', 
        max_length=4, 
        choices=PAYMENT_METHOD_CHOICES, 
        default=CASH
    )
    state = models.CharField('state', max_length=2, choices=STATES_BOOKING, default=PENDING)
    room = models.ForeignKey(Room, null=False, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
