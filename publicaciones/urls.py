from django.urls import path
from .views import DeletePublicacion


urlpatterns = [
    path('remover/<str:tipo>/<int:pk>/', DeletePublicacion.as_view(), name='delete-publicacion'),
]
