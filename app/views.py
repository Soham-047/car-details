from django.shortcuts import redirect, render
from .forms import CarForm
from django.http import HttpResponse
from .models import Car

def home(request):
    
    if request.method == 'POST':
        car_form = CarForm(request.POST)
        
        if car_form.is_valid():
            car_form.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid form data", status=400)
    else:
        car_form = CarForm()

    return render(request, 'app/home.html', {'car_form': car_form})

def about(request):
    search_query = request.GET.get('search', '')

    if search_query:
        cars = Car.objects.filter(car_company__icontains=search_query) | Car.objects.filter(car_name__icontains=search_query) | Car.objects.filter(car_desc__icontains=search_query)
    else:
        cars = Car.objects.all()
    search_query = ""
    return render(request, 'app/about.html', {'cars': cars})
