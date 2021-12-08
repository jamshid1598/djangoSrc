from import_export.widgets import (
    Widget,
    format_datetime,
)
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_str, smart_str
from datetime import (
    datetime,
    date,
    timezone,
)


class DateWidget(Widget):
    def __init__(self, format=None):
        if format is None:
            if not settings.DATE_INPUT_FORMATS:
                formats = ("%Y-%m-%d",)
            else:
                formats = settings.DATE_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, date):
            return value
        for format in self.formats:
            try:
                return datetime.strptime(value, format).date()
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date.")

    def render(self, value, obj=None):
        if not value:
            return ""
        return format_datetime(value, self.formats[0])


class DateTimeWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter. If none is set, either
    ``settings.DATETIME_INPUT_FORMATS`` or ``"%Y-%m-%d %H:%M:%S"`` is used.
    """

    def __init__(self, format=None):
        if format is None:
            if not settings.DATETIME_INPUT_FORMATS:
                formats = ("%Y-%m-%d %H:%M:%S",)
            else:
                formats = settings.DATETIME_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, datetime):
            return value
        for format in self.formats:
            try:
                dt = datetime.strptime(value, format)
                if settings.USE_TZ:
                    # make datetime timezone aware so we don't compare
                    # naive datetime to an aware one
                    dt = timezone.make_aware(dt,
                                             timezone.get_default_timezone())
                return dt
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date/time.")

    def render(self, value, obj=None):
        if not value:
            return ""
        if settings.USE_TZ:
            value = timezone.localtime(value)
        return format_datetime(value, self.formats[0])


class ForeignKeyWidget(Widget):
    def __init__(self, model, field='pk', *args, **kwargs):
        self.model = model
        self.field = field
        super().__init__(*args, **kwargs)

    def get_queryset(self, value, row, *args, **kwargs):
        """
        Returns a queryset of all objects for this Model.

        Overwrite this method if you want to limit the pool of objects from
        which the related object is retrieved.

        :param value: The field's value in the datasource.
        :param row: The datasource's current row.

        As an example; if you'd like to have ForeignKeyWidget look up a Person
        by their pre- **and** lastname column, you could subclass the widget
        like so::

            class FullNameForeignKeyWidget(ForeignKeyWidget):
                def get_queryset(self, value, row):
                    return self.model.objects.filter(
                        first_name__iexact=row["first_name"],
                        last_name__iexact=row["last_name"]
                    )
        """
        return self.model.objects.all()

    def clean(self, value, row=None, *args, **kwargs):
        val = super().clean(value)
        if val:
            return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val})
        else:
            return None

    def render(self, value, obj=None):
        if value is None:
            return ""

        attrs = self.field.split('__')
        for attr in attrs:
            try:
                value = getattr(value, attr, None)
            except (ValueError, ObjectDoesNotExist):
                # needs to have a primary key value before a many-to-many
                # relationship can be used.
                return None
            if value is None:
                return None

        return value


class ManyToManyWidget(Widget):
    """
    Widget that converts between representations of a ManyToMany relationships
    as a list and an actual ManyToMany field.

    :param model: The model the ManyToMany field refers to (required).
    :param separator: Defaults to ``','``.
    :param field: A field on the related model. Default is ``pk``.
    """

    def __init__(self, model, separator=None, field=None, *args, **kwargs):
        if separator is None:
            separator = ','
        if field is None:
            field = 'pk'
        self.model = model
        self.separator = separator
        self.field = field
        super().__init__(*args, **kwargs)

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()
        if isinstance(value, (float, int)):
            ids = [int(value)]
        else:
            ids = value.split(self.separator)
            ids = filter(None, [i.strip() for i in ids])
        return self.model.objects.filter(**{
            '%s__in' % self.field: ids
        })

    def render(self, value, obj=None):
        ids = [smart_str(getattr(obj, self.field)) for obj in value.all()]
        return self.separator.join(ids)