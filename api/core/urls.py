from .viewsets import CreateOutlierProbabilityViewset, ListOutliersProbabilityViewset
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('api/create_outlier/', CreateOutlierProbabilityViewset.as_view(), name='outliers'),
    path('api/list_outliers/<str:project_name>/<str:table_name>/', ListOutliersProbabilityViewset.as_view(), name='outliers'),
    ]
