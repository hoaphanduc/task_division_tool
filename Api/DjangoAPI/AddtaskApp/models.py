from django.db import models
from django.contrib.auth.models import AbstractUser
class tasks(models.Model):
    title=models.CharField(max_length=40, null=False)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status=models.IntegerField(default=2, choices=[
        (0, 'done'),
        (1, 'pending'),
        (2,  'Not target')

    ])
    numberofrequest=models.IntegerField(null=True)
    teamPic = models.IntegerField(null=True)
    def __str__(self):
        return self.title

class users(models.Model):
    account=models.CharField(max_length=16, null=False, unique=True)
    password=models.CharField(max_length=8, null=False)
    name=models.CharField(max_length=30, null=False)
    role=models.IntegerField(default=2,choices=[
        (0, 'admin'),
        (1, 'lead'),
        (2, 'user'),
    ])
    request= models.IntegerField(default=0, null=False)
    team=  models.ForeignKey(tasks, on_delete=models.CASCADE,db_column='teamPic',related_name='pic')
    def __str__(self):
        return self.name