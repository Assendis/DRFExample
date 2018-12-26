from django.urls import path
from .views import ProjectViewSet, CommentViewSet, get_delete_update_project, get_post_project

urlpatterns = [
    path('projects/', get_post_project, name="projects-all"),
    path('projects/<int:pk>', get_delete_update_project, name="project-del-up"),
    path('comments/', CommentViewSet.as_view({'get': 'list'}), name="comments-all"),
]