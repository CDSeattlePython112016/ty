from django.shortcuts import render

def index(request):
    return render(request, 'd_ninja/index.html')

def ninjas(request):
    return render(request, 'd_ninja/turtles.html')

def color(request, color):
    context = {'color': color}
    return redirect(request, 'd_ninja/')
