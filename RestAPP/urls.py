from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .models import Project
from .serializers import ProjectSerializer

from .views import ProjectViewSet, CommentViewSet, MyCustomAPIView

router = routers.DefaultRouter()

router.register(r'project', MyCustomAPIView, basename='custom_api_view')
router.register(r'comments', CommentViewSet)

urlpatterns = [
       url(r'^', include(router.urls)),
]

