from django.contrib import admin

from .models import (Favorites, Follow, Ingredient, IngredientInRecipe,
                     Purchase, Recipe, Tag)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('^name',)
    list_filter = ('name',)


class IngredientInRecipeAdmin(admin.TabularInline):
    model = IngredientInRecipe
    fk_name = 'recipe'
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'favorited')
    list_filter = ('author', 'name', 'tags')
    exclude = ('ingredients',)

    inlines = [
        IngredientInRecipeAdmin,
    ]

    def favorited(self, obj):
        favorited_count = Favorites.objects.filter(recipe=obj).count()
        return favorited_count


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Favorites, FavoriteAdmin)
admin.site.register(Follow, SubscriptionAdmin)
admin.site.register(IngredientInRecipe, RecipeIngredientAdmin)
