from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('home', views.indexpage, name='index'),
    path('home/', views.indexpage, name='index'),
    path('words_list', views.word_listpage, name='words_list'),
    path('words_list/', views.word_listpage, name='words_list'),
    path('add_word', views.add_wordpage, name='add_word'),
    path('add_word/', views.add_wordpage, name='add_word')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
