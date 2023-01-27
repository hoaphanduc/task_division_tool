from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import tasks, users
from .serializers import AddtaskSerializer, AssigntaskSerializer

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

class AssigntaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tasks.objects.all()
    serializer_class = AssigntaskSerializer
