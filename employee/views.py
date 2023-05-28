from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from employee.models import Employee
from django.urls import reverse_lazy

# Create


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read')

# Read


class EmployeeListView(ListView):
    model = Employee
    queryset = Employee.objects.all()

# Update


class EmployeeUpdateView(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read')

# Delete


class EmployeeDeleteView(DeleteView):
    queryset = Employee.objects.all()
    success_url = reverse_lazy('read')
