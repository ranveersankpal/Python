# user_validation/views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
        else:
            return render(request, 'user_validation/user_profile.html', {'form': form})

    form = UserProfileForm()
    return render(request, 'user_validation/user_profile.html', {'form': form})

def success_view(request):
    return render(request, 'user_validation/success.html')
