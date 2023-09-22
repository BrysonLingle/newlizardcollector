from django.shortcuts import render


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
    return render(request, 'all_lizards_html')

def all_lizards(request):
    return render(request,'lizard.html',{'lizard': lizard_data})

def home(request):
   return render(request, 'home.html')  


def lizards_index(request):
    
    return render(request, 'lizards/index.html', {'lizards': lizards})




