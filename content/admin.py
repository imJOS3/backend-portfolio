from django.contrib import admin
from .models import FAQ, FavoriteItem, ContactMessage
from .models import ContactMessage

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "published")
    list_editable = ("order", "published")


# Registrar FavoriteItem en el admin
@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "año_lanzamiento")
    search_fields = ("titulo", "tipo", "palabras_clave")


# Registrar ContactMessage en el admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
