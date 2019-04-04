from django.contrib import admin

# Register your models here.
from .models import ThirdPartyTransferError
class ThirdPartyTransferErrorAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ("tenant_name","status" ,"dealer_id", "create_date", "machine_id")
    def download_csv(self, request, queryset):
        import csv
        f = open('ro_failure.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(["tenant_name","status" ,"dealer_id", "create_date", "machine_id"])
        for s in queryset:
            writer.writerow([s.tenant_name, s.status, s.dealer_id, s.create_date, s.machine_id])
    download_csv.short_description = "Download CSV file for selected failures."

admin.site.register(ThirdPartyTransferError,ThirdPartyTransferErrorAdmin)
