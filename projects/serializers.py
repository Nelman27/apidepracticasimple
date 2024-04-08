from rest_framework import serializers
from .models import Project

#create your models here
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model:Project
        fields='__all__'
        read_only_fields=('created_at', )