from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    intro = models.CharField(max_length=255, null=True, blank=True)  
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_first = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField( null=True, blank=True, upload_to="posts")
    categories = models.ManyToManyField("Category", related_name="posts")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return reverse("blog_detail", args=[str(self.id)])


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"