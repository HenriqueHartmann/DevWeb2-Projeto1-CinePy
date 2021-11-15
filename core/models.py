from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateField()
    synopsis = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name="movies")
    genre = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        release = str(self.releaseDate).split('-')[0]
        return "%s (%s)" % (self.name, release)

    @property
    def get_genre(self):
        genre_list = []
        for i in self.genre.all():
            genre_list.append(i.name)
        return genre_list

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class MovieTime(models.Model):
    time = models.TimeField(unique=True)

    def __str__(self):
        time = str(self.time).split(":")
        del time[2]
        time = ':'.join(map(str, time))
        return "%s" % (time)


class Session(models.Model):
    DUB_TYPE = 0
    SUB_TYPE = 1
    TYPE_CHOICES = (
        (DUB_TYPE, 'Dubbed'),
        (SUB_TYPE, 'Subtitled')
    )

    OPEN_STATUS = 0
    CLOSE_STATUS = 1
    STATUS_CHOICES = (
        (OPEN_STATUS, 'Open'),
        (CLOSE_STATUS, 'Closed')
    )

    type = models.IntegerField(default=DUB_TYPE, choices=TYPE_CHOICES)
    status = models.IntegerField(default=OPEN_STATUS, choices=STATUS_CHOICES)
    price = models.FloatField()
    movieTime = models.ForeignKey(MovieTime, on_delete=models.PROTECT, related_name="screenings")
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="screenings")
    cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT, related_name="screenings")

    def __str__(self):
        return "%s - %s - %s" % (self.movieTime, self.movie, self.cinema)

    @property
    def get_type(self):
        return self.get_type_display()

    @property
    def get_status(self):
        return self.get_status_display()


class Order(models.Model):

    class OrderStatus(models.IntegerChoices):
        CART = 1, 'Cart'
        SHOPPED = 2, 'Shopped'
        PAID = 3, 'Paid'
        WITHDRAWN = 4, 'Withdrawn'

    status = models.IntegerField(default=OrderStatus.CART, choices=OrderStatus.choices)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")

    @property
    def get_status(self):
        return self.get_status_display()

    @property
    def total(self):
        queryset = self.items.all().aggregate(total=models.Sum(F('quantity')*F('session__price')))
        return queryset["total"]

class Cart(models.Model):
    quantity = models.IntegerField()
    item = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    session = models.ForeignKey(Session, on_delete=models.PROTECT, related_name="+")

    @property
    def get_total(self):
        return self.session.price * self.quantity
