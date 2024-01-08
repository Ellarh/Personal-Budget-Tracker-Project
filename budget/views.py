from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets, status, generics
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from rest_framework.response import Response
from django.db.models import Sum
from .models import BudgetUser, Budget
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, BudgetEntryForm
from .serializer import BudgetSerializer, BudgetDetailSerializer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    def get_queryset(self):
        user = self.request.user
        month = self.request.GET.get('month')

        queryset = Budget.objects.filter(user=user)

        if month:
            month_date = datetime.strptime(month, '%Y-%m').date()
            # Filter the queryset based on the month and year
            queryset = queryset.filter(date__year=month_date.year, date__month=month_date.month)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = BudgetSerializer(queryset, many=True)

        total_income = queryset.filter(budget_choice='Income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = queryset.filter(budget_choice='Expense').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({'budget': serializer.data,
                         'total_income': total_income,
                         'total_expense': total_expense,
                         })


class BudgetEntryFormView(LoginRequiredMixin,CreateView):
    form_class = BudgetEntryForm
    template_name = 'budget_entry.html'
    success_url = reverse_lazy('budget:dashboard-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateBudgetEntry(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ('name', 'description', 'amount', 'category')
    success_url = reverse_lazy('budget:dashboard-list')
    template_name = 'budget_update.html'


class DeleteBudgetEntry(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('budget:dashboard-list')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password) # This will handle password hashing
            user.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('budget:index')
        else:
            messages.error(request, 'Registration failed. Please check your input.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('budget:index')
            else:
                messages.error(request, 'This user is not active')
                return redirect('budget:register')
        else:
            messages.error(request, 'Invalid login credentials. Please Try again or register')
            return redirect('budget:user_login')
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    auth.logout(request)
    return redirect('budget:index')




























