from django.http.request import HttpRequest
from polling_units.models import PollingUnit
from lgas.models import Lga
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from results.models import (
    AnnouncedPuResults,
    )


def view_single_polling_unit_result(request:HttpRequest) -> HttpResponse:
    '''
    Renders a view with an individual polling unit's result added into the context to be displayed
    '''
    # Get a sample polling unit to be rendered using it's `uniqueid` field or raise a 404 if requested object does not exist
    # I would have done this passing the uniqueid as an arg to the view (i.e results/view_single_polling_unit/<uniqueid>/) 
    # but since this is just for development and not production I have hardcoded a verified uniqueid for this 
    sample_polling_unit = get_object_or_404(PollingUnit, uniqueid=15)

    # We are using the polling unit's `uniqueid` field for filtering all `AnnouncedPuResults`
    # model objects having `polling_unit_uniqueid` as the uniqueid in question
    # this way we are able to get announced results for a given polling unit
    sample_polling_unit_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=sample_polling_unit.uniqueid)
    context = {
        'polling_state': 'delta state',
        'sample_polling_unit': sample_polling_unit,
        'sample_polling_unit_results': sample_polling_unit_results,
    }
    return render(request, 'results/single polling unit results.html', context)

def view_summed_polling_results_by_lga(request:HttpRequest) -> HttpResponse:
    '''
    Renders a view of the summed results of all individual polling units of an Local Government Area
    '''
    lga_id = request.POST.get("lga_id") if request.method == "POST" else 6
    sample_lga = get_object_or_404(Lga, lga_id=lga_id)
    polling_units_of_sample_lga = PollingUnit.objects.filter(lga_id=sample_lga.lga_id)
    _result = []
    if polling_units_of_sample_lga.count():
        for polling_unit in polling_units_of_sample_lga:
            _result += [announced_pu_result.party_score for announced_pu_result in AnnouncedPuResults.objects.filter(polling_unit_uniqueid=polling_unit.uniqueid) if isinstance(announced_pu_result.party_score, int)]
    summed_result = sum(_result)
    context = {
        'polling_state': 'delta state',
        'sample_lga_name': sample_lga.lga_name,
        'summed_total_of_results': summed_result,
        'polling_units_of_sample_lga': polling_units_of_sample_lga,
    }
    return render(request, 'results/summed results of polling units by lga.html', context)
