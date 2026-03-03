import django_filters

from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = django_filters.DateFromToRangeFilter()
    status = django_filters.BooleanFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
