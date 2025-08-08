from django.urls import path
from . import views
from .api_views import TicketListCreateView, predict_view

urlpatterns = [
    path('submit/', views.submit_ticket, name='submit_ticket'),
    path('dashboard/', views.ticket_dashboard, name='ticket_dashboard'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('api/classify/', views.classify_ticket_api, name='classify_ticket_api'),
    path('', views.home, name='home'),
    path('api/tickets/', TicketListCreateView.as_view(), name='api_ticket_list_create'),
    path('api/predict/', predict_view, name='api_ticket_predict'),
]
