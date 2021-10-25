from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', views.GenreView.as_view()),
    path('genre/<int:id>', views.GenreView.as_view()),
]
