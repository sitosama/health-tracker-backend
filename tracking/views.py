from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Sleep, Exercise, Diet
from .serializers import SleepSerializer, ExerciseSerializer, DietSerializer

# Create your views here.


class SleepViewSet(viewsets.ModelViewSet):  # ModelViewSetを継承していることを確認
    # class SleepViewSet(generics.ListAPIView):　こいつを使うとget_extra_actionsという属性が存在しないために発生
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
