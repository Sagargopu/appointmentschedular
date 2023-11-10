from django.urls import path
from . import views

urlpatterns = [
    path('departments/',views.departments,name='departments'),
    path('professors/',views.Professors,name='professors'),
    path('login/',views.LoginUser,name='login'),
    path('logout/',views.LogoutUser,name='logout'),
    path('signup/',views.SignUp,name='signup'),
    path('officehours/',views.ViewOfficeHours,name='officehours'),
    path('myschedule/',views.MySchedule,name='myschedule'),
    path('myappointments/',views.MyAppointments,name='myappointments'),
    path('addappointments/',views.Refresh,name='addappointments'),
    path('addofficehours/',views.AddOfficeHours,name='addofficehours'),
    path('deleteofficehours/<str:id>',views.DeleteOfficeHours,name='deleteofficehours'),
    path('updateprofile/',views.updateProfile,name='updateprofile'),
    
]