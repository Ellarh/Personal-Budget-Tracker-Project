from .models import Budget, BudgetUser, Category
from rest_framework import serializers


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class BudgetDetailSerializer(serializers.HyperlinkedModelSerializer):
    # detail_url = serializers.HyperlinkedIdentityField(view_name='budget_detail', lookup_field='pk')

    class Meta:
        model = Budget
        fields = '__all__'


class BudgetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetUser
        fields = '__all__'

