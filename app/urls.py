from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core import views

router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)
router.register(r'director', views.DirectorViewSet)
router.register(r'cinema', views.CinemaViewSet)
router.register(r'movietime', views.MovieTimeViewSet)
router.register(r'movie', views.MovieViewSet)
router.register(r'session', views.SessionViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('genre-basic/', views.GenreView.as_view()),
    path('genre/<int:id>/', views.GenreView.as_view()),
    path('genre-apiview/', views.GenreList.as_view()),
    path('genre-apiview/<int:id>/', views.GenreDetail.as_view()),
    path('genre-generic/', views.GenreListGeneric.as_view()),
    path('genre-generic/<int:id>/', views.GenreDetailGeneric.as_view()),
    path('', include(router.urls))
]
