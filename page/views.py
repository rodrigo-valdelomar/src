from django.shortcuts import render

from .forms import PomodoroForm
# Create your views here.

def pomodoro_create_view(request):
    # form = PomodoroForm(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context = {
    #     "form" : form
    # }

    # return render(request, "page/pomodoro_create.html", context)
    return render(request, "page/pomodoro_create.html")

# tomar los tiempos

# hacer correr el tiempo

# avisar que se cumplió el tiempo