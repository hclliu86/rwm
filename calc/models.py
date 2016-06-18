from django.db import models

# Create your models here.


class CalcTest(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=23)

    def __str__(self):
        return self.name


class TestDataOutput(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)

    def __str__(self):
        return self.title1