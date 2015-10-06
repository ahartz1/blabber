from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
    # Note parentheses after; instances of classes
    # id is automatic
    text = models.CharField(max_length=141)
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)
    # this is how the relations are made within db


class Favorite(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
