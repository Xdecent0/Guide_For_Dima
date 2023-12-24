from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте дополнительные поля профиля пользователя, если нужно

    def __str__(self):
        return self.user.username

class Table(models.Model):
    SHAPE_CHOICES = [
        ('oval', 'Овальный'),
        ('rectangle', 'Прямоугольный'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shape = models.CharField(max_length=10, choices=SHAPE_CHOICES, default='rectangle')
    capacity = models.IntegerField()
    number = models.IntegerField(unique=True)
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"Стол {self.number} ({self.get_shape_display()}, {self.capacity} мест)"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # Добавьте дополнительные поля для бронирования, например, количество гостей и комментарий

    def __str__(self):
        return f"{self.user.username} - Стол {self.table.number} ({self.date} {self.time})"
