from django.contrib import admin
from .models import Dacha, DachaReview, DachaReservation, Favorites, Category

# Register your models here.
admin.site.register([Dacha, Category, DachaReview, DachaReservation, Favorites])
