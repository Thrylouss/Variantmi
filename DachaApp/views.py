from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, DachaSerializer, DachaReviewSerializer, DachaReservationSerializer, \
    DachaAddressSerializer, DachaImageSerializer, FavoritesSerializer
from .models import Dacha, Category, DachaImage, DachaReview, DachaReservation, DachaAddress, Favorites


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DachaViewSet(ModelViewSet):
    queryset = Dacha.objects.all()
    serializer_class = DachaSerializer

    @action(detail=False, methods=['get'])
    def my_dachas(self, request):
        user = request.user
        dachas = Dacha.objects.filter(owner=user)
        serializer = self.get_serializer(dachas, many=True)
        return Response(serializer.data)


class DachaReviewViewSet(ModelViewSet):
    queryset = DachaReview.objects.all()
    serializer_class = DachaReviewSerializer


class DachaReservationViewSet(ModelViewSet):
    queryset = DachaReservation.objects.all()
    serializer_class = DachaReservationSerializer


class DachaAddressViewSet(ModelViewSet):
    queryset = DachaAddress.objects.all()
    serializer_class = DachaAddressSerializer


class DachaImageViewSet(ModelViewSet):
    queryset = DachaImage.objects.all()
    serializer_class = DachaImageSerializer


class FavoriteViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='add/(?P<pk>[^/.]+)')
    def add_to_favorites(self, request, pk=None):
        user = request.user

        # Проверка существования дачи
        try:
            dacha = Dacha.objects.get(pk=pk)
        except Dacha.DoesNotExist:
            return Response({"detail": "Dacha not found."}, status=status.HTTP_404_NOT_FOUND)

        # Проверка на уже добавленную дачу
        favorite, created = Favorites.objects.get_or_create(user=user, dacha=dacha)

        if not created:
            return Response({"detail": "Dacha already in favorites."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Favorites.objects.filter(user=user)
        else:
            # Возвращаем пустой queryset, если пользователь не авторизован
            return Favorites.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
