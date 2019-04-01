from django.shortcuts import render
from .models import ThirdPartyTransferError
# Create your views here.
def index(request):
    tpte = ThirdPartyTransferError.objects.filter(status = 'Failed').order_by('last_update_date').reverse()[:5]
    return render(request, "index.html",{"tpte": tpte})