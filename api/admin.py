from django.contrib import admin

from.models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    empty_value_display = 'Пустое значение'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    empty_value_display = 'Пустое значение'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category')
    search_fields = ('name', 'year')
    list_filter = ('year', 'genre', 'category')
    empty_value_display = 'Пустое значение'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
