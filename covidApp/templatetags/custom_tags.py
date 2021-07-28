# register.simple_tag study for this

from covidApp.models import Availability
from django import template

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        # if its having a value so it will show in green color else red color
        return 'bg-success'
    return 'bg-danger'


# we call this function from index.html 
@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')

@register.simple_tag
def is_option_selected(selected_option, pk):
    if selected_option == str(pk):
        return 'selected'
    return ''