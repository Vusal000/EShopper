from django import forms
from core.models import contact   


# class SubscriberForm(forms.ModelForm):
#     class Meta:
#         model = subscribe
#         fields = ('email',)
#         widgets ={
#             'email': forms.EmailInput(attrs={'class':' form-control border-white p-4', 'placeholder': 'Enter Your Email '})
#         }
    
#     def clean_email(self):
#         cleaned_data = super().clean()
#         user_mail = cleaned_data.get('email')
#         if user_mail :
#             if subscribe.objects.filter(email = user_mail).exists():
#                 raise forms.ValidationError("This email is already exist")
#         return cleaned_data
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email.endswith('gmail.com'):
#            raise forms.ValidationError('Please enter a valid email address')
#         return email


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = [ "name",  "text", "email"]

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control',"placeholder":"Your Email" }),
            'name': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Your Name" }),
            'text': forms.TextInput(attrs={'class': 'form-control', "rows":"6" ,"placeholder":"Message" }),
    }   

