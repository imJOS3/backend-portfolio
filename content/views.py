from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FAQ, FavoriteItem, ContactMessage
from .serializers import FAQSerializer, FavoriteItemSerializer, ContactMessageSerializer

# -----------------------------
# CRUD de FAQs
# -----------------------------
class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all().order_by("order")
    serializer_class = FAQSerializer

class FAQRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# -----------------------------
# CRUD de FavoriteItem
# -----------------------------
class FavoriteItemListCreateView(generics.ListCreateAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

class FavoriteItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer


# -----------------------------
# CRUD de ContactMessage
# -----------------------------
class ContactMessageListCreateView(generics.ListCreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class ContactMessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
