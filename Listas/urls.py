from django.urls import path
from .views.listas_view import ListasView

urlpatterns = [
    path('', ListasView.as_view(), name='listas'),
    path('<int:id>/', ListasView.as_view(), name='lista-detalle'),
]