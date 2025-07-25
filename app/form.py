from django.shortcuts import render, redirect
from django import forms
from .models import Std

class Stdform(forms.ModelForm):
    class Meta:
        model = Std
        fields = ['name', 'roll', 'address', 'mail']  # Ensure 'address' is listed
