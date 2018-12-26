# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    about_what = models.CharField(max_length=200)
    comments = models.TextField


#class Choice(models.Model):
#    question = models.ForeignKey(Project, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

class Comments(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    username = models.CharField(max_length=100)