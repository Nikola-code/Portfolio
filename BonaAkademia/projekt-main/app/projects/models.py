from django.db import models
from django.utils.translation import gettext_lazy as _

from workers.models import Worker


class Client(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return '%s' % (self.name)


class Project(models.Model):

    class Status(models.TextChoices):
        PLANNED = 'P', _('Planned')
        ACTIVE = 'A', _('Active')
        MAINTENANCE = 'M', _('Maintenance')
        CLOSED = 'C', _('Closed')

    shortcut = models.CharField(max_length=64)
    fullName = models.CharField(max_length=256)
    client = models.ForeignKey(
        Client, related_name='P_client', on_delete=models.CASCADE)
    projectNum = models.IntegerField()
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.PLANNED,
    )
    leader = models.ForeignKey(
        Worker, related_name='P_leader', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullName + " (" + self.shortcut + ")"
