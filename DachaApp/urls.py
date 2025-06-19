from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from . import views
from .views import CustomTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="Dacha API",
        default_version="v1",
        description="Example API",
    ),
    public=True,
    permission_classes=([permissions.AllowAny,]),
)

router = DefaultRouter()
router.register('dacha', views.DachaViewSet)
router.register('dacha_review', views.DachaReviewViewSet)
router.register('dacha_reservation', views.DachaReservationViewSet)
router.register('favorites', views.FavoriteViewSet)
router.register('category', views.CategoryViewSet)
# router.register('dacha_image', views.DachaImageViewSet)
# router.register('dacha_address', views.DachaAddressViewSet)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    path('auth/jwt/create/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),


    path('', include(router.urls)),
]
