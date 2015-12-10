from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name="User")
    code = models.CharField("Code", max_length=100)

    expire_timestamp = models.DateTimeField()

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)
