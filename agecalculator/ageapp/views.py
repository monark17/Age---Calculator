from django.shortcuts import render
from .forms import AgeForm
from datetime import date

# Create your views here.

def age_calculator(request):
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            birthdate = form.cleaned_data['birthdate']
            today = date.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return render(request, 'ageapp/result.html', {'age': age})
    else:
        form = AgeForm()

    return render(request, 'ageapp/age_calculator.html', {'form': form})
