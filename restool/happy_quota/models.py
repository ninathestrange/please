import datetime

from django.db import models
from django.utils import timezone


class LeadForProject(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class WannaAdd(models.Model):
    question = models.ForeignKey(LeadForProject, on_delete=models.CASCADE)
    add_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.add_text
