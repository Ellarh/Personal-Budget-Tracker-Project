# Generated by Django 5.0 on 2024-01-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_budget_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='budget_choice',
            field=models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], default='Expense', max_length=10),
        ),
    ]
