from django.db import models
from django.contrib.auth.models import User
from block.models import Block
# Create your models here.


class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name='Block')
    owner = models.ForeignKey(User, verbose_name='Author')
    title = models.CharField('Title', max_length=100)
    content = models.CharField('Content', max_length=10000)
    status = models.IntegerField('Status', choices=((0, 'normal'), (-1, 'deleted'), (10, 'Selected')), default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
