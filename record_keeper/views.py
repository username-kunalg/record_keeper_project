from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import RecordForm
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import JsonResponse
class RecordListView(View):
    """View for displaying a list of records."""

    def get(self, request):
        """Handles GET request to display records."""
        records = Record.objects.all()
        return render(request, 'tables.html', {'records': records})

class RecordCreateView(View):
    """View for creating a new record."""

    def get(self, request):
        """Handles GET request to display the record creation form."""

        form = RecordForm()
        activities = Activity.objects.all()  # Get all activities
        return render(request, 'forms.html', {'form': form, 'activities': activities})

    def post(self, request):
        """Handles POST request to create a new record."""

        form = RecordForm(request.POST)
        if form.is_valid():
            # Since 'activity' is a ForeignKey field, you need to extract the activity ID from the submitted form data
            activity_id = request.POST.get('activity')
            activity = Activity.objects.get(pk=activity_id)  # Retrieve the selected activity
            form.instance.activity = activity  # Assign the selected activity to the record instance
            form.save()
            return redirect('record_list')
        return render(request, 'forms.html', {'form': form})

class RecordUpdateView(View):
    """View for updating an existing record."""

    def get(self, request, pk):
        """Handles GET request to display the record update form."""

        record = get_object_or_404(Record, pk=pk)

        # Format the date in "yyyy-MM-dd" format
        record.date = record.date.strftime('%Y-%m-%d')

        form = RecordForm(instance=record)
        activities = Activity.objects.all()  # Get all activities
        return render(request, 'forms.html', {'form': form, 'activities': activities})

    def post(self, request, pk):
        """Handles POST request to update an existing record."""

        record = get_object_or_404(Record, pk=pk)
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            # Extract the activity ID from the submitted form data
            activity_id = request.POST.get('activity')
            activity = Activity.objects.get(pk=activity_id)  # Retrieve the selected activity
            form.instance.activity = activity  # Assign the selected activity to the record instance
            form.save()
            return redirect('record_list')
        return render(request, 'forms.html', {'form': form})

class RecordDeleteView(View):
    """View for deleting a record."""

    def get(self, request, pk):
        """Handles GET request to display the record deletion confirmation."""
        record = get_object_or_404(Record, pk=pk)
        return render(request, 'recorddelete.html', {'record': record})

    def post(self, request, pk):
        """Handles POST request to delete a record."""
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        return redirect('record_list')

    def delete(self, request, pk):
        """Handles DELETE request to delete a record."""
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        return JsonResponse({'message': 'Record deleted successfully'})

class IndexView(TemplateView):
    """View for displaying the index page."""
    template_name = 'index.html'

class SignupView(FormView):
    """View for user signup."""
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Handles form submission."""
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    """View for user login."""
    template_name = 'login2.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('record_list')

    def form_valid(self, form):
        """Handles form submission."""
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
        return super().form_valid(form)

class LogoutView(TemplateView):
    """View for user logout."""
    def get(self, request, *args, **kwargs):
        """Handles GET request to logout."""
        logout(request)
        return redirect('login')
