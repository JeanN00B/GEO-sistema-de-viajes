from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .forms import AddClientForm, ReadUpdateClientForm
from .models import Client


@login_required
def search_name(request):
    query = request.GET.get('q')
    if query:
        query_list = (item.capitalize() for item in query.split())
        clients = Client.objects.filter(
            Q(first_name__in=query_list) | 
            Q(second_name__in=query_list) |
            Q(last_name__in=query_list) |
            Q(sur_name__in=query_list))
    else:
        clients = Client.objects.all()
    print('django was here!')
    return render(request, 'clients/clients.html', {'clients': clients})


@login_required
def clients_visualize(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients.html', {
        'clients': clients
    })


@login_required #Open the form with a button, id_type is extracted from id_number
def clients_create(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            User = get_user_model()
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
        print('POST from read_update_client.html')
        form = ReadUpdateClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/clients/')
    elif request.method == 'GET':
        form = ReadUpdateClientForm(instance=client)
        return render(request, 'clients/read_update_client.html',
                        {'form': form, 'client': client})
    else:
        raise ValueError('Error! The request method is not valid')