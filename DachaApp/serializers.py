from rest_framework import serializers
from .models import Dacha, DachaReview, DachaReservation, Favorites, Category
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model


# class DachaImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DachaImage
#         fields = '__all__'


# class DachaAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DachaAddress
#         fields = '__all__'

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'is_staff']  # добавили is_staff


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({
            'user_id': self.user.id,
            'is_staff': self.user.is_staff,
        })

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DachaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaReview
        fields = '__all__'


class DachaReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaReservation
        fields = '__all__'


class DachaSerializer(serializers.ModelSerializer):
    reviews = DachaReviewSerializer(many=True, read_only=True)
    reservations = DachaReservationSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
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
