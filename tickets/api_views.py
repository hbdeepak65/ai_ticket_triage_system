from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ml_model.predict import predict_ticket, predict_category_urgency

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

@api_view(['POST'])
def predict_view(request):
    description = request.data.get("description")
    if not description:
        return Response({"error": "Description is required"}, status=400)
    
    category, urgency = predict_ticket(description)
    return Response({
        "predicted_category": category,
        "predicted_urgency": urgency
    })
