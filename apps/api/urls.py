from django.urls import path
from apps.api.views import AuthorAPIView
from .views import AuthorGenericAPIView
from django.urls import include
from .views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors_viewset', AuthorViewSet, basename='authors-viewset')

app_name = 'api'

urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author-detail'),
    path('authors_generic/', AuthorGenericAPIView.as_view(), name='author-generic-list'),
    path('authors_generic/<int:pk>/', AuthorGenericAPIView.as_view(), name='author-generic-detail'),
    path('', include(router.urls)),
]

