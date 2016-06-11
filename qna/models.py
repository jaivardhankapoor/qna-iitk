from django.db import models
from django.utils import timezone
from accounts import UserProfile



class Question(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max-length=255, null=True, blank=True)
    content = models.TextField(max_length=4000)
    create_user = models.ForeignKey(User)
