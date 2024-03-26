from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.db.models import Q
from cities_light.models import City
from .forms import AddClientForm, ReadUpdateClientForm, AddVisaForm, AddPassportForm
from .models import Client, Visa, Passport
from django.contrib import messages



# This is for the "Buscar cliente" bar in the main page in dashboard/clients/
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

# This sort the clients by name and last name and display in the main page chart
@login_required
def clients_visualize(request):
    clients = Client.objects.all().order_by(
        'first_name', 'second_name', 'last_name', 'sur_name')
    return render(request, 'clients/clients.html', {
        'clients': clients
    })

# Open the form with a button, id_type is extracted from id_number
# Called by form that register clients
@login_required 
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
            cache.set('cached_cities', City.objects.all(), 60*60*2) # Set Cities in cache for 2 hours every time the model is accessed
            return render(request, 'clients/new_client.html',
                    {'form': form})
    else:

        form = AddClientForm()
        return render(request, 'clients/new_client.html',
                    {'form': form})
    
# Call to the client data, then display in the form with tabs
# just to visualize unless the user wants to update the data
@login_required
def clients_read_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ReadUpdateClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/clients/')
    else:
         # Set Cities in cache for 2 hours every time the model is accessed
        form = ReadUpdateClientForm(instance=client)
    
    visas = Visa.objects.filter(visa_holder=client)
    passports = Passport.objects.filter(passport_holder=client)
    return render(request, 'clients/read_update_client.html',
                        {'form': form, 'client': client, 'visas': visas, 'passports': passports})

@login_required
def visa_create(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = AddVisaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visa created!')
            return HttpResponseRedirect(reverse('clients_read_update', args=[pk]))
        else:
            messages.error(request, 'Visa not created!')
    else:
        form = AddVisaForm(initial={'visa_holder': client.pk})
    return render(request, 'clients/visa_create.html',
                    {'form': form, 'client': client})

@login_required
def visa_delete(request, pk):
    visa = get_object_or_404(Visa, pk=pk)
    messages.success(request, f'Visa to {visa.visa_to_country }, Nro: {visa.visa_number} deleted!')
    visa.delete()
    return redirect('clients_read_update', visa.visa_holder.pk)

@login_required
def passport_create(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = AddPassportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Passport created!')
            return HttpResponseRedirect(reverse('clients_read_update', args=[pk]))
        else:
            messages.error(request, 'Passport not created!')
    else:
        form = AddPassportForm(initial={'passport_holder': client.pk})
    return render(request, 'clients/passport_create.html',
                    {'form': form, 'client': client})

@login_required
def passport_delete(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    messages.success(request, f'Passport from {passport.passport_issue_country }, Nro: {passport.passport_number} deleted!')
    passport.delete()
    return redirect('clients_read_update', passport.passport_holder.pk)
