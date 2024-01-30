from django import forms

from django.core import validators


def validate_for_a(value):
    a = value.lower()
    if a[0]=='a':
        raise forms.ValidationError("NAME DOESNOT START WITH A ")


def length(value):

    if len(value) >5:
        raise forms.ValidationError("length exceeed")

# def check_age(value):

#     if value<18:
#         raise forms.ValidationError("Invalid credentials")

class userform(forms.Form):

    name = forms.CharField(max_length=100,validators = [validate_for_a,length])

    # age = forms.IntegerField(validators=[check_age])
    
    age = forms.IntegerField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    
    def clean(self):

        age  = self.cleaned_data['age']
        
        if age <18:

            raise forms.ValidationError("not suitable")

    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot is catched')