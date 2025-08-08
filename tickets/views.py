from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .ml_model.predict import predict_category_urgency
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to AI Ticket Triage System</h1>")

@login_required
def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user

            # AI prediction
            cat, urg = predict_category_urgency(ticket.title + " " + ticket.description)
            ticket.category = cat
            ticket.urgency = urg
            ticket.save()
            return redirect('ticket_dashboard')
    else:
        form = TicketForm()
    return render(request, 'tickets/submit_ticket.html', {'form': form})

@login_required
def ticket_dashboard(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tickets/dashboard.html', {'tickets': tickets})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

def classify_ticket_api(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        category, urgency = predict_category_urgency(text)
        return JsonResponse({'category': category, 'urgency': urgency})
    return JsonResponse({'error': 'Invalid request'}, status=400)
