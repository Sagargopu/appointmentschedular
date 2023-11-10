from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import UserProfiles
from django.dispatch import receiver