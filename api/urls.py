from django.urls import path, include
from note.views import NoteViewSet
from rest_framework.routers import DefaultRouter
from api.views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from api.views import ProtectedView
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)

router = DefaultRouter()

router.register('notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('test/', ProtectedView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
]