from django.db import models

# Create your models here.
class ThirdPartyTransferError(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    resource_type = models.CharField(max_length=255, blank=True, null=True)
    tenant_name = models.CharField(max_length=128, blank=True, null=True)
    dealer_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    log_file_path = models.CharField(max_length=512, blank=True, null=True)
    support_person = models.CharField(max_length=512, blank=True, null=True)
    estimate_id = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    service_advisor_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'third_party_transfer_error'