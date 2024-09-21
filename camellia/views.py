from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from . import models
from rest_framework.response import Response
from . import serializers

@api_view(['GET','POST'])
def project_list(request):
    if request.method == 'GET':
        projects = models.Project.objects.all()
        serializer = serializers.ProjectCreateSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def project_detail(request, pk):
    try:
        project = models.Project.objects.get(pk=pk)
    except models.Project.DoesNotExist:
        return Response({"error":"Project Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.ProjectDetailSerializer(project)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ProjectDetailSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################################################################################################
@api_view(['GET','POST'])
def projectimage_list(request):
    if request.method == 'GET':
        projectimages = models.projectImage.objects.all()
        serializer = serializers.ProjectImageSerializer(projectimages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.ProjectImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def projectimage_detail(request, pk):
    try:
        projectimage = models.projectImage.objects.get(pk=pk)
    except models.projectImage.DoesNotExist:
        return Response({"error":"Project Image Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.ProjectImageSerializer(projectimage)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ProjectImageSerializer(projectimage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        projectimage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################################################################################
@api_view(['GET','POST'])
def material_list(request):
    if request.method == 'GET':
        materials = models.Material.objects.all()
        serializer = serializers.MaterialSerializer(materials, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def material_detail(request, pk):
    try:
        material = models.Material.objects.get(pk=pk)
    except models.Material.DoesNotExist:
        return Response({"error":"Material Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.MaterialSerializer(material)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.MaterialSerializer(material,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##############################################################################################


@api_view(['GET','POST'])
def door_list(request):
    if request.method == 'GET':
        doors = models.Door.objects.all()
        serializer = serializers.DoorCreateSerializer(doors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.DoorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def door_detail(request, pk):
    try:
        door = models.Door.objects.get(pk=pk)
    except models.Door.DoesNotExist:
        return Response({"error":"Door Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.DoorDetailSerializer(door)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DoorDetailSerializer(door, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        door.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###########################################################################################


@api_view(['GET','POST'])
def doorcolor_list(request):
    if request.method == 'GET':
        doorcolors = models.doorColor.objects.all()
        serializer = serializers.DoorColorSerializer(doorcolors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.DoorColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def doorcolor_detail(request, pk):
    try:
        doorcolor = models.doorColor.objects.get(pk=pk)
    except models.doorColor.DoesNotExist:
        return Response({"error":"Door Color Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.DoorColorSerializer(doorcolor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DoorColorSerializer(doorcolor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        doorcolor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###############################################################################################


@api_view(['GET','POST'])
def location_list(request):
    if request.method == 'GET':
        locations = models.Location.objects.all()
        serializer = serializers.LocationSerializer(locations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def location_detail(request, pk):
    try:
        location = models.Location.objects.get(pk=pk)
    except models.Location.DoesNotExist:
        return Response({"error":"Location Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.LocationSerializer(location)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)