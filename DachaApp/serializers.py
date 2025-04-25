from rest_framework import serializers
from .models import Dacha, DachaImage, DachaReview, DachaReservation, Favorites
from djoser.serializers import TokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


class DachaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaImage
        fields = '__all__'


class DachaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaReview
        fields = '__all__'


class DachaReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaReservation
        fields = '__all__'


# class DachaAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DachaAddress
#         fields = '__all__'


class DachaSerializer(serializers.ModelSerializer):
    images = DachaImageSerializer(many=True, read_only=True)
    reviews = DachaReviewSerializer(many=True, read_only=True)
    reservations = DachaReservationSerializer(many=True, read_only=True)
    # address = DachaAddressSerializer(many=True, read_only=True)

    class Meta:
        model = Dacha
        fields = '__all__'
        read_only_fields = ('owner',)


class FavoritesSerializer(serializers.ModelSerializer):
    dacha = DachaSerializer(read_only=True)  # Вложенный сериализатор для полной информации
    dacha_id = serializers.PrimaryKeyRelatedField(
        queryset=Dacha.objects.all(),
        source='dacha',
        write_only=True
    )

    class Meta:
        model = Favorites
        fields = ['id', 'user', 'dacha', 'dacha_id', 'created_at']
        read_only_fields = ['user', 'created_at']
