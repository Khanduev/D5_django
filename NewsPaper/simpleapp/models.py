from django.db import models


class Article(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='articles',
    )
    publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()} ({self.publication:"%d %b %Y"}) {self.description[:10000]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

