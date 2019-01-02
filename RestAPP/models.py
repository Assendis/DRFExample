# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Comments(models.Model):
    comment = models.CharField(max_length=1000, null=True)
    username = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published', null=True)
    about_what = models.CharField(max_length=200, null=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)


#class Choice(models.Model):
#    question = models.ForeignKey(Project, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

