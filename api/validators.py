from django.core.exceptions import ValidationError
import datetime

def year_validation(value):
    if value > datetime.datetime.now().year:
        raise ValidationError(
            _('%(value)s is not acceptable!'),
            params={'value': value},
        )