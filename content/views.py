from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import FAQ, FavoriteItem, ContactMessage, Certificate, Project
from .serializers import FAQSerializer, FavoriteItemSerializer, ContactMessageSerializer, CertificateSerializer, ProjectSerializer

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

# -----------------------------
# CRUD de Certificate
# -----------------------------
class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descripcion', 'tipo']
    ordering_fields = ['anio', 'creado']
    ordering = ['-anio', '-creado']


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
