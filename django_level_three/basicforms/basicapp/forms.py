from django import forms
from django.core import validators

#creating own validators
# def clean_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError('start with z')

class formName(forms.Form):
    # name=forms.CharField(validators=[clean_for_z])
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='enter email again')
    text=forms.CharField(widget=forms.Textarea)
    # for detecting hidden bots
    #botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('make sure email matches')
