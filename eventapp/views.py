from django.shortcuts import render

from .models import Participant

# Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapp/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.username = request.POST.get('username','_')
        p1.phone = request.POST.get('phone','000')
        p1.email = request.POST.get('email','_')
        p1.institution = request.POST.get('institution','_')

        if len(Participant.objects.all()) > 10:
            return render(request, 'eventapp/failed.html', context)
        else:
            p1.save()
            return render(request, 'eventapp/success.html', context)
    
    if request.method =='GET':
        context['username'] = ''
        context['phone'] = ''
        context['email'] = ''
        context['institution'] = ''
    return render(request, 'eventapp/register.html', context)

def participants(request):
    context = {}

    context["participants"] = Participant.objects.all();
    return render(request, 'eventapp/participants.html', context)

def failed(request):
    context = {}
    return render(request, 'eventapp/failed.html', context)

def success(request):
    context = {}
    return render(request, 'eventapp/success.html', context)

