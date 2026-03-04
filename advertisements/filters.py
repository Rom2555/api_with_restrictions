import django_filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = django_filters.DateFromToRangeFilter()
    status = django_filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator', ]
