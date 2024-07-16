from django import forms

class CertificateSearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('ISO_9001_2008', 'ISO 9001:2008'),
        ('ISO_9001_2015', 'ISO 9001:2015'),
        ('ISO_9001_2015_ANNAB', 'ISO 9001:2015 ANNAB'),
        ('ISO_20000_1_2011', 'ISO 20000-1:2011'),
        ('ISO_20000_1_2018', 'ISO 20000-1:2018'),
        ('ISO_27001_2013', 'ISO 27001:2013'),
        ('ISO_27001_2022', 'ISO 27001:2022'),
    ]
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')
    certificate_id = forms.CharField(max_length=100, label='Certificate ID')
