from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Block(models.Model):
    name = models.CharField('Name', max_length=30)
    desc = models.CharField('Description', max_length=150)
    manager = models.ForeignKey(User, verbose_name='author')

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'block'
        verbose_name_plural = 'blocks'