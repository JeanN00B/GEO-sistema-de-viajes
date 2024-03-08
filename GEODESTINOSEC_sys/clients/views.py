from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddClientForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
from .forms import AddClientForm, ReadUpdateClientForm
from .models import Client, PROVINCES_CITIES_ECUADOR


@login_required
def search_name(request):
    query_string = request.GET.get('q')
    if query_string:
        query_list = query_string.split()
        queries = [Q(first_name__icontains=term) | 
                   Q(second_name__icontains=term) | 
                   Q(last_name__icontains=term) | 
                   Q(sur_name__icontains=term) for term in query_list]
        query = queries.pop() if queries else Q()
        for item in queries:
            query |= item
        clients = Client.objects.filter(query)
    else:
        clients = Client.objects.all()
    return render(request, 'clients/clients_search_result.html', {'clients': clients})

@login_required
def clients_visualize(request):
    clients = Client.objects.all().order_by(
        'first_name', 'second_name', 'last_name', 'sur_name')
    return render(request, 'clients/clients.html', {
        'clients': clients
    })

User = get_user_model()

@login_required
def clients_create(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.salesman_refer = User.objects.get(username=request.user.username).userprofile
            client.save()

            return redirect('/dashboard/clients/')
        else:
            return render(request, 'clients/new_client.html',
                    {'form': form})
    else:
        form = AddClientForm()
        return render(request, 'clients/new_client.html',
                    {'form': form})

@login_required
def clients_read_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ReadUpdateClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/clients/')
    else:
        form = ReadUpdateClientForm(instance=client)
    
    return render(request, 'clients/read_update_client.html',
                        {'form': form, 'client': client})