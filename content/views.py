from rest_framework import generics


from .models import FAQ, FavoriteItem, ContactMessage
from .serializers import FAQSerializer, FavoriteItemSerializer, ContactMessageSerializer

# Lista de FAQs
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.filter(published=True).order_by("order")
    serializer_class = FAQSerializer


# CRUD para FavoriteItem
class FavoriteItemListCreateView(generics.ListCreateAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

class FavoriteItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer


# Vista para crear mensajes de contacto
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ContactMessageCreateView(APIView):
    def post(self, request, format=None):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Mensaje enviado correctamente."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
