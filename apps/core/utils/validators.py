from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from rest_framework.exceptions import ValidationError


def validate_age(value):
    today = timezone.now().date()
    min_date = today - timezone.timedelta(days=10 * 365)  # 10 years ago

    if value > min_date:
        raise ValidationError(
            _('The minimum age requirement is 10 years.'),
        )
