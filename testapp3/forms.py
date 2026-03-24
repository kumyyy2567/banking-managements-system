from django import forms
from testapp3.models import Account, Transaction
class  CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class  UpdateAccountForm(forms.ModelForm):        
    class Meta:
        model = Account
        # Do not allow changing the primary key (accno) via the update form.
        # Only allow updating customer name, email and balance.
        fields = ["cname", "email", "balance"]

class TransactionForm(forms.Form):
    TRANSACTION_CHOICES = [('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')]
    accno = forms.IntegerField()
    ttype = forms.ChoiceField(choices=TRANSACTION_CHOICES)
    tamt = forms.FloatField()
    tdate = forms.DateField()