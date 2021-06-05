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


class TitleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    # OR:
    # category = serializers.SlugRelatedField(
    #     slug_field=['name','slug'],
    #     read_only=True
    # )
    genre = GenreSerializer(many=True, read_only=True)
    # OR:
    # genre = serializers.SlugRelatedField(
    #     slug_field='slug',
    #     read_only=True,
    #     many=True
    # )
    # +
    # rating = .....

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title
