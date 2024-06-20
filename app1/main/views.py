from django.shortcuts import redirect, render
from django.http import HttpResponse
from users.models import User

def index(request):
    return render(request, 'main/index.html')

def profile_list(request):
    if request.user.is_authenticated:
        profiles = User.objects.exclude(username=request.user.username, first_name=request.user.first_name, image=request.user.image, last_name=request.user.last_name, id=request.user.id)
        return render(request, "main/profile_list.html", {"profiles": profiles})
    else:
        return redirect("index")
    
def places(request):
    return render(request, 'main/places.html')