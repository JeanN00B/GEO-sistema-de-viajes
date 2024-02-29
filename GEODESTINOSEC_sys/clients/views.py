from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddClientForm
from django.contrib.auth import get_user_model
from .models import Client

@login_required
def clients_visualize(request):
    clients = Client.objects.all()
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