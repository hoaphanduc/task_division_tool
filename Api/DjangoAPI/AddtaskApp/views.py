from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import tasks, users
from .serializers import AddtaskSerializer, AssigntaskSerializer, ProjectsSerializer, PicsSerializer

from rest_framework import status
from rest_framework import generics


class AddtaskList(generics.ListCreateAPIView):
    model = tasks
    serializer_class = AddtaskSerializer

    def get_queryset(self):
        return tasks.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = AddtaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class AddtaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tasks.objects.all()
    serializer_class = AddtaskSerializer

class AssigntaskList(generics.ListCreateAPIView):
    queryset = tasks.objects.all()
    serializer_class = AssigntaskSerializer

    def create(self, request, *args, **kwargs):
        task = get_object_or_404(tasks, pk=request.data['project'])
        task.teamPic = request.data['pic']
        task.save()

        return JsonResponse({
            'message': 'Assign a task to a pic successful!'
        }, status=status.HTTP_201_CREATED)

class AssigntaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tasks.objects.all()
    serializer_class = AssigntaskSerializer

class ProjectsList(generics.ListCreateAPIView):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return tasks.objects.filter(teamPic__isnull=True)

class PicsList(generics.ListCreateAPIView):
    serializer_class = PicsSerializer

    def get_queryset(self):
        tasksList = tasks.objects.all()
        return users.objects.exclude(id__in=tasksList.values('teamPic'))