from .models import *
from django.contrib.auth.models import User

def user_role(request):
    is_student = False
    is_professor = False
    if request.user.is_authenticated:
        user = request.user
        if Student.objects.filter(user=user).exists():
            is_student=True
        else:
            is_professor = True

    return {
        'is_student': is_student,
        'is_professor': is_professor,
    }