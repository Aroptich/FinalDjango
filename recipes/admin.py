from django.contrib import admin

from recipes.models import Recipe, Recipe_Category, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'ingredient', 'created']


@admin.register(Recipe_Category)
class Recipe_CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']