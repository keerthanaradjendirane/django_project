from django.shortcuts import render, redirect
from .forms import MyForm  # Import your form
from .models import MyModel  # Import your model

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new record to the database
            return redirect('home')  # Redirect to the same page to avoid resubmission
    else:
        form = MyForm()
    
    data = MyModel.objects.all()  # Fetch all records from your model
    return render(request, 'home.html', {'form': form, 'data': data})
