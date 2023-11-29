from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.Students,name='students'),
    path('profile/',views.Profile,name='profile'),
    path('viewappointments/<str:pk>/',views.ViewAppointments,name='viewappointments'),
    path('confirmacard/<str:id>/',views.ConfirmCard,name='confirmcard'),
    path('cancelcard/<str:id>/',views.CancelCard,name='cancelcard'),
    path('bookappointment/<str:pk>/',views.BookAppointment,name='bookappointment'),
    path('cancelappointment/<str:pk>/',views.CancelAppointment,name='cancelappointment'),
]
