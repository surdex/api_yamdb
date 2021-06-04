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
    category = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True,
        many=True
    )
    class Meta:
        fields = ('category', 'genre', 'name', 'year')
        model = Title

