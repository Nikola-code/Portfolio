from django.db import models
from django.utils.translation import gettext_lazy as _


class Worker(models.Model):

    class Role(models.TextChoices):
        WORKER = 'W', _('Worker')
        LEADER = 'L', _('Leader')
        ADMIN = 'A', _('Admin')

    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    role = models.CharField(
        max_length=1,
        choices=Role.choices,
        default=Role.WORKER,
    )
    status = models.BooleanField(default=1)
    workHours = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName + " (" + self.email + ")"


class Week(models.Model):
    weekName = models.CharField(max_length=16)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    hours = models.IntegerField(default=40)

    def __str__(self):
        return str(self.weekName) + " (" + str(self.hours) + ")"


class JobTime(models.Model):
    worker = models.ForeignKey(
        Worker, related_name='JT_worker', on_delete=models.CASCADE)
    project = models.ForeignKey(
        'projects.Project', related_name='JT_project', on_delete=models.CASCADE)
    week = models.ForeignKey(Week, related_name='JT_week',
                             on_delete=models.CASCADE)
    workPart = models.FloatField(default=40, blank=True, null=True)
    availability = models.FloatField(default=40, blank=True)

    def __str__(self):
        return str(self.worker.firstName) + " " + str(self.worker.lastName) + " - " + str(self.week.weekName)

