from django.shortcuts import render
from .models import RowCallDetaiRecord
# Create your views here.


def index(request):
    cdrs = RowCallDetaiRecord.objects.all().order_by('-start_ring')
    return render(request, template_name='readcsv/base.html', context={'cdrs':cdrs})