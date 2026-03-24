from django.urls import path
from testapp3 import views

urlpatterns = [
    path('', views.HomeTemplate.as_view(), name='home'),
    path('create_acc/', views.CreateAccountFromView.as_view(), name='create_acc'),
    path('update_input/', views.EditAccountView.as_view(), name='edit_account'),
    path('read_acc/', views.ReadAccountView1.as_view(), name='read_account'),
    path('details/<int:pk>/', views.AccountDetailsView.as_view(), name='account_details'),
    path('update_acc/<int:pk>/', views.UpdateAccountView.as_view(), name='update_account'),
    path('transaction/', views.TransactionTemplateView.as_view(), name='transaction'),
    path('transaction_process/', views.TransactionView.as_view(), name='transaction_process'),
    path('transaction_history/', views.TransactionsHistTemp.as_view(), name='transaction_history'),
    path('trans_report/', views.TransactionHistView.as_view(), name='trans_report'),
]
