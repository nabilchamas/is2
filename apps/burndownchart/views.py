from chartit import DataPool, Chart
from apps.burndownchart.models import BurndownchartDato
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def burndownchart_view(request):
    
    # Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': BurndownchartDato.objects.all()},
              'terms': [
                'sprint_dias',
                'burndown_estimado',
                'burndown_actual']}
             ])

    # Step 2: Create the Chart object
    cht = Chart(
            datasource=weatherdata,
            series_options=
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'sprint_dias': [
                    'burndown_estimado',
                    'burndown_actual']
                  }}],
            chart_options=
              {'title': {
                   'text': 'Burndownchart'},
               'xAxis': {
                    'title': {
                       'text': 'Dias'}},
               'yAxis': {
                    'title': {
                       'text': 'Tareas Pendientes'}}})

    # Step 3: Send the chart object to the template.
    return render_to_response('burndownchart/burndownchart.html', {'burndownchart': cht})




