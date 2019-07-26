from django.core.exceptions import ValidationError


def validate_region_subset_of_city(value):
    regions = Region.objects.filter(city = value)
    
    if value not in regions:
        raise ValidationError('Origin Region must be subset of origin City.')
