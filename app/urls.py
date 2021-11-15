from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)
router.register(r'director', views.DirectorViewSet)
router.register(r'cinema', views.CinemaViewSet)
router.register(r'movietime', views.MovieTimeViewSet)
router.register(r'movie', views.MovieViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'cart', views.CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre-basic/', views.GenreView.as_view()),
    path('genre/<int:id>/', views.GenreView.as_view()),
    path('genre-apiview/', views.GenreList.as_view()),
    path('genre-apiview/<int:id>/', views.GenreDetail.as_view()),
    path('genre-generic/', views.GenreListGeneric.as_view()),
    path('genre-generic/<int:id>/', views.GenreDetailGeneric.as_view()),
    path('', include(router.urls))
]
