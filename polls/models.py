from pyexpat import model
from secrets import choice
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=300)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=280)

    def __str__(self):
        return self.choice
