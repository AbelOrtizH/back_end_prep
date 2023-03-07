from django.shortcuts import render
from django.http import HttpResponse
from littleLemon.forms import *

# Create your views here.
# def home(request):
#     path = request.path
#     response = HttpResponse(f'Esto funiona y lo hace BIEN. {path}')
#     return response

# def menuitems(request, name):
#     items ={
#         'pasta': 'Fresh pastal',
#         'salad': 'onion, tomatoes, lemon',
#         'dessert': 'Made whith creme'
#     }
#     #code to access dic by passing a value 
#     description = items[name]
#     return HttpResponse(f'<h2>{name}</h2>  {description}')

def form_view(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "home.html", context)