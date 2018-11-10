from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

from .managers import PublishedManager


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    objects = models.Manager()
    published = PublishedManager()

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish', )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])
