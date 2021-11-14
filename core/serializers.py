from rest_framework.serializers import ModelSerializer
from core import models


# Genre
class GenreSerializer(ModelSerializer):
    class Meta:
        model = models.Genre
        fields = "__all__"


# Director
class DirectorSerializer(ModelSerializer):
    class Meta:
        model = models.Director
        fields = "__all__"


# Cinema
class CinemaSerializer(ModelSerializer):
    class Meta:
        model = models.Cinema
        fields = "__all__"


# MovieTime
class MovieTimeSerializer(ModelSerializer):
    class Meta:
        model = models.MovieTime
        fields = "__all__"


# Movie
class MovieSerializer(ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"
