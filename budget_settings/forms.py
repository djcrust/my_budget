from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionForm(forms.ModelForm):
    Date = forms.DateField(
        widget=DateInput(attrs={
            'class': 'form-control datetimepicker-input',
        })
    )
    Account = forms.ModelChoiceField(
        queryset=Account.objects.all().order_by('Name'),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    Category = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('Name'),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    Withdrawal = forms.DecimalField(
        initial=0,
        label='Debit',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    Image = forms.ImageField(
        required=False,

    )
    Deposit = forms.DecimalField(
        initial=0,
        label='Credit',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    Comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Enter a comment'
            }
    ))

    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['created_at', 'created_by', 'updated_at', 'updated_by', 'Number']
