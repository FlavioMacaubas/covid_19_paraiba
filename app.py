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
             '04-04-2020', '07-04-2020', '08-04-2020', '13-04-2020',
             '14-04-2020', '15-04-2020', '16-04-2020', '17-04-2020',
             '18-04-2020', '19-04-2020', '20-04-2020', '21-04-2020',
             '22-04-2020', '23-04-2020']

city_data = {
    'Paraíba': {'dias': eixo_dias,
                'confirmados': [17, 20, 28, 30, 34, 41, 55, 136, 152, 165, 195, 205, 236, 245, 263, 301, 345,386],
                'recuperados': [3, 3, 3, 3, 9, 11, 14, 52, 52, 80, 80, 90, 90, 99, 116, 116, 116,116],
                'obitos': [0, 1, 1, 1, 3, 4, 7, 14, 21, 24, 26, 28, 29, 32, 33, 39, 40,44]},

    'João Pessoa': {'dias': eixo_dias,
                    'confirmados': [12, 14, 22, 24, 26, 30, 40, 103, 115, 124, 142, 148, 163, 172, 185, 205, 230,254],
                    'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                    'obitos': [0, 0, 0, 0, 1, 2, 4, 9, 12, 14, 14, 15, 15, 17, 20, 25, 25,28]},
  
    'Campina Grande': {'dias': eixo_dias, 'confirmados': [2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 8, 8, 12, 12, 12, 20, 24,30],
                       'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                       'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2,2]},

    'Santa Rita': {'dias': eixo_dias,
                   'confirmados': [0, 0, 0, 0, 0, 2, 4, 10, 12, 14, 17, 17, 21, 20, 20, 24, 25,25],
                   'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                   'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3,4]},

    'Cabedelo': {'dias': eixo_dias, 'confirmados': [0, 1, 1, 1, 1, 1, 2, 5, 5, 6, 7, 8, 9, 9, 11, 12, 15,15],
                 'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                 'obitos': [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2]},

    'Bayeux': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 6, 6, 8, 8, 9, 9, 10,10],
               'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
               'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,1]},
  
    'Sapé': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 8,10],
             'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
             'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,1]},
  
    'Patos': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 0, 1, 1, 1, 4, 4, 4, 5, 5, 7, 8, 8, 8, 8,8],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
              'obitos': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,2]},
  
    'Cajazeiras': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,4],
                   'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                   'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,1]},
  
    'Sousa': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,4],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
              'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Junco do Seridó': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3],
                        'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                        'obitos': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1]},
  
    'Guarabira': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,3],
                        'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                        'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Igaracy': {'dias': eixo_dias, 'confirmados': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
                'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},


    'Serra Branca': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
                     'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                     'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Taperoá': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
                'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1]},

    'São João do Rio do Peixe': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                 'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                                 'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Pombal': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2],
               'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
               'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Riachão do Poço': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,1],
                        'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                        'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,1]},

    'São Bento': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Congo': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,1],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
              'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Queimadas': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Bom Jesus': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Itabaiana': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,1],
                  'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                  'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Cruz do Espírito Santo': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,1],
                               'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                               'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Conde': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,1],
              'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
              'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Itapororoca': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
                    'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                    'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Barra de São Miguel': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
                            'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                            'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Alagoa Nova': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
                    'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                    'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]},

    'Coremas': {'dias': eixo_dias, 'confirmados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
                'recuperados': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                'obitos': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]}
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
    {'label': 'Queimadas', 'value': 'Queimadas'},
    {'label': 'Bom Jesus', 'value': 'Bom Jesus'},
    {'label': 'Cajazeiras', 'value': 'Cajazeiras'},
    {'label': 'Itabaiana', 'value': 'Itabaiana'},
    {'label': 'Cruz do Espírito Santo', 'value': 'Cruz do Espírito Santo'},
    {'label': 'Conde', 'value': 'Conde'},
    {'label': 'Itapororoca', 'value': 'Itapororoca'},
    {'label': 'Barra de São Miguel', 'value': 'Barra de São Miguel'},
    {'label': 'Alagoa Nova', 'value': 'Alagoa Nova'},
    {'label': 'Coremas', 'value': 'Coremas'},
    {'label': 'Guarabira', 'value': 'Guarabira'},
]


## Preparação Brasil - Começo ##
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv', error_bad_lines = False)

