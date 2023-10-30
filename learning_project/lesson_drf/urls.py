from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_user, name='home'),
    path('log_user', views.login_user, name='home'),
    path('log_user/', views.login_user, name='home'),
    path('reg_user', views.new_user_reg, name='registration'),
    path('reg_user/', views.new_user_reg, name='registration'),
    path('notes', views.notes_page, name='notes'),
    path('notes/', views.notes_page, name='notes'),
    path('add_note', views.add_note, name='add_note'),
    path('add_note/', views.add_note, name='add_note'),
    path('logout', views.logout_page, name='logout'),
    path('logout/', views.logout_page, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)