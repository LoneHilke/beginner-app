from django.shortcuts import render

# Create your views here.

def index(request):
    meetups =[
        { 'title': 'A first meetup', 
        'location': 'rundeperler', 
        'slug': 'første ide'},
        { 'title': 'A second meetup', 
        'location': 'rørperler', 
        'slug': 'nye måder ide' },
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })








    # fra https://www.youtube.com/watch?v=t7DrJqcUviA&list=RDCMUCSJbGtTlrDami-tDGPUV9-w&index=3