from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime as dt
from django.utils.translation import gettext_lazy as _



def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug=models.CharField(max_length=100,null=True)
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering = ('-name',)
    def __str__(self):
        return self.name



class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='d1.jpg')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    now=timezone.make_aware(dt.datetime.now(),timezone.get_current_timezone())
    published = models.DateTimeField(default=now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    post_objects = PostObjects()  # custom manager

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"
        ordering = ('-published',)

    def __str__(self):
        return self.title