from django import forms
from dataclasses import fields
from django.forms import ModelForm
from.models import *
from crispy_forms.helper import FormHelper


class LocationForm(ModelForm):
    # name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Site name'}), required=False)
    # zipcode = models.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zipcode'}), required=False)
    # city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Site city'}), required=False)
    # country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)
    # address = models.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}), required=False)
    # lat = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    # lng = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    # place_id = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    pass

    class Meta:
        model = Location
        fields = ('name', 'country','zipcode', 'city','address')