from django.db import models
from Core.models.user import User
from post.models import Category


class Post(models.Model):
    ''' Create Post Models '''
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='author'
    )
    title = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='category'
    )
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    total_view = models.PositiveBigIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    is_hot = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, related_name='blog', null=True
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=25, blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to="comment_image", null=True)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True)
    total_like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @classmethod
    def is_parent(self):
        if self.parent.field.name is not None:
            return False
        return True
