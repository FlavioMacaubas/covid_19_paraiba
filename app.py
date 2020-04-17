## Bootstrap Grid tutorial - adding style to the app

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
from dash.dependencies import Input, Output, State, ClientsideFunction

os.chdir('C:/Users/Macaubas/PycharmProjects/untitled/venv/Scripts')

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv("paraiba_covid.csv")

eixo_dias = ['31-03-2020', '01-04-2020', '02-04-2020', '03-04-2020', '04-04-2020', '07-04-2020','08-04-2020','14-04-2020']

city_data = {
    'Paraíba': {'dias': eixo_dias, 'confirmados': [17, 20, 28,30,34,41,55,136], 'recuperados':[3,3,3,3,9,11,14,52], 'obitos':[0,1,1,1,3,4,7,14]},
    'João Pessoa': {'dias': eixo_dias, 'confirmados': [12, 14, 22, 24,26,30,40,103], 'recuperados':[0,0,0,0,0,0,0,0], 'obitos':[0,0,0,0,1,2,4,9]},
    'Bayeux': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,1,4], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,0,0,0,0,1]},
    'Cabedelo': {'dias': eixo_dias, 'confirmados': [0, 1, 1, 1, 1,1,2,5], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0, 0,0,1,2]},
    'Patos': {'dias': eixo_dias, 'confirmados': [1, 1, 1,0,1,1,1,4], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,1,1,1,1,1,1,1]},
    'Junco do Seridó': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,1,1,1,3], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,1,1,1,1]},
    'Campina Grande': {'dias': eixo_dias, 'confirmados': [2, 2, 2, 2, 2,3,3,3], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,0,0,0,0]},
    'Iguaracy': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1,1,1,1,1],'recuperados':[0,0,0,0,0,0,0,0], 'obitos':[0,0,0,0,0,0,0,0]},
    'Sousa': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1,1,1,1,1], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,0,0,0,0]},
    'Serra Branca': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,1,1,1,1,1], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,0,0,0,0,0]},
    'Santa Rita': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,2,4,10], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,0,0,0,0]},
    'Sapé': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,1], 'recuperados':[0,0,0,0,0,0,0,0],'obitos':[0,0,0,0,0,0,0,0,0]}
}

cidades_pb = [
    {'label': 'Paraíba', 'value': 'Paraíba'},
    {'label': 'João Pessoa', 'value': 'João Pessoa'},
    {'label': 'Cabedelo', 'value': 'Cabedelo'},
    {'label': 'Patos', 'value': 'Patos'},
    {'label': 'Junco do Seridó', 'value': 'Junco do Seridó'},
    {'label': 'Campina Grande', 'value': 'Campina Grande'},
    {'label': 'Iguaracy', 'value': 'Iguaracy'},
    {'label': 'Sousa', 'value': 'Sousa'},
    {'label': 'Serra Branca', 'value': 'Serra Branca'},
    {'label': 'Santa Rita', 'value': 'Santa Rita'},
    {'label': 'Bayeux', 'value': 'Bayeux'},
    {'label': 'Sapé', 'value': 'Sapé'}
]



