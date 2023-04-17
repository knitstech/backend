from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import ShortUUIDField


User = get_user_model()


class Pattern(models.Model):
    pattern_number = ShortUUIDField(_("Pattern number"))
    prompt = models.TextField("Users text")
    author = models.ForeignKey(
        User,
        related_name="pattern_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Author"),
    )
    created_up = models.DateTimeField("request time", auto_now_add=True)
