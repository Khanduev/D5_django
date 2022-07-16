from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='articles')
    publication = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE, related_name='articles', null=True)


    def __str__(self):
        return f'{self.name.title()} ({self.publication:"%H:%M %d.%m.%Y"}) {self.description[:10000]}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Creator (models.Model):
    creator = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.creator.title()
