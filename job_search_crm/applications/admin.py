from django.contrib import admin
from .models import (Application, Company, CustomerProfile, Event, Position)


class ApplicationAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


class CustomerProfileAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class PositionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Position, PositionAdmin)
