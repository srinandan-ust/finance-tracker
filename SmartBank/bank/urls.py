from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', login_required(views.dashboard_view), name='dashboard'),
    path('deposit/', login_required(views.deposit_view), name='deposit'),
    path('withdraw/', login_required(views.withdraw_view), name='withdraw'),
    path('finance/emi/', login_required(views.emi_view), name='emi'),
    path('finance/sip/', login_required(views.sip_view), name='sip'),
    path('finance/fd/', login_required(views.fd_view), name='fd'),
    path('finance/rd/', login_required(views.rd_view), name='rd'),
    path('finance/retirement/', login_required(views.retirement_view), name='retirement'),
    path('finance/home-loan/', login_required(views.home_loan_view), name='home_loan'),
    path('finance/credit-card/', login_required(views.credit_card_view), name='credit_card'),
    path('finance/tax/', login_required(views.tax_view), name='tax'),
    path('finance/budget/', login_required(views.budget_view), name='budget'),
    path('finance/net-worth/', login_required(views.net_worth_view), name='net_worth'),
]
