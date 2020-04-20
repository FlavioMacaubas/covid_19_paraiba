# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
from textwrap import dedent


app = dash.Dash(__name__)
server = app.server
app.title = "Covid-19 Paraíba"

eixo_dias = ['31-03-2020', '01-04-2020', '02-04-2020', '03-04-2020',
             '04-04-2020', '07-04-2020','08-04-2020','13-04-2020',
             '14-04-2020', '15-04-2020', '16-04-2020', '17-04-2020',
             '18-04-2020', '19-04-2020']

city_data = {
    'Paraíba': {'dias': eixo_dias, 'confirmados': [17, 20, 28,30,34,41,55,136, 152, 165,195,205,236,245],
                'recuperados':[3,3,3,3,9,11,14,52,52,80,80,90,90,99],
                'obitos':[0,1,1,1,3,4,7,14,21,24,26,28,29,32]},

    'João Pessoa': {'dias': eixo_dias, 'confirmados': [12, 14, 22, 24,26,30,40,103,115,124,142,148,163,172], 
                    'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    'obitos':[0,0,0,0,1,2,4,9,12,14,14,15,15,17]},
  
    'Bayeux': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,1,4,4,4,6,6,8,8], 
               'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               'obitos':[0,0,0,0,0,0,0,0,1,1,1,1,1,1]},
  
    'Cabedelo': {'dias': eixo_dias, 'confirmados': [0, 1, 1, 1, 1,1,2,5,5,6,7,8,9,9], 
                 'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 'obitos':[0,0,0,0,0,0,1,2,2,2,2,2,2,2]},
  
    'Patos': {'dias': eixo_dias, 'confirmados': [1, 1, 1,0,1,1,1,4,4,4,5,5,7,8], 
              'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              'obitos':[0,1,1,1,1,1,1,1,1,1,2,2,2,2]},
  
    'Junco do Seridó': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,1,1,1,3,3,3,3,3,3,3], 
                        'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        'obitos':[0,0,0,0,1,1,1,1,1,1,1,1,1,1]},
  
    'Campina Grande': {'dias': eixo_dias, 'confirmados': [2, 2, 2, 2, 2,3,3,3,3,4,8,8,12,12], 
                       'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       'obitos':[0,0,0,0,0,0,0,0,0,0,1,1,1,2]},
  
    'Igaracy': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                 'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                 'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Sousa': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1], 
              'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Serra Branca': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,1,1,1,1,1,1,1,1,1,1], 
                     'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Santa Rita': {'dias': eixo_dias, 
                   'confirmados': [0, 0, 0, 0,0,2,4,10,12,14,17,17,21,20], 
                   'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   'obitos':[0,0,0,0,0,0,0,0,1,1,1,1,2,2]},
  
    'Sapé': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,1,1,1,1,1,1,2,2], 
             'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             'obitos':[0,0,0,0,0,0,0,0,0,0,1,1,1,1]},
  
    'Taperoá': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,1,1,1,1,1,1,1], 
                'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                'obitos':[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]},
  
    'São João do Rio do Peixe': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,1,1,1,1,1,1], 
                                 'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Pombal': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,0,0,1,2,2,2], 
               'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Riachão do Poço': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,0,0,0,1,1,1], 
                        'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        'obitos':[0,0,0,0,0,0,0,0,0,0,0,1,1,1]},
  
    'São Bento': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,0,0,0,1,1,1], 
                  'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Congo': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,0,0,0,0,1,1], 
              'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
  
    'Queimadas': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0,0,0,0,0,0,0,0,0,1,1], 
                  'recuperados':[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  'obitos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
}

