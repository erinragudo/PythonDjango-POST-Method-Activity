from django.shortcuts import render, redirect
from .forms import AppointmentForm

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can define where to redirect after saving the form
    else:
        form = AppointmentForm()
    
    return render(request, 'scheduling/appointment_form.html', {'form': form})
