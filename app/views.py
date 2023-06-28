from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def HTML_FORMS(request):
    if request.method == 'POST':
        UND=request.POST['un']
        PD=request.POST['pw']
        UOD=User.objects.get_or_create(Username=UND)[0]
        UOD.save()
        PWO=User.objects.get_or_create(Password=PD)[0]
        PWO.save()
        return HttpResponse('Insertions data is successfully...............')
    return render(request,'HTML_FORMS.html')