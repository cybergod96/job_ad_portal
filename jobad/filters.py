from .models import Advertisement
import django_filters


class AdFilter(django_filters.FilterSet):
    employer__company_name = django_filters.CharFilter(label='Nazwa firmy', lookup_expr='icontains')
    job_title = django_filters.CharFilter(label='Nazwa stanowiska', lookup_expr='icontains')
    employer__branch = django_filters.CharFilter(label='Nazwa branży', lookup_expr='icontains')

    class Meta:
        model = Advertisement
        fields = ['employer__company_name', 'job_title', 'employer__branch', ]