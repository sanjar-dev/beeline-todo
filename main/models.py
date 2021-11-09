from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    persone = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=12)
    date_meeting = models.DateField()
    is_done = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class MonthGoal(models.Model):
    goal = models.CharField(max_length=100)
    goal_description = models.CharField(max_length=200)
    month = models.DateField()
    
    dif_easy = "EASY"
    dif_normal = "NORMAL"
    dif_hard = "HARD"

    difficulty_choices = ([
        (dif_easy, "Easy"),
        (dif_normal, "Normal"),
        (dif_hard, "Hard")
    ])

    difficulty = models.CharField(max_length=6, choices=difficulty_choices, default=dif_normal)
