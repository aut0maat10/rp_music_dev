from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = MarkdownxField()
    # body = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images/')
    # blurb = models.TextField(max_length=200, blank=True, default='')
    blurb = MarkdownxField()
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField(
        'Post', related_name='categories', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
