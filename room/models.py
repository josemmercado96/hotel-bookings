from django.db import models

# Create your models here.


class Room(models.Model):

    code_room = models.CharField(max_length=10, unique=True, null=False)
    beds = models.PositiveIntegerField(default=1)
    is_suite = models.BooleanField(default=False, null=False)

    def __str__(self):
        return "{}".format(self.code_room)
