from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import JsonResponse

from .models import *
from .forms import TransactionForm


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        return render(request,'budget_settings/dashboard.html')


def transaction_edit(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(instance=transaction)
        category = Category.objects.all().order_by('Name')
        account = Account.objects.all().order_by('Name')
        transaction_number = increment_transaction_number()
        context = {
            'category_list': category,
            'account_list': account,
            'transaction_number': transaction_number,
            'form': form
        }
        if request.method == 'POST':
            form = TransactionForm(request.POST, instance=transaction)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/transaction_list/')
            else:
                return HttpResponseRedirect('/transaction_edit/')
        return render(request, 'budget_settings/transaction_new.html', context)


def transaction_new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        form = TransactionForm()
        category = Category.objects.all().order_by('Name')
        account = Account.objects.all().order_by('Name')
        transaction_number = increment_transaction_number()
        context = {
            'category_list': category,
            'account_list': account,
            'transaction_number': transaction_number,
            'form': form,
        }
        if request.method == 'POST':
            form = TransactionForm(request.POST)
            if form.is_valid():
                Transaction = form.save(commit=False)
                Transaction.created_by = request.user
                Transaction.save()
                return HttpResponseRedirect('/transaction_list/')
            else:
                return render(request, 'budget_settings/transaction_new.html', context)
        else:
            form = TransactionForm()
            return render(request, 'budget_settings/transaction_new.html', context)


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    context = {
        'transaction': transaction
    }
    if request.method == 'POST':
        transaction.delete()
        return HttpResponseRedirect('/transaction_list/')
    return render(request, 'budget_settings/transaction_delete.html', context)


def transaction_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        transaction = Transaction.objects.all().order_by('-Date','-Number')
        context = {
            'transaction_list': transaction,
        }
        return render(request, 'budget_settings/transaction_list.html',context)


def settings_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_user/')
    else:
        return render(request, 'budget_settings/settings.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = settings.LOGIN_REDIRECT_URL
                print('OK')
                return redirect(redirect_to)
            else:
                context = {
                    'error': 'Your My Money account is disabled.',
                }
                return render(request, 'budget_settings/login.html',context)
        else:
            context = {
                'error': 'Invalid Login or Password.',
            }
            return render(request, 'budget_settings/login.html', context)
    else:
        context = {
            'error': '',
        }
        return render(request, 'budget_settings/login.html', context)


def logout_user(request):
    logout(request)
    context = {
        "form": '',
    }
    return render(request, 'budget_settings/login.html', context)
