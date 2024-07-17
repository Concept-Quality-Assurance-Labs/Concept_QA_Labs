from django.shortcuts import render, redirect
from .models import Update1, Update2, Update3
from django.conf import settings
import os
from .forms import CertificateSearchForm

# Create your views here.

def index(request):
    return render(request, 'cqal/index.html')

def Knowmore(request):
    return render(request, 'cqal/knowmore.html')

def cmmi(request):
    return render(request, 'cqal/cmmi.html')

def faq(request):
    return render(request, 'cqal/faq.html')

def training(request):
    return render(request, 'cqal/training.html')

def iso(request):
    return render(request, 'cqal/iso.html')

def ai(request):
    return render(request, 'cqal/ai.html')

def metrics(request):
    return render(request, 'cqal/metrics.html')

def Appraisals(request):
    return render(request, 'cqal/process appraisals.html')

def iso9001(request):
    return render(request, 'cqal/iso9001.html')

def iso27001(request):
    return render(request, 'cqal/iso27001.html')

def iso20000(request):
    return render(request, 'cqal/iso20000.html')
    
def Accrediatations(request):
    return render(request, 'cqal/accrediatations.html')
    
def update_1(request):
    update1 = Update1.objects.all()
    context = {'info1': update1}
    return render(request, 'cqal/update1.html', context)
    
def update_2(request):
    update2 = Update2.objects.all()
    context = {'info2': update2}
    return render(request, 'cqal/update2.html', context)

def update_3(request):
    update3 = Update3.objects.all()
    context = {'info3': update3}
    return render(request, 'cqal/update3.html', context)


def directory(request):
    form = CertificateSearchForm()
    certificate_image = None
    error_message = None  # Add an error message variable
    
    if request.method == 'POST':
        form = CertificateSearchForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            certificate_id = form.cleaned_data['certificate_id']
            folder_name = category
            certificate_path = os.path.join(settings.MEDIA_ROOT, folder_name, f"{certificate_id}.jpg")

            if os.path.exists(certificate_path):
                certificate_image = os.path.join(settings.MEDIA_URL, folder_name, f"{certificate_id}.jpg")
            else:
                error_message = 'Certificate not found. Please contact info@conceptqalabs.com'

    return render(request, 'cqal/directory.html', {'form': form, 'certificate_image': certificate_image, 'error_message': error_message})

    
    