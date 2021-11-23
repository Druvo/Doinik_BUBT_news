from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
