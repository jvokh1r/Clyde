from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='media/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tags = models.CharField(max_length=221)

    def __str__(self):
        return self.tags


class Category(models.Model):
    cat = models.CharField(max_length=221)

    def __str__(self):
        return self.cat



