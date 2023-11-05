from django.db import models
from django.core.validators import MinLengthValidator


class Recipe(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)
    description = models.CharField(max_length=404, validators=[MinLengthValidator(3)], null=False)
    cooking_steps = models.CharField(max_length=404)
    cooking_time_in_seconds = models.IntegerField(null=False)
    photo_of_the_dish = models.FileField(upload_to='my_gallery')
    autor = models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)
    average_price_in_restaurants = models.DecimalField(max_digits=10, decimal_places=2)

    # director2 = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    # actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.name} - {self.autor} - {self.average_price_in_restaurants}'


class RecipeCategories(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.name}'


class ToLinkRecipesAndCategories(models.Model):
    categories = models.ForeignKey(RecipeCategories, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.recipe} - {self.categories}'
