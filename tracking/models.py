from django.db import models


# Create your models here.
class Sleep(models.Model):
    date = models.DateField()
    sleep_duration = models.FloatField()  # 睡眠時間（時間単位）
    sleep_quality = models.CharField(max_length=50)


class Exercise(models.Model):
    date = models.DateField()
    exercise_type = models.CharField(
        max_length=100, default="運動未定義"
    )  # デフォルト値を設定
    duration = models.IntegerField()  # 運動時間（分）
    intensity = models.CharField(max_length=10, default="中")  # デフォルト値を設定

    def __str__(self):
        return f"{self.date} - {self.exercise_type} - {self.duration}分"


class Diet(models.Model):
    date = models.DateField()
    meal_type = models.CharField(
        max_length=50
    )  # 食事の種類（朝食、昼食、夕食、スナック）
    calories = models.IntegerField()  # カロリー
    notes = models.TextField(blank=True, null=True)  # メモ（オプション）

    def __str__(self):
        return f"{self.date} - {self.meal_type} - {self.calories} kcal"
