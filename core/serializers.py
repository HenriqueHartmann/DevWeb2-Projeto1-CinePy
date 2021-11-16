from rest_framework.serializers import ModelSerializer, CharField, ListField, FloatField
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


class MovieDetailSerializer(ModelSerializer):
    director = CharField(source="director.name")
    genre = ListField(source="get_genre")

    class Meta:
        model = models.Movie
        fields = "__all__"
        depth = 1


# Session
class SessionSerializer(ModelSerializer):
    class Meta:
        model = models.Session
        fields = "__all__"


class SessionDetailSerializer(ModelSerializer):
    type = CharField(source="get_type")
    status = CharField(source="get_status")
    movieTime = CharField(source="movieTime.time")
    movie = CharField(source="movie.name")
    cinema = CharField(source="cinema.name")
    class Meta:
        model = models.Session
        fields = "__all__"


# Cart
class CartSerializer(ModelSerializer):
    total = FloatField(source="get_total")
    session = SessionDetailSerializer()

    class Meta:
        model = models.Cart
        fields = ("session", "quantity", "total")
        depth = 1


class CreateEditCartSerializer(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ("session", "quantity")


# Order
class OrderSerializer(ModelSerializer):
    user = CharField(source="user.email")
    status = CharField(source="get_status")
    items = CartSerializer(many=True)

    class Meta:
        model = models.Order
        fields = ("id", "status", "user", "items", "total")


class CreateEditOrderSerializer(ModelSerializer):
    items = CreateEditCartSerializer(many=True)
    class Meta:
        model = models.Order
        fields = ("user", "items")

    def create(self, validated_data):
        items = validated_data.pop("items")
        order = models.Order.objects.create(**validated_data)
        for item in items:
            models.Cart.objects.create(item=order, **item)
        order.save()
        return order

    def update(self, instance, validated_data):
        items = validated_data.pop("items")
        if items:
            instance.items.all().delete()
            for item in items:
                models.Cart.objects.create(item=instance, **item)
            instance.save()
            return instance
