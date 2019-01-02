# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from RestAPP.models import Project, Comments
from RestAPP.serializers import ProjectSerializer, CommentSerializer
from rest_framework import mixins, generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class CommentViewSet(viewsets.ModelViewSet):
    model = Comments
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
#
# class ProjectView(ListCreateAPIView):
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all()
#
#     @classmethod
#     def get_extra_actions(self):
#         return []

class MyCustomAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer




# @api_view(['GET', 'DELETE', 'PUT'])
# def get_delete_update_project(request, pk):
#
#     try:
#         project = Project.objects.get(pk=pk)
#     except Project.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     if request.method == 'GET':
#         serializer = ProjectSerializer(project, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'DELETE':
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     elif request.method == 'PUT':
#         serializer = ProjectSerializer(project, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'POST'])
# def get_post_project(request):
#
#     if request.method == 'GET':
#         project = Project.objects.all()
#         serialize = ProjectSerializer(project, many=True)
#         return Response(serialize.data)
#
#     elif request.method == 'POST':
#         serialize = ProjectSerializer(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)