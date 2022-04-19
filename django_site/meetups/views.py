from django.shortcuts import render

# Create your views here.

def index(request):
    meetups =[
        { 'title': 'A first meetup', 
        'location': 'rundeperler', 
        'slug': 'a-first-meetup'},
        { 'title': 'A second meetup', 
        'location': 'rørperler', 
        'slug': 'a-second-meetup' },
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A first Meetup', 
        'description': 'This is the first test',
        }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })









    # fra https://www.youtube.com/watch?v=t7DrJqcUviA&list=RDCMUCSJbGtTlrDami-tDGPUV9-w&index=3