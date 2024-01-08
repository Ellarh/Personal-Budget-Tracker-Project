from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('dashboard', views.DashboardView, basename='dashboard')


app_name = 'budget'

urlpatterns = [
    path('budget/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('budget-entry/', views.BudgetEntryFormView.as_view(), name='budget-entry'),
    path('update-budget/<slug:pk>/', views.UpdateBudgetEntry.as_view(), name='update_budget'),
    path('delete-budget/<slug:pk>/', views.DeleteBudgetEntry.as_view(), name='delete_budget'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout')

]
