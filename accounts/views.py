from django.shortcuts import render, HttpResponse

def home(request):
    numbers = {1,2,3,4,5}
    name = 'Max'

    args = {'myName': name}
    return render(request, 'accounts/login.html', args)