app.layout = html.Div(
    html.Div([
        dcc.Store(id="aggregate_data"),

        #### CABEÇALHO
        html.Div(
            [
                html.H1(children='Covid-19 (Paraíba)¹ ² ³',
                        className='nine columns',
                        style={
                            'margin-top':40,
                        }),
                html.Img(
                    src=app.get_asset_url("logo_nova.jpg"),
                    className='three columns',
                    style={
                        'height': '10%',
                        'width': '10%',
                        'float': 'right',
                        'position': 'relative',
                    },
                ),
                html.Img(
                    src=app.get_asset_url("ufpb.png"),
                    className='three columns',
                    style={
                        'height': '6%',
                        'width': '6%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top':15,
                    },
                ),
                html.Div(children='''
                        Laboratório de Inteligência Artificial e Macroeconomia Computacional.
                        ''',
                        className='nine columns',
                        style={
                             'margin-bottom': 40,
                         }
                )
            ], className="row"
        ),

        dcc.Markdown(children=''' > Atualizado pelo Boletim Epidemiológico nº 9 de 14/04/2020.'''),

        # Containers para mostrar os valores
        html.Div(
            [
                # Dropdown para selecionar cidade
                html.Div(
                    [
                        dcc.Markdown(children='''O gráfico de barras mostrará os dados da primeira cidade selecionada.
                                                    Como padrão, os dados apresentados são o do Estado.'''),
                        html.P('Escolha cidade:'),
                        dcc.Dropdown(
                            id='Cities',
                            options=cidades_pb,
                            value =['Paraíba'],
                            multi = True,
                            className="dcc_control",
                        ),

                        html.P('Filtrar dados por:'),
                        dcc.RadioItems(
                            id="situacao",
                            options=[
                                {"label": "Confirmados ", "value": "confirmados"},
                                {"label": "Recuperados", "value": "recuperados"},
                                {"label": "Óbitos ", "value": "obitos"},
                            ],
                            value="confirmados",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        )
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),

                # Radio items para selecionar status


                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="well_text"), html.P("Suspeitos")],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="gasText"), html.P("Confirmados")],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="oilText"), html.P("Recuperados")],
                                    id="oil",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="waterText"), html.P("Óbitos")],
                                    id="water",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),

                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),


        # Exibe os gráficos
        html.Div(
            [
                html.Div([
                    dcc.Graph(
                        id='example-graph'
                    )
                ], className='six columns'
                ),

                html.Div([
                    dcc.Graph(
                        id='example-graph-2'
                    )
                ], className='six columns'
                )
            ], className="row"
        ),


        # Notas de roda pé
        html.Div([
            dcc.Markdown(
                children='''
           ¹ O Dashboard apresentado trata-se de uma iniciativa do Laboratório da Inteligência Artificial e Macroeconomia Computacional (LABIMEC), 
             ainda em versão de testes. O propósito é facilitar a visualização do coronavírus no estado da Paraíba e em seus municípios. Futuras funcionalidades
             estão sendo implementadas pela equipe do laboratório, para sugestões entrar em contato nos seguintes emails:

             * cassiodanobrega@yahoo.com.br - Coordenador do LABIMEC
             * flaviomacaubas@gmail.com - Membro do LABIMEC
             '''),

            dcc.Markdown(
                children='''
           ² Os dados disponibilizados são provenientes dos [Boletins Epidemiológicos Coronavírus / Covid-19](https://paraiba.pb.gov.br/diretas/saude/consultas/vigilancia-em-saude-1/boletins-epidemiologicos)
            da Secretaria de Saúde de Estado da Paraíba. Não há dados de recuperados discriminado por município, por esta razão não é possível gerar 
            os gráficos de série temporal.
           '''),

            dcc.Markdown(
                children='''
          ³ O Dashboard não substitui, sob qualquer hipótese, os dados oficiais do Governo do Estado da Paraíba.
          ''')
        ], className = "six columns")

    ], className='ten columns offset-by-one')


)


# Atualiza gráfico de barras
@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'value')])
def update_image_src(selector):
    if len(selector) == 0:
        selector.append('Paraíba')
    data = []
    if  selector[0] == "Paraíba":
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['confirmados'],
                         'type': 'bar', 'name': 'Confirmados', 'marker' : { "color" : 'crimson'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['recuperados'],
                         'type': 'bar', 'name': 'Recuperados', 'marker' : { "color" : 'blue'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['obitos'],
                         'type': 'bar', 'name': 'Óbitos', 'marker' : { "color" : 'black'}})
    else:
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['confirmados'],
                         'type': 'bar', 'name': 'Confirmados', 'marker' : { "color" : 'crimson'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['obitos'],
                         'type': 'bar', 'name': 'Óbitos', 'marker' : { "color" : 'black'}})
    figure = {
        'data': data,
        'layout': {
            'title': 'Panorama Confirmados/Recuperados/Óbitos {}'.format(selector[0]),
            'xaxis': dict(
                title='Dia',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='Quantidade',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure

# Atualiza gráfico de linha
@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities', 'value'), dash.dependencies.Input('situacao','value')])
def update_image_src(selector, situacao):
    data = []
    for city in selector:
        data.append({'x': city_data[city]['dias'], 'y': city_data[city][situacao],
                     'type': 'line', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'title': 'Série Temporal - Quantidade de {}'.format(situacao),
            'xaxis': dict(
                title='Dia',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='Quantidade',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


@app.callback(
    [
        Output("well_text", "children"),
        Output("gasText", "children"),
        Output("oilText", "children"),
        Output("waterText", "children"),
    ],
    [Input("aggregate_data", "data")],
)
def update_text(data):
    return '---', city_data['Paraíba']['confirmados'][-1], city_data['Paraíba']['recuperados'][-1],city_data['Paraíba']['obitos'][-1]

if __name__ == '__main__':
    app.run_server(debug=True)
