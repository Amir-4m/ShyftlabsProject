from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.utils.validators import validate_age
from mixins.model_mixins import BaseModelMixin


class Student(BaseModelMixin):
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=64,
    )
    family_name = models.CharField(
        verbose_name=_("Family Name"),
        max_length=64
    )
    email = models.EmailField(
        verbose_name=_("Email"),
    )
    courses = models.ManyToManyField(
        to='Course',
        verbose_name=_("Student Courses"),
        through='StudentCourse'
    )
    date_of_birth = models.DateField(
        verbose_name=_('Date Of Birth'),
        validators=[validate_age]
    )
    is_active = models.BooleanField(
        verbose_name=_('Active?'),
        default=True
    )

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Course(BaseModelMixin):
    title = models.CharField(
        _("Title"),
        max_length=64,
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Active?'),
        default=True
    )

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return f"{self.title}"


class StudentCourse(BaseModelMixin):
    class ScoreChoices(models.TextChoices):
        A = 'A', _('A')
        B = 'B', _('B')
        C = 'C', _('C')
        D = 'D', _('D')
        E = 'E', _('E')
        F = 'F', _('F')

    student = models.ForeignKey(
        Student,
        verbose_name=_('Student'),
        related_name='student_courses',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_('Course'),
        related_name='student_courses',
        on_delete=models.CASCADE
    )
    score = models.CharField(
        verbose_name=_('Score'),
        choices=ScoreChoices.choices,
        max_length=1,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Active?'),
        default=True
    )

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return f"{self.student}-{self.course}"
