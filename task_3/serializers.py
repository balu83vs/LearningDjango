from rest_framework import serializers
from .models import Users, Goods, Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            "id",
            "key",
            "username",
            "is_valid",
        ]


class UserSerializer(serializers.ModelSerializer):
    token = TokenSerializer()
    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "token",
        ]


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = [
            "id",
            "name",
            "amount",
            "price",
        ]