from django.shortcuts import render, redirect
from .forms import AppointmentForm

def create_appointment(request):
    form = AppointmentForm()
    context = {
            'form': form,
        }
    return render(request, 'scheduling/appointment_form.html', {'form': form})
