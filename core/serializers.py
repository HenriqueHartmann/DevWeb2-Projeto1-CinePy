from rest_framework.serializers import ModelSerializer, CharField, ListField, IntegerField,EmailField, Serializer
from core import models


# User
class UserSerializer(Serializer):
    id = IntegerField()
    username = CharField()
    email = EmailField()
    first_name = CharField()
    last_name = CharField()


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


class MovieDetailSerializer(ModelSerializer):
    director = CharField(source="director.name")
    genre = ListField(source="get_genre")

    class Meta:
        model = models.Movie
        fields = "__all__"
        depth = 1


# Order
class OrderSerializer(ModelSerializer):
    user = UserSerializer()
    status = CharField(source="get_status")

    class Meta:
        model = models.Order
        fields = "__all__"
