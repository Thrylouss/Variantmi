from django.contrib import admin
from .models import Category, Dacha, DachaImage, DachaReview, DachaReservation, DachaAddress

# Register your models here.
admin.site.register([Category, Dacha, DachaImage, DachaReview, DachaReservation, DachaAddress])