cidades_pb = [
    {'label': 'Paraíba', 'value': 'Paraíba'},
    {'label': 'João Pessoa', 'value': 'João Pessoa'},
    {'label': 'Cabedelo', 'value': 'Cabedelo'},
    {'label': 'Patos', 'value': 'Patos'},
    {'label': 'Junco do Seridó', 'value': 'Junco do Seridó'},
    {'label': 'Campina Grande', 'value': 'Campina Grande'},
    {'label': 'Igaracy', 'value': 'Igaracy'},
    {'label': 'Sousa', 'value': 'Sousa'},
    {'label': 'Serra Branca', 'value': 'Serra Branca'},
    {'label': 'Santa Rita', 'value': 'Santa Rita'},
    {'label': 'Bayeux', 'value': 'Bayeux'},
    {'label': 'Sapé', 'value': 'Sapé'},
    {'label': 'Taperoá', 'value': 'Taperoá'},
    {'label': 'São João do Rio do Peixe', 'value': 'São João do Rio do Peixe'},
    {'label': 'Pombal', 'value': 'Pombal'},
    {'label': 'Riachão do Poço', 'value': 'Riachão do Poço'},
    {'label': 'São Bento', 'value': 'São Bento'},
    {'label': 'Congo', 'value': 'Congo'},
    {'label': 'Queimadas', 'value': 'Queimadas'}
]

def build_modal_info_overlay(id, side, content):
    """
    Build div representing the info overlay for a plot panel
    """
    div = html.Div([  # modal div
        html.Div([  # content div
            html.Div([
                html.H4([
                    "Info",
                    html.Img(
                        id=f'close-{id}-modal',
                        src="assets/times-circle-solid.svg",
                        n_clicks=0,
                        className='info-icon',
                        style={'margin': 0},
                    ),
                ], className="container_title", style={'color': 'white'}),

                dcc.Markdown(
                    content
                ),
            ])
        ],
            className=f'modal-content {side}',
        ),
        html.Div(className='modal')
    ],
        id=f"{id}-modal",
        style={"display": "none"},
    )

    return div

app.layout = html.Div(
    html.Div([
        build_modal_info_overlay('indicator', 'bottom', dedent("""
    A _**Escolha de Cidades**_ é um painel em que você pode selecionar os municípios que você
    deseja ver a evolução do covid-19. Como padrão, mostrará os valores da Paraíba e de 
    João Pessoa.

    A primeira opção selecionada indicará qual informação deve ser mostrada nos
     quadros de valores (suspeitos, confirmados, recuperados e óbitos). Dessa forma, caso
     você queira ver os dados do seu município no Panorama e nos quadros de valores, você deve
     deixá-lo como primeira opção.

     A filtragem funciona apenas para o gráfico de Série Temporal. Ainda não é possível encontrar dados
     de recuperados por município, caso você tenha essa informação e/ou esse meio, entrar em contato em dos
     emails da nota de roda pé.
    """)),

        build_modal_info_overlay('map', 'bottom', dedent("""
    O _**Mapa**_ destaca os municípios que tiveram casos confirmados de covid-19 no estado
    da Paraíba. Ao clicar em um território, você pode visualizar informações detalhadas da região. 

    Os mapas são organizados pela paleta de vermelho, quanto mais escuro mais casos relativamente ao total
    de casos no estado, quanto mais claro, menos caso relativo a quantidade total de casos do estado.
    """)),
        build_modal_info_overlay('range', 'top', dedent("""
    O _**Panorama Confirmados/Recuperados/Óbitos**_ mostra a quantidade de cada um desses campos no decorrer
    dos dias no estado. Facilita a interpretação da proporção de óbitos e recuperação em relação ao total.
    """)),

        build_modal_info_overlay('created', 'top', dedent("""
    A _**Série Temporal**_ mostra a quantidade de casos confirmados/recuperados/óbitos por dia, ainda não se tem
    dados de recuperados por município. Caso você selecione mais de 1 município, você poderá comparar a evolução
    do fenômeno.
        """)),

        dcc.Store(id="aggregate_data"),

        #### CABEÇALHO
        html.Div([
            html.H1(children=[
                'Covid-19 (Paraíba)¹²³',
                html.A(
                    html.Img(
                        src="assets/logo_nova.jpg",
                        style={'float': 'right', 'height': '150px'}
                    ),

                    href="https://dash.plot.ly/"),
            ], style={'text-align': 'left'}),
          
            html.H6(children=[
                'Laboratório de Inteligência Artificial e Macroeconomia Computacional - LABIMEC'
            ], style={'text-align': 'left'}),
          
        ]),

        dcc.Markdown(children=
                     ''' > Atualização Covid-19 19/04 às 17h. Para melhor experiência acesse pelo computador.

                         
        '''),

        # Containers para mostrar os valores
        html.Div(
            [
                # Dropdown para selecionar cidade
                html.Div(
                    [
                        html.H4([
                            "Escolha as cidades que deseja:",
                            html.Img(
                                id='show-indicator-modal',
                                src="assets/question-circle-solid.svg",
                                className='info-icon',
                            ),
                        ], className="container_title"),

                        dcc.Dropdown(
                            id='Cities',
                            options=cidades_pb,
                            value=['Paraíba', 'João Pessoa'],
                            multi=True,
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
                        ),
                    ],
                     className ='six columns pretty_container',
                     id="indicator-div"
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="well_text"), html.P("Ativos")],
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

        # Gráficos
        html.Div([
            html.Div(
                children=[
                    html.H4([
                        "Série Temporal dos Municípios Selecionados",
                        html.Img(
                            id='show-created-modal',
                            src="assets/question-circle-solid.svg",
                            className='info-icon',
                        ),
                    ], className="container_title"),

                    # Radio items para selecionar status

                    dcc.Graph(
                        id='example-graph-2',
                    ),
                ],
                className='six columns pretty_container', id="created-div"
            ),

            html.Div(
                children=[
                    html.H4([
                        "Panorama Confirmado/Recuperados/Óbitos",
                        html.Img(
                            id='show-range-modal',
                            src="assets/question-circle-solid.svg",
                            className='info-icon',
                        ),
                    ], className="container_title"),
                    dcc.Graph(
                        id='example-graph',
                    ),
                ],
                className='six columns pretty_container', id="range-div"
            ),
        ]),

        # Mapa
        html.Div(children=[
            html.Div(children=[
                html.H4([
                    "Mapa",
                    html.Img(
                        id='show-map-modal',
                        src="assets/question-circle-solid.svg",
                        className='info-icon',
                    ),
                ], className="container_title"),
                html.Iframe(id='map', srcDoc=open("MAPA_COVID19.html", 'r').read(), width='100%', height='600'),
            ], className='twelve columns pretty_container',
                style={
                    'float' : 'left',
                    'width': '97%',
                    'margin-right': '0',
                },
                id="map-div"
            ),
        ]),

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
        ])

    ], id="mainContainer", style={"display": "flex", "flex-direction": "column"}
    )
)

