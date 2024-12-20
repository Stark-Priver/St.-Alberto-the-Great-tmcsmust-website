# Generated by Django 4.2.15 on 2024-08-21 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MoyomtakatifuwaYesuMemberTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Ada', 'Ada')], max_length=50, verbose_name='Transaction Type')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('transaction_date', models.DateField(auto_now_add=True, verbose_name='Transaction Date')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moyomtakatifuwaYesuTransactions', to=settings.AUTH_USER_MODEL, verbose_name='Member Unique Identifier')),
            ],
            options={
                'verbose_name': 'Moyo Mtakatifu wa Yesu Malipo ya Ada',
                'verbose_name_plural': 'Moyo Mtakatifu wa Yesu Malipo ya Ada',
            },
        ),
    ]
