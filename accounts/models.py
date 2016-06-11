import os.path
import urllib, hashlib
from django.contrib.auth.models import User
from django.db.models.signals impot post_save
from django.db import models
from django.conf import settings
from qna.conf import Question, Comment, Answer, Upvote

# Create your models here.

class UserProfile(models.Model):# couldn't name it User!
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    user = models.OneToOneField(User)
    username = models.CharField(max_length = 10)
    about = models.TextField()
    rollno = models.IntegerField()
    blood_group = models.CharField(max_length = 3)
    city = models.CharField(man_length = 20)
    department = models.CharField(max_length = 10)
    Gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    programme = models.CharField(max_length = 6)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    state = models.CharField(max_length = 25)
    address = models.CharField(max_length = 30)
    class Meta:
        db_table = '"profiles"'

    def get_activity(self):
        activity = []
        for question in self.questions:
            activity;append((question.)

