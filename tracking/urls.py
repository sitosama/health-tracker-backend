from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SleepViewSet, ExerciseViewSet, DietViewSet
from . import views

router = DefaultRouter()
router.register(r"sleep", SleepViewSet)  # 'sleep' エンドポイントを登録
router.register(r"exercise", ExerciseViewSet)
router.register(r"diet", DietViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("sleep/", views.SleepViewSet.as_view({"get": "list"}), name="sleep-create"),
    path(
        "Exercise/", views.ExerciseViewSet.as_view({"get": "list"}), name="sleep-create"
    ),
    path("Diet/", views.DietViewSet.as_view({"get": "list"}), name="sleep-create"),
]
