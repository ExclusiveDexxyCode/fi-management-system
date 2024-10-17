from django.db import models
from teams.models import TeamModel

# Create your models here.
class DriverModel( models.Model):
    name = models.CharField(max_length=200, blank=True)
    nationality = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField()
    team = models.ManyToManyField(TeamModel)
    championship_won = models.IntegerField(default=0, blank=True)