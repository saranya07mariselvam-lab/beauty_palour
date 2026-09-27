from django import forms
from .models import Enquiry,Testimonial



class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Your Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Phone Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email (optional)'
            }),
            'service': forms.Select(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Preferred date/time or special request',
                'rows': 4
            }),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['customer_name', 'message', 'rating']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Your Name'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Share your experience with us...',
                'rows': 4
            }),
            'rating': forms.Select(
                choices=[(5, '5 - Excellent'), (4, '4 - Good'), (3, '3 - Average'), (2, '2 - Below Average'), (1, '1 - Poor')],
                attrs={'class': 'form-control'}
            ),
        }