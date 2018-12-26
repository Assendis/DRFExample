# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.test import TestCase, Client
from .models import Project, Comments
from rest_framework.response import Response
from .serializers import ProjectSerializer
from rest_framework import status
from .views import ProjectViewSet

client= Client()

class ProjectTest(TestCase):

    def setUp(self):
        Project.objects.create(
            project_name='Python',
            pub_date='1999-10-22 09:09',
            about_what='python',
            comments='python çok güzel bişi')

    def test_project_breed(self):
        project = Project.objects.get(project_name='Python')
        self.assertEqual(project.about_what, 'python')

    def test_update_project(self):
        project = Project.objects.get(project_name='Python')
        project.project_name = 'PyPy'
        project.save()

        self.assertEqual(project.project_name, 'PyPy')

    def test_delete_project(self):
        project = Project.objects.get(project_name='Python')
        project.delete()
        self.assertNotIn(project, Project.objects.all())

    def test_get_all_projects(self):
        response = client.get(reverse('projects-all'))
        pro = Project.objects.all()
        serializer = ProjectSerializer(pro, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
