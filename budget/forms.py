from .models import BudgetUser, Budget
from django import forms


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = BudgetUser
        fields = ('first_name', 'email', 'password')


class BudgetEntryForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ('budget_entry_name', 'description', 'category', 'amount', 'budget_choice', 'month')
