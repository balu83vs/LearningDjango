from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page, name='login'),
    path('login', views.login_page, name='login'),
    path('login/', views.login_page, name='login'),
    path('reg', views.add_user, name='reg'),
    path('reg/', views.add_user, name='reg'),
    path('notes', views.notespage, name='notes'),
    path('notes/', views.notespage, name='notes'),
    path('add_note', views.add_notepage, name='add_note'),
    path('add_note/', views.add_notepage, name='add_note'),
    path('logout', views.logoutpage, name='logout'),
    path('logout/', views.logoutpage, name='logout')

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)