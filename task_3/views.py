import uuid

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Token, Goods, Users
from .serializers import TokenSerializer, GoodsSerializer

import sqlite3


#  функция определения максимального id пользователя
def is_max_id():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(id) FROM task_3_users")

    max_id = cursor.fetchone()[0]

    conn.close()
    return max_id


@api_view(["GET"])
def get_token(request):
    # Генерация уникального токена
    unique_token = str(uuid.uuid4())

    # Проверка на уникальность токена
    while Token.objects.filter(key=unique_token).exists():
        unique_token = str(uuid.uuid4())

    # Создание нового пользователя по запросу
    id_users = is_max_id()
    if not id_users:
        id_users = 0
    user = Users.objects.create(username="user" + f"{id_users+1}")

    # Сохранение токена в базе данных
    token_obj = Token.objects.create(username=user, key=unique_token)

    # Возврат токена в формате JSON
    serializer = TokenSerializer(token_obj)
    return Response(serializer.data, status=status.HTTP_200_OK)


class GoodsListView(APIView):
    def get(self, request):
        token = request.query_params.get("token", None)
        if not token:
            return Response(
                "Token must be present", status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            token_obj = Token.objects.get(key=token)
            if not token_obj.is_valid:
                return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)
        except Token.DoesNotExist:
            return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)

        if type(self) is GoodsListView:
            # Сериализуем список всех продуктов
            products = Goods.objects.all()
            serializer = GoodsSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_200_OK)


class NewGoodView(GoodsListView):
    def post(self, request):
        token = request.query_params.get("token", None)
        if not token:
            return Response(
                "Token must be present", status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            token_obj = Token.objects.get(key=token)
            if not token_obj.is_valid:
                return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)
        except Token.DoesNotExist:
            return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)

        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            price = serializer.validated_data.get("price")
            amount = serializer.validated_data.get("amount")

            if price <= 0:
                return Response(
                    "Price must be more than 0", status=status.HTTP_400_BAD_REQUEST
                )
            if amount <= 0:
                return Response(
                    "Amount must be more than 0", status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)