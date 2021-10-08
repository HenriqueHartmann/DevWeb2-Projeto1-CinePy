from django.contrib import admin

from core.models import Director, Genre, Movie, Cinema, MovieTime, Session, Order, Cart


admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(MovieTime)
admin.site.register(Session)


class CartItemsInline(admin.TabularInline):
    model = Cart

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (CartItemsInline,)
