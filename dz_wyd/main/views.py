from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm  # Assuming you'll create a form

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST) #using forms is better practice
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to a list view or another appropriate page
    else:
        form = UserForm()  # Create an empty form

    return render(request, 'add_user.html', {'form': form})

def user_list(request):
    users = User.objects.all()  # Retrieve all User objects from the database
    return render(request, 'user_list.html', {'users': users})