# Adiciona e remove os dados de ajuda
for id in ['indicator', 'map', 'range', 'created']:
    @app.callback([Output(f"{id}-modal", 'style'), Output(f"{id}-div", 'style')],
                    [Input(f'show-{id}-modal', 'n_clicks'),
                    Input(f'close-{id}-modal', 'n_clicks')])
    def toggle_modal(n_show, n_close):
        ctx = dash.callback_context
        if ctx.triggered and ctx.triggered[0]['prop_id'].startswith('show-'):
            return {"display": "block"}, {'zIndex': 1003}
        else:
            return {"display": "none"}, {'zIndex': 0}

# Atualiza gráfico de barras
@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'value')])
def update_image_src(selector):
    if len(selector) == 0:
        selector.append('Paraíba')
    data = []
    if selector[0] == "Paraíba":
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['recuperados'],
                     'type': 'bar', 'name': 'Recuperados', 'marker': {"color": 'blue'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['obitos'],
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
    else:
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': city_data[selector[0]]['dias'], 'y': city_data[selector[0]]['obitos'],
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
    figure = {
        'data': data,
        'layout': {
            'height': 350,
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
    [dash.dependencies.Input('Cities', 'value'), dash.dependencies.Input('situacao', 'value')])
def update_image_src(selector, situacao):
    if len(selector) == 0:
        selector.append('Paraíba')
    data = []
    for city in selector:
        data.append({'x': city_data[city]['dias'], 'y': city_data[city][situacao],
                     'type': 'line', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'height': 350,
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
    [Input("aggregate_data", "data"), dash.dependencies.Input('Cities', 'value')],
)
def update_text(data, selector):
    if len(selector) == 0:
        selecionado = 'Paraíba'
    else:
        selecionado = selector[0]
    return (city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['recuperados'][-1] - city_data[selecionado]['obitos'][-1]), \
           city_data[selecionado]['confirmados'][-1], \
           city_data[selecionado]['recuperados'][-1],\
           city_data[selecionado]['obitos'][-1]


if __name__ == '__main__':
    app.run_server()