estados_br = [
    {'label':'Brasil', 'value':'BR'},
    {'label': 'São Paulo', 'value': 'SP'},
    {'label': 'Rio de Janeiro', 'value': 'RJ'},
    {'label': 'Paraíba', 'value': 'PB'},
    {'label': 'Acre', 'value': 'AC'},
    {'label': 'Alagoas', 'value': 'AL'},
    {'label': 'Amapá', 'value': 'AP'},
    {'label': 'Amazonas', 'value': 'AM'},
    {'label': 'Bahia', 'value': 'BA'},
    {'label': 'Ceará', 'value': 'CE'},
    {'label': 'Distrito Federal', 'value': 'DF'},
    {'label': 'Espírito Santo', 'value': 'ES'},
    {'label': 'Goiás', 'value': 'GO'},
    {'label': 'Maranhão', 'value': 'MA'},
    {'label': 'Mato Grosso', 'value': 'MT'},
    {'label': 'Mato Grosso do Sul', 'value': 'MS'},
    {'label': 'Minas Gerais', 'value': 'MG'},
    {'label': 'Pará', 'value': 'PA'},
    {'label': 'Paraná', 'value': 'PR'},
    {'label': 'Pernambuco', 'value': 'PE'},
    {'label': 'Piauí', 'value': 'PI'},
    {'label': 'Rio Grande do Norte', 'value': 'RN'},
    {'label': 'Rio Grande do Sul', 'value': 'RS'},
    {'label': 'Rondônia', 'value': 'RO'},
    {'label': 'Roraima', 'value': 'RR'},
    {'label': 'Santa Catarina', 'value': 'SC'},
    {'label': 'Sergipe', 'value': 'SE'},
    {'label': 'Tocatins', 'value': 'TO'},
]
## Preparação Brasil - Fim ##

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

        build_modal_info_overlay('map', 'bottom', dedent("""
    O _**Mapa**_ destaca os municípios que tiveram casos confirmados de covid-19 no estado
    da Paraíba. Ao clicar em um território, você pode visualizar informações detalhadas da região. 
    Os mapas são organizados pela paleta entre amarelo de vermelho, quanto mais vermelho, mais casos relativamente ao total
    de casos no estado, quanto mais amarelo, menos caso relativo a quantidade total de casos do estado.
    """)),
        build_modal_info_overlay('range', 'top', dedent("""
    O _**Panorama Confirmados/Recuperados/Óbitos**_ mostra a quantidade de cada um desses campos no decorrer
    dos dias no estado. Facilita a interpretação da proporção de óbitos e recuperação em relação ao total.

    O campo mostrará a primeira opção selecionada no _**Escolha de Cidades**_.
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
                        src="assets/logo_nova-removebg.png",
                        style={'float': 'right', 'height': '150px'}
                    ),

                    href="https://www.instagram.com/labimec/"),
            ], style={'text-align': 'left'}),

            html.H6(children=[
                'Laboratório de Inteligência Artificial e Macroeconomia Computacional - LABIMEC',
            ], style={'text-align': 'left'}),

        ]),

        dcc.Markdown(children=
                     ''' > Atualização Covid-19 22/04 às 20h. Para melhor experiência acesse pelo computador.
        '''),
        dcc.Markdown(children=
                     ''' > Fonte dados do Brasil: https://github.com/wcota/covid19br (dados oficiais do Ministério da Saúde).
        '''),

        dcc.Tabs([
            ###### TAB PARAÍBA COMEÇA AQUI ##############
            dcc.Tab(label="Paraíba", children=[

                # Containers para mostrar os valores
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H4([
                                                    "Escolha as cidades que deseja:",
                                                ]),

                                                dcc.Dropdown(
                                                    id='cidades_menu',
                                                    options=cidades_pb,
                                                    value='Paraíba',
                                                    className="dcc_control",
                                                )

                                            ], className='mini_container'),

                                        html.Div(
                                            [
                                                html.H4(id="well_text", style={'text-align': 'center'}),
                                                html.P(id="well_perc", style={'text-align': 'center'}),
                                                html.P("Ativos", style={'text-align': 'center'})
                                            ],
                                            id="wells",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="gasText", style={'text-align': 'center'}),
                                             html.P(id="gas_perc", style={'text-align': 'center'}),
                                             html.P("Confirmados", style={'text-align': 'center'})],
                                            id="gas",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="oilText", style={'text-align': 'center'}),
                                             html.P(id="oil_perc", style={'text-align': 'center'}),
                                             html.P("Recuperados", style={'text-align': 'center'})],
                                            id="oil",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="waterText", style={'text-align': 'center'}),
                                             html.P(id="water_perc", style={'text-align': 'center'}),
                                             html.P("Óbitos", style={'text-align': 'center'})],
                                            id="water",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="mortalidadeText", style={'text-align': 'center'}),
                                             html.P(id="mortalidade_perc", style={'text-align': 'center'}),
                                             html.P("Mortalidade", style={'text-align': 'center'})],
                                            id="mortalidade",
                                            className="mini_container",
                                        ),

                                        html.Div(
                                            [html.H4(id="recuperacaoText", style={'text-align': 'center'}),
                                             html.P(id="recuperacao_perc", style={'text-align': 'center'}),
                                             html.P("Recuperação", style={'text-align': 'center'})],
                                            id="recuperacao",
                                            className="mini_container",
                                        ),

                                    ],
                                    id="info-container",
                                    className="row container-display",
                                ),

                            ],
                            id="right-column",
                            className="twelve columns",
                        ),
                    ],
                    className="twelve columns row flex-display",
                    style={"zIndex": 1}
                ),

                # Mapa
                html.Div(children=[
                    dcc.Tabs([
                        dcc.Tab(label="Confirmados", children=[
                            html.Div(children=[
                                html.H4([
                                    "Mapa",
                                    html.Img(
                                        id='show-map-modal',
                                        src="assets/question-circle-solid.svg",
                                        className='info-icon',
                                    ),
                                ], className="container_title"),
                                html.Iframe(id='map', srcDoc=open("MAPA_COVID19.html", 'r').read(), width='100%',
                                            height=600),
                            ], className='nine columns pretty_container',
                                style={
                                    'float': 'left',
                                    'width': '97%',
                                    'height': '100%',
                                    'margin-right': '0',
                                },
                                id="map-div"
                            ),

                            html.Div([
                                html.H4(["Total de Casos Confirmados"], style={'text-align': 'center'}),
                                html.H3([city_data['Paraíba']['confirmados'][-1]], id='total_casos',
                                        style={'text-align': 'center',
                                               'color': 'crimson',
                                               'margin-top': 2,
                                               'height': "20%"}),
                            ], className="three columns pretty_container"),

                            html.Div([
                                html.Div([
                                    html.Strong([city_data['João Pessoa']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("João Pessoa", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Santa Rita']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Santa Rita", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Campina Grande']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Campina Grande", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Cabedelo']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Cabedelo", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Bayeux']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Bayeux", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Patos']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Patos", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Sapé']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Sapé", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Junco do Seridó']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Junco do Seridó", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Cajazeiras']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Cajazeiras", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Pombal']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Pombal", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Sousa']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Sousa", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Igaracy']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Igaracy", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Queimadas']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Queimadas", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Congo']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Congo", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['São Bento']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("São Bento", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['São João do Rio do Peixe']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("São João do Rio do Peixe", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Taperoá']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Taperoá", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Riachão do Poço']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Riachão do Povo", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Bom Jesus']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Bom Jesus", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Itabaiana']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Itabaiana", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Cruz do Espírito Santo']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Cruz do Espírito Santo", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([city_data['Conde']['confirmados'][-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Conde", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                ], className="control-tab"),

                            ], className="three columns pretty_container",
                                style={"overflowX": "scroll", 'text-align': 'left', 'height': 500}),
                        ]),

                    ], className='custom-tab'),

                ], className='twelve columns pretty_container'),

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

                            html.H6([
                                "Escolha as cidades que deseja:",
                            ]),

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

                            # Radio items para selecionar status

                            dcc.Graph(
                                id='example-graph-2',
                            ),
                        ],
                        className='twelve columns pretty_container', id="created-div"
                    ),

                    html.Div(
                        children=[
                            html.H4([
                                "Panorama Confirmados/Recuperados/Óbitos",
                                html.Img(
                                    id='show-range-modal',
                                    src="assets/question-circle-solid.svg",
                                    className='info-icon',
                                ),
                            ], className="container_title"),

                            html.P("Selecione seu município"),
                            dcc.Dropdown(
                                id='cidades',
                                options=cidades_pb,
                                value='Paraíba',
                                multi=False,
                                className="dcc_control",
                            ),

                            dcc.Graph(
                                id='example-graph',
                            ),
                        ],
                        className='twelve columns pretty_container', id="range-div"
                    ),
                ]),

            ]),
            ###### TAB PARAÍBA ACABA AQUI ###############

            ###### TAB BRASIL COMEÇA AQUI ###############
            dcc.Tab(label='Brasil', children=[
                # Containers Brasil
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H4([
                                                    "Escolha o estado:",
                                                ]),

                                                dcc.Dropdown(
                                                    id='estados_menu',
                                                    options=estados_br,
                                                    value='BR',
                                                    className="dcc_control",
                                                )

                                            ], className='mini_container'),

                                        html.Div(
                                            [
                                                html.H4(id="well_text_br", style={'text-align': 'center'}),
                                                html.P(id="well_perc_br", style={'text-align': 'center'}),
                                                html.P("Ativos", style={'text-align': 'center'})
                                            ],
                                            id="wells_br",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="gasText_br", style={'text-align': 'center'}),
                                             html.P(id="gas_perc_br", style={'text-align': 'center'}),
                                             html.P("Confirmados", style={'text-align': 'center'})],
                                            id="gas_br",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="oilText_br", style={'text-align': 'center'}),
                                             html.P(id="oil_perc_br", style={'text-align': 'center'}),
                                             html.P("Recuperados*", style={'text-align': 'center'})],
                                            id="oil_br",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="waterText_br", style={'text-align': 'center'}),
                                             html.P(id="water_perc_br", style={'text-align': 'center'}),
                                             html.P("Óbitos", style={'text-align': 'center'})],
                                            id="water_br",
                                            className="mini_container",
                                        ),
                                        html.Div(
                                            [html.H4(id="mortalidadeText_br", style={'text-align': 'center'}),
                                             html.P(id="mortalidade_perc_br", style={'text-align': 'center'}),
                                             html.P("Mortalidade", style={'text-align': 'center'})],
                                            id="mortalidade_br",
                                            className="mini_container",
                                        ),

                                        html.Div(
                                            [html.H4(id="recuperacaoText_br", style={'text-align': 'center'}),
                                             html.P(id="recuperacao_perc_br", style={'text-align': 'center'}),
                                             html.P("Recuperação*", style={'text-align': 'center'})],
                                            id="recuperacao_br",
                                            className="mini_container",
                                        ),

                                    ],
                                    id="info-container-br",
                                    className="row container-display",
                                ),

                            ],
                            id="right-column-br",
                            className="twelve columns",
                        ),
                    ],
                    className="twelve columns row flex-display",
                    style={"zIndex": 1}
                ),


                # Mapa Brasil
                # Mapa
                html.Div(children=[
                    dcc.Tabs([
                        dcc.Tab(label="Confirmados", children=[
                            html.Div(children=[
                                html.H4([
                                    "Mapa",
                                ], className="container_title"),
                                html.Iframe(id='map_br', srcDoc=open("MAPA_COVID19_BR.html", 'r').read(), width='100%',
                                            height=600),
                            ], className='nine columns pretty_container',
                                style={
                                    'float': 'left',
                                    'width': '75%',
                                    'height': '100%',
                                    'margin-right': '0',
                                },
                                id="map-div-br"
                            ),

                            html.Div([
                                html.H4(["Total de Casos Confirmados"], style={'text-align': 'center'}),
                                html.H3([df.loc[df['state'] == 'TOTAL']['totalCasesMS'].values[-1]], id='total_casos_br',
                                        style={'text-align': 'center',
                                               'color': 'crimson',
                                               'margin-top': 2,
                                               'height': "20%"}),
                            ], className="three columns pretty_container"),

                            html.Div([
                                html.Div([
                                    html.Strong([df.loc[df['state'] == 'SP']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("São Paulo", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'RJ']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Rio de Janeiro", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'CE']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Ceará", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'PE']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Pernambuco", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'BA']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Bahia", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'MA']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Maranhão", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'ES']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Espírito Santo", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'MG']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Minas Gerais", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'PA']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Pará", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'SC']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Santa Catarina", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'PR']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Paraná", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'RS']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Rio Grande do Sul", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'DF']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Distrito Federal", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'RN']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Rio Grande do Norte", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'AP']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Amapá", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'GO']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Goiás", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'PB']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Paraíba", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'AL']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Alagoas", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'RR']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Roraima", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'RO']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Rondônia", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'AC']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Acre", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'MT']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Mato Grosso", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'PI']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Piauí", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'MS']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Mato Grosso do Sul", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'SE']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Sergipe", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                    html.Strong([df.loc[df['state'] == 'TO']['totalCasesMS'].values[-1]],
                                                style={'color': 'crimson', 'font-size': 20}),
                                    html.Span(" "),
                                    html.Span("Tocantins", style={'font-size': 20}),
                                    html.Hr(style={'margin': 0}),

                                ], className="control-tab"),

                            ], className="three columns pretty_container",
                                style={"overflowX": "scroll", 'text-align': 'left', 'height': 500}),
                        ]),

                    ], className='custom-tab'),

                ], className='twelve columns pretty_container'),

                # Gráficos
                html.Div([
                    html.Div(
                        children=[
                            html.H4([
                                "Série Temporal dos Estados Selecionados",
                            ], className="container_title"),

                            html.H6([
                                "Escolha os estados que deseja:",
                            ]),

                            dcc.Dropdown(
                                id='Estados',
                                options=estados_br,
                                value=['BR','SP','PB'],
                                multi=True,
                                className="dcc_control",
                            ),

                            html.P('Filtrar dados por:'),
                            dcc.RadioItems(
                                id="situacao_br",
                                options=[
                                    {"label": "Confirmados", "value": "totalCasesMS"},
                                    {"label": "Óbitos", "value": "deathsMS"},
                                ],
                                value="totalCasesMS",
                                labelStyle={"display": "inline-block"},
                                className="dcc_control",
                            ),

                            # Radio items para selecionar status

                            dcc.Graph(
                                id='brasil-grafico-1',
                            ),
                        ],
                        className='twelve columns pretty_container', id="created-div-2"
                    ),

                    html.Div(
                        children=[
                            html.H4([
                                "Panorama Confirmados/Recuperados/Óbitos",
                            ], className="container_title"),

                            html.P("Selecione seu município"),
                            dcc.Dropdown(
                                id='estados',
                                options=estados_br,
                                value='BR',
                                multi=False,
                                className="dcc_control",
                            ),

                            dcc.Graph(
                                id='brasil-grafico-2',
                            ),
                        ],
                        className='twelve columns pretty_container', id="range-div-2"
                    ),
                ]),
            ]),
        ], className = 'twelve columns'),

        # Notas de roda pé
    html.Div([
            dcc.Markdown(
                children='''
    ¹ O Dashboard apresentado trata-se de uma iniciativa do Laboratório da Inteligência Artificial e Macroeconomia Computacional (LABIMEC), 
     ainda em versão de testes. O propósito é facilitar a visualização dos casos de coronavírus no estado da Paraíba e em seus municípios. Futuras funcionalidades
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
    '''),

        dcc.Markdown(
            children='''
        * Não há dados de recuperados na base de dados para o Brasil que estamos utilizando.
        ''')
        ]),


    ], id="mainContainer", style={"display": "flex", "flex-direction": "column"}
    )
)

# Adiciona e remove os dados de ajuda
for id in ['map', 'range', 'created']:
    @app.callback([Output(f"{id}-modal", 'style'), Output(f"{id}-div", 'style')],
                  [Input(f'show-{id}-modal', 'n_clicks'),
                   Input(f'close-{id}-modal', 'n_clicks')])
    def toggle_modal(n_show, n_close):
        ctx = dash.callback_context
        if ctx.triggered and ctx.triggered[0]['prop_id'].startswith('show-'):
            return {"display": "block"}, {'zIndex': 1003}
        else:
            return {"display": "none"}, {'zIndex': 0}


# Atualiza gráfico de barras Brasil
@app.callback(
    dash.dependencies.Output('brasil-grafico-2', 'figure'),
    [dash.dependencies.Input('estados', 'value')])
def update_image_src(selector):
    if len(selector) == 0:
        selector = 'SP'
    data = []

    if selector == 'BR':
        data.append(
            {'x': df.loc[df['state'] == 'TOTAL']['date'], 'y': df.loc[df['state'] == 'TOTAL']['totalCasesMS'].values,
             'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append(
            {'x': df.loc[df['state'] == 'TOTAL']['date'], 'y': df.loc[df['state'] == 'TOTAL']['deathsMS'].values,
             'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
    else:
        data.append({'x': df.loc[df['state']==selector]['date'], 'y': df.loc[df['state']==selector]['totalCasesMS'].values,
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': df.loc[df['state']==selector]['date'], 'y': df.loc[df['state']==selector]['deathsMS'].values,
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})

    figure = {
        'data': data,
        'layout': {
            'height': 450,
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
                )),
            'barmode': 'group',
            'bargap': 0.2,
            'bargroupgap': 0.15,
        }
    }
    return figure

# Atualiza gráfico de linha Brasil
@app.callback(
    dash.dependencies.Output('brasil-grafico-1', 'figure'),
    [dash.dependencies.Input('Estados', 'value'), dash.dependencies.Input('situacao_br', 'value')])
def update_image_src(selector, situacao):
    if len(selector) == 0:
        selector.append('SP')
    data = []
    for estado in selector:
        if estado == 'BR':
            data.append({'x': list(df[df['state'] == 'TOTAL']['date']), 'y': df[df['state'] == 'TOTAL'][situacao].values,
                     'type': 'line', 'name': estado})
        else:
            data.append({'x': list(df[df['state'] == estado]['date']), 'y': df[df['state'] == estado][situacao].values,
                     'type': 'line', 'name': estado})
    figure = {
        'data': data,
        'layout': {
            'height': 450,
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


# Atualiza gráfico de barras Paraíba
@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('cidades', 'value')])
def update_image_src(selector):
    if len(selector) == 0:
        selector = 'Paraíba'
    data = []

    if selector == "Paraíba":
        data.append({'x': city_data[selector]['dias'], 'y': city_data[selector]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': city_data[selector]['dias'], 'y': city_data[selector]['recuperados'],
                     'type': 'bar', 'name': 'Recuperados', 'marker': {"color": 'blue'}})
        data.append({'x': city_data[selector]['dias'], 'y': city_data[selector]['obitos'],
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'orange'}})
    else:
        data.append({'x': city_data[selector]['dias'], 'y': city_data[selector]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': city_data[selector]['dias'], 'y': city_data[selector]['obitos'],
                     'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'orange'}})
    figure = {
        'data': data,
        'layout': {
            'height': 450,
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
                )),
            'barmode': 'group',
            'bargap': 0.2,
            'bargroupgap': 0.15,
        }
    }
    return figure


# Atualiza gráfico de linha Paraíba
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
            'height': 450,
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


# Menus Paraiba
@app.callback(
    [
        Output("well_text", "children"),
        Output("well_perc", "children"),
        Output("gasText", "children"),
        Output("gas_perc", "children"),
        Output("oilText", "children"),
        Output("oil_perc", "children"),
        Output("waterText", "children"),
        Output("water_perc", "children"),
        Output("mortalidadeText", "children"),
        Output("mortalidade_perc", "children"),
        Output("recuperacaoText", "children"),
        Output("recuperacao_perc", "children"),
    ],
    [Input("aggregate_data", "data"), dash.dependencies.Input('cidades_menu', 'value')],
)
def update_text(data, selector):

    def formata_saida(valor):
        if valor > 0:
            return "▲ {:.1f}%".format(valor)
        elif valor == 0:
            return "{:.1f}%".format(valor)
        else:
            return "▼ {:.1f}%".format(valor)

    if len(selector) == 0:
        selecionado = 'Paraíba'
    else:
        selecionado = selector

    # Preparando dados
    #ativos
    ativos_inicial = (city_data[selecionado]['confirmados'][-2] - city_data[selecionado]['recuperados'][-2] -
            city_data[selecionado]['obitos'][-2])

    if ativos_inicial <= 0:
        ativos_inicial = 1

    #confirmados
    confirmados_inicial = city_data[selecionado]['confirmados'][-2]

    if confirmados_inicial <= 0:
        confirmados_inicial = 1

    #recuperados
    recuperados_inicial = city_data[selecionado]['recuperados'][-2]

    if recuperados_inicial <= 0:
        recuperados_inicial = 1

    #obitos
    obitos_inicial = city_data[selecionado]['obitos'][-2]

    if obitos_inicial <= 0:
        obitos_inicial = 1

    # Mortalidade e Recuperacao
    confirmados_final = city_data[selecionado]['confirmados'][-1]
    confirmados_passado = city_data[selecionado]['confirmados'][-2]

    if confirmados_final == 0:
        confirmados_final = 1

    if confirmados_passado == 0:
        confirmados_passado = 1

    mortalidade_atual = ( city_data[selecionado]['obitos'][-1]/confirmados_final ) * 100
    mortalidade_passado = ( city_data[selecionado]['obitos'][-2]/confirmados_passado ) * 100

    if mortalidade_passado == 1:
        mortalidade_passado = 0

    variacao_mortalidade =  ( mortalidade_atual - (( city_data[selecionado]['obitos'][-2]/confirmados_passado ) * 100))* 100 / mortalidade_passado

    recuperacao_atual = ( city_data[selecionado]['recuperados'][-1]/confirmados_final ) * 100
    recuperacao_passado = (city_data[selecionado]['recuperados'][-2]/confirmados_passado) * 100

    if recuperacao_passado == 0:
        recuperacao_passado = 1

    variacao_recuperacao = (recuperacao_atual - ((city_data[selecionado]['recuperados'][-2]/confirmados_passado) * 100)) * 100     / recuperacao_passado

    # Dados de sáida

    ativos = (city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['recuperados'][-1] -
            city_data[selecionado]['obitos'][-1])

    novos_ativos = ( (city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['recuperados'][-1] -
            city_data[selecionado]['obitos'][-1]) - (city_data[selecionado]['confirmados'][-2] - city_data[selecionado]['recuperados'][-2] -
            city_data[selecionado]['obitos'][-2]) ) * 100/ ativos_inicial


    novos_confirmados = ( city_data[selecionado]['confirmados'][-1] - city_data[selecionado]['confirmados'][-2] ) * 100 / confirmados_inicial

    novos_recuperados = ( city_data[selecionado]['recuperados'][-1] - city_data[selecionado]['recuperados'][-2] ) * 100 / recuperados_inicial

    novos_obitos = ( city_data[selecionado]['obitos'][-1] - city_data[selecionado]['obitos'][-2] ) * 100 / obitos_inicial



    return "{}".format(ativos), \
           formata_saida(novos_ativos), \
           "{}".format(city_data[selecionado]['confirmados'][-1]), \
           formata_saida(novos_confirmados), \
           "{}".format(city_data[selecionado]['recuperados'][-1]), \
           formata_saida(novos_recuperados), \
           "{}".format(city_data[selecionado]['obitos'][-1]), \
           formata_saida(novos_obitos), \
           "{:.1f}%".format(mortalidade_atual), \
           formata_saida(variacao_mortalidade), \
           "{:.1f}%".format(recuperacao_atual), \
            formata_saida(variacao_recuperacao)


@app.callback(
    [
        Output('well_perc', 'style'),
        Output('gas_perc', 'style'),
        Output('oil_perc', 'style'),
        Output('water_perc', 'style'),
        Output('mortalidade_perc', 'style'),
        Output('recuperacao_perc', 'style'),
    ],
    [
        Input("well_perc", "children"),
        Input("gas_perc", "children"),
        Input("oil_perc", "children"),
        Input("water_perc", "children"),
        Input("mortalidade_perc", "children"),
        Input("recuperacao_perc", "children"),
    ])
def atualiza_style(valor_well, valor_gas, valor_oil, valor_water, valor_mortalidade, valor_recuperacao):
    lista_styles=[]
    for valores in [valor_well,valor_gas,valor_oil,valor_water, valor_mortalidade, valor_recuperacao]:
        if "▲" in valores:
            lista_styles.append({'text-align': 'center', 'color':'green'})
        elif "▼" in valores:
            lista_styles.append({'text-align': 'center', 'color':'red'})
        else:
            lista_styles.append({'text-align': 'center', 'color':'black'})

    return lista_styles[0], lista_styles[1], lista_styles[2], lista_styles[3], lista_styles[4], lista_styles[5]

# Menus Brasil
@app.callback(
    [
        Output("well_text_br", "children"),
        Output("well_perc_br", "children"),
        Output("gasText_br", "children"),
        Output("gas_perc_br", "children"),
        Output("oilText_br", "children"),
        Output("oil_perc_br", "children"),
        Output("waterText_br", "children"),
        Output("water_perc_br", "children"),
        Output("mortalidadeText_br", "children"),
        Output("mortalidade_perc_br", "children"),
        Output("recuperacaoText_br", "children"),
        Output("recuperacao_perc_br", "children"),
    ],
    [Input("aggregate_data", "data"), dash.dependencies.Input('estados_menu', 'value')],
)
def update_text(data, selector):

    def formata_saida(valor):
        if valor > 0:
            return "▲ {:.1f}%".format(valor)
        elif valor == 0:
            return "{:.1f}%".format(valor)
        else:
            return "▼ {:.1f}%".format(valor)

    if len(selector) == 0 or (selector == 'BR'):
        selecionado = 'TOTAL'
    else:
        selecionado = selector

    #ATIVOS
    ativos_inicial = df.loc[df['state'] == selecionado]['totalCases'].values[-2] - \
                     df.loc[df['state'] == selecionado]['deathsMS'].values[-2]

    ativos_final = df.loc[df['state'] == selecionado]['totalCases'].values[-1] - \
                     df.loc[df['state'] == selecionado]['deathsMS'].values[-1]

    if ativos_inicial == 0:
        ativos_inicial = 1

    variacao_ativos = (ativos_final - (df.loc[df['state'] == selecionado]['totalCases'].values[-2] - \
                     df.loc[df['state'] == selecionado]['deathsMS'].values[-2])) * 100 / ativos_inicial

    #CONFIRMADOS
    confirmado_inicial = df.loc[df['state'] == selecionado]['totalCasesMS'].values[-2]
    confirmado_final = df.loc[df['state'] == selecionado]['totalCasesMS'].values[-1]

    if confirmado_inicial == 0:
        confirmado_inicial = 1

    variacao_confirmados = (confirmado_final - df.loc[df['state'] == selecionado]['totalCasesMS'].values[-2])*100/confirmado_inicial

    #OBITOS
    obitos_inicial = df.loc[df['state'] == selecionado]['deathsMS'].values[-2]
    obitos_final =  df.loc[df['state'] == selecionado]['deathsMS'].values[-1]

    if obitos_inicial == 0:
        obitos_final = 1

    variacao_obitos = (obitos_final - df.loc[df['state'] == selecionado]['deathsMS'].values[-2])*100/obitos_inicial

    #MORTALIDADE
    mortalidade_inicial = obitos_inicial * 100/confirmado_inicial
    mortalidade_final = obitos_final * 100 / confirmado_final

    if mortalidade_inicial == 0:
        mortalidade_inicial = 1

    variacao_mortalidade = (mortalidade_final - mortalidade_inicial)*100/mortalidade_inicial

    return "{}".format(ativos_final), \
           formata_saida(variacao_ativos), \
           "{}".format(confirmado_final), \
           formata_saida(variacao_confirmados), \
           "{}".format(0), \
           formata_saida(0), \
           "{}".format(obitos_final), \
           formata_saida(variacao_obitos), \
           "{:.1f}%".format(mortalidade_final), \
           formata_saida(variacao_mortalidade), \
           "{:.1f}%".format(0), \
            formata_saida(0)


@app.callback(
    [
        Output('well_perc_br', 'style'),
        Output('gas_perc_br', 'style'),
        Output('oil_perc_br', 'style'),
        Output('water_perc_br', 'style'),
        Output('mortalidade_perc_br', 'style'),
        Output('recuperacao_perc_br', 'style'),
    ],
    [
        Input("well_perc_br", "children"),
        Input("gas_perc_br", "children"),
        Input("oil_perc_br", "children"),
        Input("water_perc_br", "children"),
        Input("mortalidade_perc_br", "children"),
        Input("recuperacao_perc_br", "children"),
    ])
def atualiza_style(valor_well, valor_gas, valor_oil, valor_water, valor_mortalidade, valor_recuperacao):
    lista_styles=[]
    for valores in [valor_well,valor_gas,valor_oil,valor_water, valor_mortalidade, valor_recuperacao]:
        if "▲" in valores:
            lista_styles.append({'text-align': 'center', 'color':'green'})
        elif "▼" in valores:
            lista_styles.append({'text-align': 'center', 'color':'red'})
        else:
            lista_styles.append({'text-align': 'center', 'color':'black'})

    return lista_styles[0], lista_styles[1], lista_styles[2], lista_styles[3], lista_styles[4], lista_styles[5]
  
if __name__ == '__main__':
    app.run_server()
