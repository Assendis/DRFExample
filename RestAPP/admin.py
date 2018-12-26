# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Project, Comments



class ProjectAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'project_name', 'about_what']

admin.site.register(Project, ProjectAdmin)

#class ChoicesAdmin(admin.ModelAdmin):
#    fields = ['choice_text', 'question', 'votes']
#admin.site.register(Choice, ChoicesAdmin)
admin.site.register(Comments)



