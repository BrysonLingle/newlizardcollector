from django.shortcuts import render
from .models import Lizard
from django .views.generic.edit import CreateView
# lizard_data = [
#     {
#         'name': 'Green Anole',
#         'color': 'Green',
#         'size': 'Small',
#         'description': 'The green anole is a small lizard found in the southeastern United States.'
#     },
#     {
#         'name': 'Bearded Dragon',
#         'color': 'Various',
#         'size': 'Medium',
#         'description': 'Bearded dragons are popular pet lizards known for their beard-like scales.'
#     },
   
# ]

def about(request):
    return render(request, 'about.html')

def all_lizards(request):
    # lizard_data = Lizard.objects.all()
    lizards = Lizard.objects.all()
    return render(request, 'lizards/index.html', {'lizards': lizards})


def home(request):
   return render(request, 'home.html')  

def lizards_detail(request, lizard_id):
    lizard = Lizard.objects.get(id=lizard_id)
    return render(request, 'lizards/detail.html', {'lizard': lizard})


# def lizards_index(request):
    
#     return render(request, 'lizards/index.html', {'lizards': lizards})

class LizardCreate(CreateView):
    model = Lizard 
    fields = 


