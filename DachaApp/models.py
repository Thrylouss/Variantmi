from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dacha(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    single_bed_room_count = models.PositiveSmallIntegerField()
    double_bed_room_count = models.PositiveSmallIntegerField()
    enter_time = models.TimeField()
    exit_time = models.TimeField()
    room_count = models.PositiveSmallIntegerField()
    week_day_price = models.PositiveIntegerField()
    week_end_price = models.PositiveIntegerField()
    square_meter = models.PositiveIntegerField()

    alcohol = models.BooleanField(default=False)
    available_only_family = models.BooleanField(default=False)
    loudly_music = models.BooleanField(default=False)
    party = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)

    wifi = models.BooleanField(default=False)
    playstation_5 = models.BooleanField(default=False)
    playstation_4 = models.BooleanField(default=False)
    playstation_3 = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    billiards = models.BooleanField(default=False)
    table_tennis = models.BooleanField(default=False)
    football_field = models.BooleanField(default=False)
    karaoke = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    jacuzzi = models.BooleanField(default=False)
    turkish_bath = models.BooleanField(default=False)
    indoor_swimming_pool = models.BooleanField(default=False)
    outdoor_swimming_pool = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    VERIFIED_TYPES = [
        ('verified', 'Verified'),
        ('not_verified', 'Not Verified'),
        ('new', 'New'),
    ]

    is_verified = models.CharField(max_length=20, choices=VERIFIED_TYPES, default='new')

    def __str__(self):
        return self.name


class DachaImage(models.Model):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='dacha_images/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.dacha.name}"


class DachaReview(models.Model):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.dacha.name}"


class DachaReservation(models.Model):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name="reservations")
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.dacha.name}"


class DachaAddress(models.Model):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name="addresses")
    district = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Address for {self.dacha.name}"


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name='favorite_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'dacha')  # запрещает дублирование
