from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView
from django.views import View
from testapp3.forms import CreateAccountForm, UpdateAccountForm, TransactionForm
from django.urls import reverse_lazy
from testapp3.models import Account, Transaction


# Create your views here.
class HomeTemplate(TemplateView):
    template_name = 'home.html'

class CreateAccountFromView(CreateView):
    form_class = CreateAccountForm
    template_name = "create_acc.html"
    success_url = reverse_lazy("home")

class UpdateAccountView(UpdateView):
    model = Account
    form_class = UpdateAccountForm
    template_name = "update_acc.html"
    success_url = reverse_lazy("home")
    context_object_name = "account"

class EditAccountView(View):
    def get(self, request):
        return render(request, "update_input.html")
    
    def post(self, request):
        accno = request.POST.get("accno")
        url = f"/update_acc/{accno}/"
        return redirect(url)

class ReadAccountView(TemplateView):
    def get(self,request):
        accno =request.GET.get("accno")
        url = "/update_acc/" + str(accno)
        response = redirect(url)
        return response
    
class AccountDetailsView(DetailView):
    model = Account
    template_name  = "details.html"
    context_object_name = "account"

class ReadAccountView1(View):
    def get(self, request):
        accno = request.GET.get("accno")
        url = '/details/' + str(accno)
        response = redirect(url)
        return response
    
class ReadAccountTemplate(TemplateView):
    template_name  = "details_input.html" 

class TransactionTemplateView(TemplateView):
    template_name = "transaction.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TransactionForm()
        return context

class TransactionView(View):
    def post(self, request):
        accno = request.POST.get('accno')
        ttype = request.POST.get('ttype')
        tamt = request.POST.get('tamt')
        tdate = request.POST.get('tdate')
        account = Account.objects.get(accno=accno)
        if ttype == "deposit":
            account.balance = account.balance + int(tamt)
        elif ttype == "withdrawal":
            account.balance = account.balance - int(tamt)
        account.save()
        t1 = Transaction(accno=account, ttype=ttype, tamt=tamt, tdate=tdate)
        t1.save()
        response = redirect(reverse_lazy("home"))
        return response
    
class TransactionsHistTemp(TemplateView):
    template_name = "transaction_history.html"


class TransactionHistView(View):
    def get(self, request):
        accno = request.GET.get('accno')
        account = Account.objects.get(accno=accno)
        qs = Transaction.objects.filter(accno=account)
        response = render(request, "trans_rep.html", context={'qs': qs})
        return response
      
       