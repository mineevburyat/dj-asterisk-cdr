from django.contrib import admin

from .models import RowCallDetaiRecord


# class DetailsInline(admin.TabularInline):
#     model = CDR_details
#     extra = 0

# Register your models here.


@admin.register(RowCallDetaiRecord)
class CDR_Record_UniqAdmin(admin.ModelAdmin):
    # inlines = [DetailsInline]
    list_display = ('uniquedid', 'from_phone', 'to_phone', 'start_ring', 'is_audio')
    sortable_by = ('uniquedid', 'start_ring')