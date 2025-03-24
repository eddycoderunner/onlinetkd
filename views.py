from django.shortcuts import render, redirect
from .forms import CompetitorRegistrationForm

def register_competitor(request):
    if request.method == "POST":
        form = CompetitorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = CompetitorRegistrationForm()

    return render(request, 'register.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')