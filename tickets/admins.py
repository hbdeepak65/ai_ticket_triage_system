from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'urgency', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'urgency', 'category')
