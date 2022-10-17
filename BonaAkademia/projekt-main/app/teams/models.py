from django.db import models
from workers.models import Worker

class Team(models.Model):
	shortcut = models.CharField(max_length=64)
	fullName = models.CharField(max_length=256)
	leader = models.ForeignKey(
		Worker,
		related_name='T_leader',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return f"{self.shortcut} ({self.fullName})"

class TeamMembership(models.Model):
	worker = models.ForeignKey(
		Worker,
		related_name='T_worker',
		on_delete=models.CASCADE
	)
	team = models.ForeignKey(
		Team,
		related_name='T_team',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return f"{self.worker} - {self.team}"

