from enum import unique
from django.db import models

# Create your models here.


class Client(models.Model):

    dni = models.CharField('dni', max_length=10, unique=True, null=False, blank=False)
    name = models.CharField('name', max_length=50, null=False, blank=False)
    is_company = models.BooleanField(
        'is company',
        default=False,
        help_text="If the client is a company, check true"
    )
