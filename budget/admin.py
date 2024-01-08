from django.contrib import admin
from .models import Budget, BudgetUser, Category
from django.contrib.auth.admin import UserAdmin


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user','budget_entry_name', 'category', 'amount')
    list_editable = ('amount', )
    search_fields = ('name', 'category')


class BudgetUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_per_page = 10


# fields = list(UserAdmin.fieldsets)
# fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'password')})
# UserAdmin.fieldsets = tuple(fields)


admin.site.register(Budget, BudgetAdmin)
admin.site.register(BudgetUser, BudgetUserAdmin)
admin.site.register(Category)