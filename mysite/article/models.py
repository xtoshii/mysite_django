from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mdeditor.fields import MDTextField
import markdown
from django.utils.html import strip_tags

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogArticle(models.Model):
    title = models.CharField(max_length=300)
    # author = models.ForeignKey(User,on_delete=models.CASCADE,)
    body = MDTextField()
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0, editable=False)
    publish = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, default=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)


    class Meta():
        ordering = ('-publish',)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


    def __str__(self):
        return self.title



