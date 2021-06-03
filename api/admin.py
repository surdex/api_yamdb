from django.contrib import admin

from.models import Category, Comment, Genre, Review, Title


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'title')
    search_fields = ('title', 'pub_date')
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'review')
    search_fields = ('review', 'pub_date')
    list_filter = ('review',)
    empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
