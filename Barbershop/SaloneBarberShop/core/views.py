from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate , login , logout
from .models import Room , Message , Lecturer
from django.urls import reverse
import os
from django.contrib.auth.models import Group
# Create your views here.
from .decorates import *
class Signupclient(CreateView):
    model = User
    form_class = Signupclient
    template_name = 'signupstudent.html'

    def form_valid(self, form):
        user = form.save()
        student_group = Group.objects.get(name='student')
        student_group.user_set.add(user)
        return redirect('homepage')

class SignupAdmin(CreateView):
    model = User
    form_class = Signupadmin
    template_name = 'signupadmin.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('homepage')



def Loginclient(request):
    if request.method == "GET" :
        return render(request,'loginstudent.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('modelstudent')
        else:
            print("Make sure that your Username and password are correct")
            return redirect('loginstudent')



def loginadmin(request):
    if request.method == "GET":
        return render(request, 'loginadmin.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin/')
        else:
            print("Make sure that your Username and password are correct")
            return redirect('loginadmin')

def logout_user(request):
    logout(request)
    return redirect('loginstudent')


def homepage(request):
    return render(request , 'homepage.html')

def service(request):
    return render(request , 'service.html')


def booking(request):
    return render(request,'booking.html')




def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'bookings/booking.html', {'form': form})

def booking_success_view(request):
    return render(request, 'bookings/success.html')


@login_required
@limit_to_admin
def adminpage(request):
    return render(request, 'adminpage.html')





def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')



def search(request):
    query = request.GET.get('query', '').strip().lower()
    if not query:
        # No search query was entered
        return HttpResponse("You did not search for anything.")

    # Define a mapping of keywords to view names (URL names)
    search_mappings = {

    }


    for keyword, view_name in search_mappings.items():
        if query == keyword:

            return redirect(reverse(view_name))


    return HttpResponse(f"No results found for '{query}'.")









