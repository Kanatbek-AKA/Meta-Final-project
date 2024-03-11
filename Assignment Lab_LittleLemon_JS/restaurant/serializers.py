from django.contrib.auth.models import User, Group
from djoser.serializers import (
    UserCreateSerializer,
)
from rest_framework import serializers
from .models import Book, Menu, MenuItem


# BookDRF
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


# Djoser
# class UserSerializers(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         fields = ["id", "username", "email", "password"]


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
