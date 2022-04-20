from django.shortcuts import render
from .models import Meetup
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description,
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })









    # fra https://www.youtube.com/watch?v=t7DrJqcUviA&list=RDCMUCSJbGtTlrDami-tDGPUV9-w&index=3
    # kommet til 1:30:19