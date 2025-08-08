from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tickets.api_views import TicketListCreateView, predict_view
from tickets import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),   # API endpoints for tickets
    path('api/users/', include('users.urls')),
    path('', views.ticket_dashboard, name='home'),
    path('api/tickets/', TicketListCreateView.as_view(), name='api_ticket_list_create'),
    path('api/predict/', predict_view, name='api_ticket_predict'),
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)