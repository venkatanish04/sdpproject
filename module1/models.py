from django.db import models


class Anish(models.Model):
    # inside all are columns only in database
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()

    class Meta:
        db_table = "Register"


class Feedback(models.Model):

    FirstName = models.TextField(max_length=255)
    LastName = models.TextField(max_length=255)
    Email = models.EmailField(primary_key=True)
    Comment = models.TextField(max_length=255)

    class Meta:
        db_table = "Feedback"
