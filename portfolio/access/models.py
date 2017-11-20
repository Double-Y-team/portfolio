from django.db import models
from django.contrib.auth.models import User


class Moderator(User):
    user = models.OneToOneField(User)
    front_end = models.CharField(max_length=128)



