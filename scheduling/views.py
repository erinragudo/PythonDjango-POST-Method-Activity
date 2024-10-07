from django.shortcuts import render, redirect
from .forms import AppointmentForm

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    context = {
            'form': form,
        }
    return render(request, 'scheduling/appointment_form.html', context)
