from django.urls import path
from results.views import (
    view_single_polling_unit_result,
    view_summed_polling_results_by_lga
    )


app_name = 'results'
urlpatterns = [
    path(r'', view_single_polling_unit_result, name='single-polling-results'),
    path(r'lga', view_summed_polling_results_by_lga, name='view-summed-polling-results-by-lga'),
]
