from django.urls import path
from .views import (
    FAQListCreateView, FAQRetrieveUpdateDestroyView,
    FavoriteItemListCreateView, FavoriteItemRetrieveUpdateDestroyView,
    ContactMessageListCreateView, ContactMessageRetrieveUpdateDestroyView,
)

urlpatterns = [
    # FAQs
    path("faqs/", FAQListCreateView.as_view(), name="faq-list-create"),
    path("faqs/<int:pk>/", FAQRetrieveUpdateDestroyView.as_view(), name="faq-detail"),

    # Favorite Items
    path("favorite-items/", FavoriteItemListCreateView.as_view(), name="favoriteitem-list-create"),
    path("favorite-items/<int:pk>/", FavoriteItemRetrieveUpdateDestroyView.as_view(), name="favoriteitem-detail"),

    # Contact Messages
    path("contact/", ContactMessageListCreateView.as_view(), name="contactmessage-list-create"),
    path("contact/<int:pk>/", ContactMessageRetrieveUpdateDestroyView.as_view(), name="contactmessage-detail"),
]
