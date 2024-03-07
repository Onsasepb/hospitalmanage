from django.shortcuts import render,redirect
from yummyapp.models import User, Login


# Create your views here.
def index(request):
        return render(request, 'index.html')


def innerpage(request):
    return render(request, 'sample-inner-page.html')

def register(request):
    if request.method == 'POST':
        user = User(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        user.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        if Login.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            login = Login.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request, 'index.html', {'login':login})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
