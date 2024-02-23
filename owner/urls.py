from django.urls import path
from owner import views

app_name = 'owners'
urlpatterns = [
    path('estimated/<int:order_id>', views.make_order_estimated_time, name='estimated'),
]

