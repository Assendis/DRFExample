from RestAPP.models import Project, Comments
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = ('project_name',
                  'pub_date',
                  'about_what',
                  'comments')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields = ('text',
                  'comment',
                  'username')