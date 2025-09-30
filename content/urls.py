from django.urls import path
from .views import FAQListView, FavoriteItemListCreateView, FavoriteItemRetrieveUpdateDestroyView, ContactMessageCreateView

urlpatterns = [
    path("faqs/", FAQListView.as_view(), name="faqs"),
    path("favorite-items/", FavoriteItemListCreateView.as_view(), name="favoriteitem-list-create"),
    path("favorite-items/<int:pk>/", FavoriteItemRetrieveUpdateDestroyView.as_view(), name="favoriteitem-detail"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-message"),
]
