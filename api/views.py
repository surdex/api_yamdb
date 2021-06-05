from rest_framework.pagination import PageNumberPagination
# from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Category, Genre, Title
from .permissions import IsUserIsAdmin
from .serializers import CategorySerializer, GenreSerializer, TitleCreateSerializer, TitleGetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TitleFilter


class CustomMixin(ListModelMixin,
                  CreateModelMixin,
                  DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class CategoryViewSet(CustomMixin):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] # , IsUserIsAdmin
    serializer_class = CategorySerializer
    lookup_field = 'slug' # - NB 1111
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


class GenreViewSet(CustomMixin):
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] # , IsUserIsAdmin
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] # , IsUserIsAdmin
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action == ('create' or 'partial_update'):
            return TitleCreateSerializer
        return TitleGetSerializer
