import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModelMixin(models.Model):
    __doc__ = _("Base Model includes `created_at` and `updated_at`.")
    uuid = models.UUIDField(
        _("UUID"),
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        editable=False,
        help_text=_("Timestamp when the object was created.")
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']
