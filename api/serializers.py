from rest_framework import serializers

from .models import Category, Genre, Title

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(
    #     slug_field=['name','slug'],
    #     read_only=True
    # )
    category = CategorySerializer(read_only=True)
    # genre = serializers.SlugRelatedField(
    #     slug_field='slug',
    #     read_only=True,
    #     many=True
    # )
    genre = GenreSerializer(many=True, read_only=True)
    class Meta:
        # fields = ('category', 'genre', 'name', 'year')
        fields = '__all__'
        model = Title

