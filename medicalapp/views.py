from django.http import HttpResponse
from medical.settings import EMAIL_HOST_USER
from medical import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from medicalapp.forms import PatientInfoForm
from medicalapp.models import PatientInfo
# Create your views here.

def index(request):
    form=PatientInfoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/mail')
    else:
        form=PatientInfoForm()
    return render(request,"index.html",{'form':form})

def feedback(request):
    return render(request,"feedback.html")
def infoshow(request):
    patient=PatientInfo.objects.all()
    return render(request,"infoshow.html",{'patient':patient})
def destroy(request,id):
    patient=PatientInfo.objects.get(id=id)
    patient.delete()
    return redirect('/infoshow')
#doctorreport shows page//doctorpage.html
def doctorpage(request,id):
    patient=PatientInfo.objects.get(id=id)
    return render(request,"doctorpage.html",{'patient':patient})
def proceed(request,id):
    patient=PatientInfo.objects.get(id=id)
    form=PatientInfoForm(request.POST or None,instance=patient)
    if form.is_valid():
        form.save()
        return redirect('/infoshow')
    else:
        form=PatientInfoForm()
    return render(request,"doctorpage.html",{'patient':patient})
#pharmacy details show
def pharmacyshow(request):
    patient=PatientInfo.objects.all()
    return render(request,"pharmacyshow.html",{'patient':patient})
#index1-currently unused
def index1(request):
    return render(request,"index1.html")
def index0(request):
    form=PatientInfoForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect('/infoshow')
    else:
        form=PatientInfoForm()
    return render(request,"index0.html",{'form':form})
#pharmacy page views
def pharmacypage(request,id):
    patient=PatientInfo.objects.get(id=id)
    return render(request,"pharmacypage.html",{'patient':patient})


#prescription details
def prescription(request,id):
    patient=PatientInfo.objects.get(id=id)
    form=PatientInfoForm(request.POST or None,instance=patient)
    if form.is_valid():
        form.save()
        return redirect('/pharmacyshow')
    else:
        form=PatientInfoForm()
    return render(request,"pharmacypage.html",{'form':form})

#mail

def mail(request):
    form=PatientInfoForm()
    subject="Greetings"
    msg="congratulations for your success"
    #to="sonuyohannan@gmail.com"
    to=form.EmailField
    res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if(res==1):
        msg="Mail Sent Sucessfully"
    else:
        msg="mail could not send"
    return HttpResponse(msg)


#login and Log-out system for doctorvisit.com
