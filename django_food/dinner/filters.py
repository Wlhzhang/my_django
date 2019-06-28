import django_filters

from dinner.models import DinnerInfo


class DinnerFilter(django_filters.FilterSet):
    # price = django_filters.DateFromToRangeFilter('饭局价格',max_digits=8,decimal_places=2)
    # number = django_filters.IsoDateTimeFilter('人数')
    # activities_play = django_filters.CharFilter('活动玩法', max_length=30)
    # username = django_filters.CharFilter(method='my_custom_filter')
    class Meta:
        model = DinnerInfo
        fields = {
            'price': ['lte', 'gte'],
            'number': ['lte', 'gte'],
            'activities_play':['contains']
        }
