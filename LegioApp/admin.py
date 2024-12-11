from django.contrib import admin
from .models import LegioMemberTransaction



@admin.register(LegioMemberTransaction)
class LegioMemberTransactionAdmin(admin.ModelAdmin):
    list_display = ['member','transaction_type', 'amount', 'transaction_date']
    list_filter = ['transaction_type', 'transaction_date']
    search_fields = ('member__unique_identifier', 'transaction_type')