from django.urls import path
from Reviews.views.reviews_view import ReviewsView

urlpatterns = [
    path("", ReviewsView.as_view(), name='reviews'),
]