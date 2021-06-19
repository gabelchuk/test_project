from django import forms
from myapp.models import Citi, Language


class FindForm(forms.Form):
    citi = forms.ModelChoiceField(queryset=Citi.objects.all(),
                                  to_field_name = 'slug', required = False,
                        widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Місто')
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                  to_field_name = 'slug', required = False,
                        widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Вакансія')
