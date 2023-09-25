from django.shortcuts import render
from .models import Lizard

lizard_data = [
    {
        'name': 'Green Anole',
        'color': 'Green',
        'size': 'Small',
        'description': 'The green anole is a small lizard found in the southeastern United States.'
    },
    {
        'name': 'Bearded Dragon',
        'color': 'Various',
        'size': 'Medium',
        'description': 'Bearded dragons are popular pet lizards known for their beard-like scales.'
    },
   
]

def about(request):
    return render(request, 'about.html')

def all_lizards(request):
    # lizard_data = Lizard.objects.all()
    return render(request, 'all_lizard.html', {'lizard_data': lizard_data})


def home(request):
   return render(request, 'home.html')  


# def lizards_index(request):
    
#     return render(request, 'lizards/index.html', {'lizards': lizards})




