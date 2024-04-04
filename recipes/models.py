from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    """Модель рецепта в БД"""
    name = models.CharField(max_length=150)
    discription = models.CharField(max_length=1000)
    step = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author')
    ingredient = models.CharField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    """Модель категории в БД"""
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Recipe_Category(models.Model):
    """Модель связующей таблицы рецептаи категорий в БД"""
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe')
    catigory = models.ManyToManyField('Category', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return f'{self.recipe}'