from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, DachaSerializer, DachaReviewSerializer, DachaReservationSerializer, \
    DachaAddressSerializer, DachaImageSerializer
from .models import Dacha, Category, DachaImage, DachaReview, DachaReservation, DachaAddress


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DachaViewSet(ModelViewSet):
    queryset = Dacha.objects.all()
    serializer_class = DachaSerializer


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