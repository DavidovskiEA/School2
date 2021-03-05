from django.db import models


class School(models.Model):
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.number


class Group(models.Model):
    number = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
