from django.shortcuts import render, redirect
from .models import Update1, Update2, Update3
from django.conf import settings
import os
from .forms import CertificateSearchForm

# Create your views here.


# Define the index view function
def index(request):
    """
    Handles the request for the index page and renders the 'cqal/index.html' template.
    """
    return render(request, 'cqal/index.html')


# Define the Knowmore view function
def Knowmore(request):
    """
    Handles the request for the Knowmore page and renders the 'cqal/knowmore.html' template.
    """
    return render(request, 'cqal/knowmore.html')


def cmmi(request):
    """Render the 'cqal/cmmi.html' template."""
    return render(request, 'cqal/cmmi.html')


def faq(request):
    """Render the 'cqal/faq.html' template."""
    return render(request, 'cqal/faq.html')


def training(request):
    """Render the 'cqal/training.html' template."""
    return render(request, 'cqal/training.html')


def iso(request):
    """Render the 'cqal/iso.html' template."""
    return render(request, 'cqal/iso.html')


def ai(request):
    """Render the 'cqal/ai.html' template."""
    return render(request, 'cqal/ai.html')


def metrics(request):
    """Render the 'cqal/metrics.html' template."""
    return render(request, 'cqal/metrics.html')


def Appraisals(request):
    """Render the 'cqal/process appraisals.html' template."""
    return render(request, 'cqal/process appraisals.html')


def iso9001(request):
    """Render the 'cqal/iso9001.html' template."""
    return render(request, 'cqal/iso9001.html')


def iso27001(request):
    """Render the 'cqal/iso27001.html' template."""
    return render(request, 'cqal/iso27001.html')


def iso20000(request):
    """Render the 'cqal/iso20000.html' template."""
    return render(request, 'cqal/iso20000.html')


def iso14001(request):
    """Render the 'cqal/iso14001.html' template."""
    return render(request, 'cqal/iso14001.html')


def Accrediatations(request):
    """Render the 'cqal/accrediatations.html' template."""
    return render(request, 'cqal/accrediatations.html')


def update_1(request):
    """Render the 'cqal/update1.html' template with update1 data."""
    update1 = Update1.objects.all()
    context = {'info1': update1}
    return render(request, 'cqal/update1.html', context)


def update_2(request):
    """Render the 'cqal/update2.html' template with update2 data."""
    update2 = Update2.objects.all()
    context = {'info2': update2}
    return render(request, 'cqal/update2.html', context)


def update_3(request):
    """Render the 'cqal/update3.html' template with update3 data."""
    update3 = Update3.objects.all()
    context = {'info3': update3}
    return render(request, 'cqal/update3.html', context)


def directory(request):
    """
    Handle certificate search and render 'cqal/directory.html'.
    """
    # Initialize the search form
    form = CertificateSearchForm()
    
    # Initialize variables for certificate image and error message
    certificate_image = None
    error_message = None
    
    # Process POST requests
    if request.method == 'POST':
        # Re-initialize form with POST data
        form = CertificateSearchForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Extract category and certificate ID from the form
            category = form.cleaned_data['category']
            certificate_id = form.cleaned_data['certificate_id']
            
            # Construct the path to the certificate image
            folder_name = category
            certificate_path = os.path.join(settings.MEDIA_ROOT, folder_name, f"{certificate_id}.jpg")

            # Check if the certificate image file exists
            if os.path.exists(certificate_path):
                # Construct the URL for the certificate image
                certificate_image = os.path.join(settings.MEDIA_URL, folder_name, f"{certificate_id}.jpg")
            else:
                # Set error message if certificate is not found
                error_message = 'Certificate not found. Please contact info@conceptqalabs.com'

    # Render the 'cqal/directory.html' template with the form, image, and error message
    return render(request, 'cqal/directory.html', {'form': form, 'certificate_image': certificate_image, 'error_message': error_message})