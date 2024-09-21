from rest_framework import serializers
from . import models

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.projectImage
        fields = ['image', 'is_video', 'is_image']


class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ['id', 'name', 'description', 'main_image', 'images']


######################################################################
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'


######################################################################
class DoorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Door
        fields = '__all__'


class DoorColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.doorColor
        fields = ['color_name','color_image']


class DoorDetailSerializer(serializers.ModelSerializer):
    colors = DoorColorSerializer(many=True, read_only=True)

    class Meta:
        model = models.Door
        fields = ['id', 'name', 'description', 'additionalInfo', 'colors']


######################################################################
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'
