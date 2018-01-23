from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=20)
    favourite = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=20)
    note = models.TextField(null=True)
    accessible = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField(null=True)
    acquired = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Objective(models.Model):
    name = models.CharField(max_length=20)
    skill = models.ForeignKey(Skill, null=True, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    note = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
