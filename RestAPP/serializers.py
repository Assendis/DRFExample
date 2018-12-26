from RestAPP.models import Project, Comments
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields = '__all__'


