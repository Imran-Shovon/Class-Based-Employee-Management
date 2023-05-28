from django.urls import path

from . import views

urlpatterns = [
    # Create
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    # Read
    path('', views.EmployeeListView.as_view(), name='read'),
    # Update
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name='update'),
    # Delete
    path('delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='delete')



]
