from django import forms
from .models import Department


class FilterForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="All Departments", required=False)