from django.db import models

# Create your models here.


class TestDb1(models.Model):
    testdb_name = models.CharField(max_length=200)
    testdb_age = models.IntegerField()

    def __str__(self):
        return self.testdb_name