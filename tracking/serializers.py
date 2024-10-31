# データをJSON形式で返すためのシリアライザを定義
from rest_framework import serializers
from .models import Sleep, Exercise, Diet


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = "__all__"
