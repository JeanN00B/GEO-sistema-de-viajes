from django.shortcuts import render, redirect, get_object_or_404
from .filter_form import ClientFilter
from clients.models import Client
from .models import FilterAsJSON
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json
from urllib.parse import quote
from django.contrib import messages
from django.urls import reverse


def analytics_index(request):
    return render(request, 'analytics/analytics_index.html',
                    {'clients': Client.objects.all(),
                     'filters': FilterAsJSON.objects.all()})


def analytics_filter(request):
    if request.method == 'GET':
        f = ClientFilter(request.GET, queryset=Client.objects.all())
        return render(request, 'analytics/filter_form.html',
                    {'filter': f})
    else:
        print('POST?????')
        return render(request, 'analytics/filter_form.html')

@login_required
def analytics_filter_save(request):
    if request.method == 'POST':
        json_content = json.loads(request.POST['json_content'])
        data = {
            'name': request.POST['name'],
            'description': request.POST['description'],
            'json_content': json_content
        }
        custom_query = FilterAsJSON(**data)
        try:
            custom_query.full_clean()
            custom_query.save()
            # return render(request, 'analytics/filter_form.html')
            # return HttpResponseRedirect('analytics')
            return redirect('analytics')
        except Exception as e:
            messages.error(request, f'Error: {e}')
    else:
        print('GET????')
        return redirect('analytics')
    

@login_required
def analytics_filter_update(request, pk):
    filter = FilterAsJSON.objects.get(pk=quote(pk))
    f = ClientFilter(request.GET, queryset=Client.objects.all())
    f.form.data = filter.json_content
    return render(request, 'analytics/filter_form.html')


@login_required
def analytics_filter_delete(request, pk):
    filter = get_object_or_404(FilterAsJSON, pk=pk)
    messages.success(request, f'Filter {filter.name} deleted!')
    filter.delete()
    return redirect('analytics')