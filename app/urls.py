from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', views.GenreView.as_view()),
    path('genre/<int:id>/', views.GenreView.as_view()),
    path('genre-apiview/', views.GenreList.as_view()),
    path('genre-apiview/<int:id>/', views.GenreDetail.as_view()),
    path('genre-generic/', views.GenreListGeneric.as_view()),
    path('genre-generic/<int:id>/', views.GenreDetailGeneric.as_view()),
]
