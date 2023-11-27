from . import views
from django.urls import path
from .views import GoodsListView, NewGoodView, get_token


urlpatterns = [
    path('goods', GoodsListView.as_view(), name='goods_list'),
    path('new_good', NewGoodView.as_view(), name='new_good'),
    path('get_token', views.get_token, name='get_token'),
]