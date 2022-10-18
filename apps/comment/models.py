from django.db import models
from apps.blog.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='media/')
    email = models.EmailField()
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


