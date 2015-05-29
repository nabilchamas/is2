from chartit import DataPool, Chart
from apps.burndownchart.models import BurndownchartDato
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.proyecto.models import Proyecto
from django.shortcuts import render


def burndownchart_view(request, proyecto_id):
    
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    # Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': BurndownchartDato.objects.filter(proyecto_id = proyecto_id)},
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

    return render_to_response('burndownchart/burndownchart.html', {'burndownchart': cht, 'proyecto': proyecto.nombre})


def listar_proyectos_burndownchart(request):
    '''
        Lista los proyectos
    '''
    lista_proyectos = Proyecto.objects.all()
    context = {'lista_proyectos':lista_proyectos}
    return render(request, 'burndownchart/listar_proyectos_burndownchart.html', context)



