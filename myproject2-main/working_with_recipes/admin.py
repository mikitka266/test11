from django.contrib import admin
from .models import Recipe, RecipeCategories, ToLinkRecipesAndCategories


admin.site.register(Recipe)
admin.site.register(RecipeCategories)
admin.site.register(ToLinkRecipesAndCategories)