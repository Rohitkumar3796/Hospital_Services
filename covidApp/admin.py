from django.contrib import admin
from django.db import models
from django.db.models.expressions import F
from covidApp.models import State, City, Hospital, Facility, Availability


# ADD SIGNALS
# This signal is use for when you want to add data in one model on admin but you want add that data to another model so there you have to use signals  (Eg we add data in hospital model, that data add to services also, So in services we have not add data separately)
# from-----
from django.db.models.signals import post_save
# receiver is a decorator
from django.dispatch import receiver

@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    facilities = Facility.objects.all()
    for facility in facilities:
        availability = Availability(hospital = instance, facility = facility)
        availability.save() 

@receiver(post_save, sender=Facility)
def afterFacilitySave(signal, instance, **kwargs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availability = Availability(hospital = hospital, facility = instance)
        availability.save() 

# END-----
#  THIS CLASSES FOR DATA SHOWING IN THE TABLE
class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['title']

    #this fucntion is used to show data in this format (4/10) 



class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name', 'phone', 'address', 'city']

class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'state']

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital', 'facility','total','available','updated_at']
    list_editable = ['total','available']


# Register your models here.
admin.site.register(State)
admin.site.register(City, CityAdmin) 
admin.site.register(Hospital, HospitalAdmin) #we have to register the class here
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availability, AvailabilityAdmin)


