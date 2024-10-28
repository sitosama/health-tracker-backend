from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Sleep, Exercise, Diet
from .serializers import SleepSerializer, ExerciseSerializer, DietSerializer

# Create your views here.


class SleepViewSet(viewsets.ModelViewSet):  # ModelViewSetを継承していることを確認
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer


# class SleepViewSet(generics.CreateAPIView):
#     queryset = Sleep.objects.all()
#     serializer_class = SleepSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
