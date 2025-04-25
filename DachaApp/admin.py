from django.contrib import admin
from .models import Dacha, DachaImage, DachaReview, DachaReservation, Favorites

# Register your models here.
admin.site.register([Dacha, DachaImage, DachaReview, DachaReservation, Favorites])
