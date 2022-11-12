from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(User,  # +
                               verbose_name='Автор',
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               )
    name = models.CharField()
    image = models.ImageField()
    text = models.TextField()
    cooking_time = models.PositiveBigIntegerField()
    pub_date = models.DateTimeField()
    ingredients = models.ManyToManyField()
    tag = models.ManyToManyField()


class Tag(models.Model):
    name = models.CharField()
    color = models.CharField()
    slug = models.SlugField()


class Ingredient(models.Model):
    name = models.CharField()
    unit = models.CharField()


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
        related_name='ingredients_amounts',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество ингредиента',
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        unique_together = ('ingredient', 'recipe')
        constraints = [
            models.UniqueConstraint(
                fields=['ingredient', 'recipe'],
                name='recipe_ingredient_unique',
            )
        ]


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_subscriber',)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipe')
    data_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    subscription_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата подписки'
    )


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='customers'
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
    )
