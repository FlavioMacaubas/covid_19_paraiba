# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
from textwrap import dedent


app = dash.Dash(__name__)
server = app.server

app.title = "Covid-19 PB-BR"

## Preparação Paraíba - Começo ##
df_pb = pd.read_csv("https://raw.githubusercontent.com/FlavioMacaubas/covid_19_paraiba/master/base_dados.csv",
                    error_bad_lines=False)

cidades_pb = []
for cidade in df_pb['cidade'].unique():
    dic_aux = {'label': cidade, 'value': cidade}
    cidades_pb.append(dic_aux)

## Preparação Paraíba - Fim ##

## Preparação Brasil - Começo ##
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv',
                 error_bad_lines=False)

estados_br = [
    {'label': 'Brasil', 'value': 'BR'},
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
    {'label': 'Tocantins', 'value': 'TO'},
]

## Preparação Brasil - Fim ##

## Preenchendo os maiores - PB (COMEÇO) ##
total_casos = []
total_mortes = []
cidades = []

for cidade in df_pb['cidade'].unique():
    cidades.append(cidade)
    total_casos.append(df_pb.loc[df_pb['cidade'] == cidade]['confirmados'].values[-1])
    total_mortes.append(df_pb.loc[df_pb['cidade'] == cidade]['obitos'].values[-1])

base_dados_pb = pd.DataFrame({'cidade': cidades, 'confirmados': total_casos, 'obitos': total_mortes})
base_dados_pb = base_dados_pb.loc[base_dados_pb['cidade'] != 'Paraíba']
base_dados_pb = base_dados_pb.loc[base_dados_pb['confirmados'] > 0]

lista_maiores_pb = []

for cidade in base_dados_pb.sort_values('confirmados', ascending=False)['cidade']:
    div = html.Strong([base_dados_pb.loc[base_dados_pb['cidade'] == cidade][
                           'confirmados'].values[-1]],
                      style={'color': 'crimson', 'font-size': 20}), html.Span(" "), html.Span(cidade, style={
        'font-size': 20}), html.Hr(style={'margin': 0})

    # É muito importante usar extend nesse contexto, porque append irá criar uma lista de listas.
    lista_maiores_pb.extend(div)

base_dados_pb_o = base_dados_pb.loc[base_dados_pb['obitos'] != 0]
maiores_obitos_pb = []
for cidade in base_dados_pb_o.sort_values('obitos', ascending=False)['cidade']:
    div = html.Strong([base_dados_pb.loc[base_dados_pb['cidade'] == cidade]['obitos'].values[-1]],
                      style={'color': '#420881', 'font-size': 20}), \
          html.Span(" "), \
          html.Span(cidade, style={'font-size': 20}), \
          html.Hr(style={'margin': 0})

    # É muito importante usar extend nesse contexto, porque append irá criar uma lista de listas.
    maiores_obitos_pb.extend(div)
## Preenchendo os maiores - PB (FIM) ##

### Preenchendo os maiores - BR (COMEÇO) ###
sigla_estados_br = {'SP': 'São Paulo',
                    'RJ': 'Rio de Janeiro',
                    'PB': 'Paraíba',
                    'AC': 'Acre',
                    'AL': 'Alagoas',
                    'AP': 'Amapá',
                    'AM': 'Amazonas',
                    'BA': 'Bahia',
                    'CE': 'Ceará',
                    'DF': 'Distrito Federal',
                    'ES': 'Espírito Santo',
                    'GO': 'Goiás',
                    'MA': 'Maranhão',
                    'MT': 'Mato Grosso',
                    'MS': 'Mato Grosso do Sul',
                    'MG': 'Minas Gerais',
                    'PA': 'Pará',
                    'PR': 'Paraná',
                    'PE': 'Pernambuco',
                    'PI': 'Piauí',
                    'RN': 'Rio Grande do Norte',
                    'RS': 'Rio Grande do Sul',
                    'RO': 'Rondônia',
                    'RR': 'Roraima',
                    'SC': 'Santa Catarina',
                    'SE': 'Sergipe',
                    'TO': 'Tocantins'}
total_casos = []
total_mortes = []
estados = []

for estado in df['state'].unique():
    estados.append(estado)
    total_casos.append(df.loc[df['state'] == estado]['totalCasesMS'].values[-1])
    total_mortes.append(df.loc[df['state'] == estado]['deathsMS'].values[-1])

base_dados_br = pd.DataFrame({'estado': estados, 'confirmados': total_casos, 'obitos': total_mortes})
base_dados_br = base_dados_br.loc[base_dados_br['estado'] != 'TOTAL']

lista_maiores_br = []
for estado in base_dados_br.sort_values('confirmados', ascending=False)['estado']:
    div = html.Strong([base_dados_br.loc[base_dados_br['estado'] == estado]['confirmados'].values[-1]],
                      style={'color': 'crimson', 'font-size': 20}), \
          html.Span(" "), \
          html.Span(sigla_estados_br[estado], style={'font-size': 20}), \
          html.Hr(style={'margin': 0})

    # É muito importante usar extend nesse contexto, porque append irá criar uma lista de listas.
    lista_maiores_br.extend(div)

maiores_obitos_br = []

base_dados_br_o = base_dados_br.loc[base_dados_br['obitos'] != 0]

for estado in base_dados_br_o.sort_values('obitos', ascending=False)['estado']:
    div = html.Strong([base_dados_br_o.loc[base_dados_br_o['estado'] == estado]['obitos'].values[-1]],
                      style={'color': '#420881', 'font-size': 20}), \
          html.Span(" "), \
          html.Span(sigla_estados_br[estado], style={'font-size': 20}), \
          html.Hr(style={'margin': 0})

    # É muito importante usar extend nesse contexto, porque append irá criar uma lista de listas.
    maiores_obitos_br.extend(div)


### Preenchendo maiores - BR (FIM) ###

# Menus explicações
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
                'Covid-19 (PB - BR)',
                html.A(
                    html.Img(
                        src="assets/logo_nova-removebg.png",
                        style={'float': 'right', 'height': '120px', 'display': 'inline'}
                    ),

                    href="https://www.instagram.com/labimec/"),

                html.A(
                    html.Img(
                        src="assets/fapesq_logo.png",
                        style={'float': 'right', 'height': '120px', 'display': 'inline'}
                    ),

                    href="http://fapesq.rpp.br/"),

                html.A(
                    html.Img(
                        src="assets/selo_DPE.png",
                        style={'float': 'right', 'height': '100px', 'display': 'inline', 'margin-top': 20}
                    ),

                    href="https://defensoria.pb.def.br/noticias.php?idcat=1&id=2342"),

            ], style={'text-align': 'left'}),

            html.H6(children=[
                'Laboratório de Inteligência Artificial e Macroeconomia Computacional - LABIMEC',

            ], style={'text-align': 'left'}),

        ], className='banner'),

        dcc.Markdown(children=
                     ''' > Atualização Covid-19 22/08 às 20:00h. Para melhor experiência acesse pelo computador.
        '''),

        dcc.Tabs([
            ###### TAB PARAÍBA COMEÇA AQUI ##############
            dcc.Tab(label="Paraíba", children=[

                # Containers para mostrar os valores
                html.Div(
                    [
                        html.Div(
                            [

                                html.H4([
                                    "Escolha a cidade:",
                                ]),

                                dcc.Dropdown(
                                    id='cidades_menu',
                                    options=cidades_pb,
                                    value='Paraíba',
                                    className="dcc_control",
                                ),

                                html.Div(
                                    [

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
                                             html.P("Letalidade", style={'text-align': 'center'})],
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
                        # MAPA TAB DE CONFIRMADOS
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
                                            height=620),
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
                                html.H3([df_pb.loc[df_pb['cidade'] == 'Paraíba']['confirmados'].values[-1]],
                                        id='total_casos',
                                        style={'text-align': 'center',
                                               'color': 'crimson',
                                               'margin-top': 2,
                                               'height': "20%"}),
                                html.P([str(len(base_dados_pb)) + " dos 223 municípios " + "({:.1f}%)".format(
                                    len(base_dados_pb) * 100 / 223)], style={'text-align': 'center'})
                            ], className="three columns pretty_container"),

                            html.Div([
                                html.Div(children=lista_maiores_pb, className="control-tab"),

                            ], className="three columns pretty_container",
                                style={"overflowX": "scroll", 'text-align': 'left', 'height': 500}),
                        ]),

                        # MAPA TAB DE ÓBITOS
                        dcc.Tab(label='Óbitos', children=[
                            html.Div(children=[
                                html.H4([
                                    "Mapa",
                                ], className="container_title"),
                                html.Iframe(id='map_pb_o', srcDoc=open("MAPA_COVID19_OBITOS.html", 'r').read(),
                                            width='100%',
                                            height=620),
                            ], className='nine columns pretty_container',
                                style={
                                    'float': 'left',
                                    'width': '75%',
                                    'height': '100%',
                                    'margin-right': '0',
                                },
                                id="map-div-pb-o"
                            ),

                            html.Div([
                                html.H4(["Total de Óbitos Confirmados"], style={'text-align': 'center'}),
                                html.H3([df_pb.loc[df_pb['cidade'] == 'Paraíba']['obitos'].values[-1]],
                                        id='total_obitos_pb',
                                        style={'text-align': 'center',
                                               'color': '#420881',
                                               'margin-top': 2,
                                               'height': "20%"}),
                                html.P([str(len(base_dados_pb_o)) + " dos 223 municípios " + "({:.1f}%)".format(
                                    len(base_dados_pb_o) * 100 / 223)], style={'text-align': 'center'})
                            ], className="three columns pretty_container"),

                            html.Div([
                                html.Div(children=maiores_obitos_pb, className="control-tab"),

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
                                    {"label": "Recuperados ", "value": "recuperados"},
                                    {"label": "Óbitos", "value": "obitos"},
                                    {"label": "Ativos", "value": "ativos"},
                                    {"label": "Novos Casos ", "value": "novos_casos"},
                                    {"label": "Letalidade ", "value": "letalidade"},
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
                                        html.H4([
                                            "Escolha o estado:",
                                        ]),

                                        dcc.Dropdown(
                                            id='estados_menu',
                                            options=estados_br,
                                            value='BR',
                                            className="dcc_control",
                                        )

                                    ]),
                                html.Div(
                                    [
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
                                             html.P("Recuperados", style={'text-align': 'center'})],
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
                                             html.P("Letalidade", style={'text-align': 'center'})],
                                            id="mortalidade_br",
                                            className="mini_container",
                                        ),

                                        html.Div(
                                            [html.H4(id="recuperacaoText_br", style={'text-align': 'center'}),
                                             html.P(id="recuperacao_perc_br", style={'text-align': 'center'}),
                                             html.P("Recuperação", style={'text-align': 'center'})],
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
                                html.H3([df.loc[df['state'] == 'TOTAL']['totalCasesMS'].values[-1]],
                                        id='total_casos_br',
                                        style={'text-align': 'center',
                                               'color': 'crimson',
                                               'margin-top': 2,
                                               'height': "20%"}),
                            ], className="three columns pretty_container"),

                            html.Div([
                                html.Div(children=lista_maiores_br, className="control-tab"),

                            ], className="three columns pretty_container",
                                style={"overflowX": "scroll", 'text-align': 'left', 'height': 500}),
                        ]),

                        dcc.Tab(label='Óbitos', children=[
                            html.Div(children=[
                                html.H4([
                                    "Mapa",
                                ], className="container_title"),
                                html.Iframe(id='map_br_o', srcDoc=open("MAPA_COVID19_BR_OBITOS.html", 'r').read(),
                                            width='100%',
                                            height=620),
                            ], className='nine columns pretty_container',
                                style={
                                    'float': 'left',
                                    'width': '75%',
                                    'height': '100%',
                                    'margin-right': '0',
                                },
                                id="map-div-br-o"
                            ),

                            html.Div([
                                html.H4(["Total de Óbitos Confirmados"], style={'text-align': 'center'}),
                                html.H3([df.loc[df['state'] == 'TOTAL']['deathsMS'].values[-1]],
                                        id='total_obitos_br',
                                        style={'text-align': 'center',
                                               'color': '#420881',
                                               'margin-top': 2,
                                               'height': "20%"}),
                            ], className="three columns pretty_container"),

                            html.Div([
                                html.Div(children=maiores_obitos_br, className="control-tab"),

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
                                value=['BR', 'SP', 'PB'],
                                multi=True,
                                className="dcc_control",
                            ),

                            html.P('Filtrar dados por:'),
                            dcc.RadioItems(
                                id="situacao_br",
                                options=[
                                    {"label": "Confirmados", "value": "totalCasesMS"},
                                    {"label": "Óbitos", "value": "deathsMS"},
                                    {"label": "Recuperados", "value": "recovered"},
                                    {"label": "Novos Casos", "value": "newCases"},
                                    {"label": "Ativos", "value": "ativos"},
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
                                "Panorama Confirmados/Óbitos",
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
        ], className='twelve columns'),

        html.Hr(),

        # Começo do Perguntas Frequentes -

        html.Div([
            dcc.Markdown(
                children=['''
                # Perguntas Frequentes

                ### O que é o LABIMEC?

                O Laboratório de Inteligência Artificial e Macroeconomia Computacional (LABIMEC), da Universidade Federal da Paraíba (UFPB), 
                foi fundado no ano de 2018 e, desde então, vem realizando pesquisas voltadas para a análise de políticas macroeconômicas. 

                ### Como um laboratório de economia passou a monitorar um vírus?

                As transformações que acontecem no mundo acadêmico e na sociedade exige cada vez mais versatilidade dos pesquisadores e profissionais. 
                Os trabalhos desenvovidos no LABIMEC são fortemente vinculados a métodos quantitativos e análises de dados, apesar do Covid-19 não pertencer a
                esfera dos fenômenos econômicos diretamente, os efeitos do vírus na economia já podem ser constatados. Com esse propósito, decidimos somar nossos
                esforços e habilidades aos demais setores da sociedade.

                ### Onde podemos saber mais sobre o LABIMEC?

                * O nosso portal pode ser acessado pelo seguinte link: [Site](https://www.ufpb.br/labimec)
                * O nosso instagram pode ser acessado pelo seguinte link: [Instragram](https://www.instagram.com/labimec/)
                * O email do nosso coordenador: cassiodanobrega@yahoo.com.br

                ### De onde são os dados do Dashboard?

                * Os dados disponibilizados são provenientes dos [Boletins Epidemiológicos Coronavírus / Covid-19](https://paraiba.pb.gov.br/diretas/saude/consultas/vigilancia-em-saude-1/boletins-epidemiologicos)
                da Secretaria de Saúde de Estado da Paraíba.

                * Em relação ao Brasil, utilizamos os dados do Ministério da Saúde, coletados através do [repositório](https://github.com/wcota/covid19br) de Wesley Cota.

                ### Com quem entrar em contato caso encontre algum problema ou sugestão no Dash?

                Para sugestões e relatos de problemas, pode-se entrar em contato com os seguintes emails:

                * cassiodanobrega@yahoo.com.br - Coordenador do LABIMEC
                * flaviomacaubas@gmail.com - Membro do LABIMEC


                ### O que é Fapesq?

                A [Fapesq](http://fapesq.rpp.br/) é a Fundação de Apoio à Pesquisa - Fapesq, órgão vínculada à Secretaria de Estado da Educação e da Ciência e Tecnologia - SEECT, 
                está situada na Rua Emiliano Rosendo Silva, S/N, no bairro de Bodocongó, na cidade de Campina Grande - Paraíba, CEP 58.429690, 
                Telefone (83) 99921 4203, E-mail fapesq@fapesq.rpp.br.


                ''']),

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
        data.append(
            {'x': df.loc[df['state'] == 'TOTAL']['date'], 'y': df.loc[df['state'] == 'TOTAL']['recovered'].values,
             'type': 'bar', 'name': 'Recuperados', 'marker': {"color": 'blue'}})
    else:
        data.append(
            {'x': df.loc[df['state'] == selector]['date'], 'y': df.loc[df['state'] == selector]['totalCasesMS'].values,
             'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append(
            {'x': df.loc[df['state'] == selector]['date'], 'y': df.loc[df['state'] == selector]['deathsMS'].values,
             'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
        data.append(
            {'x': df.loc[df['state'] == 'TOTAL']['date'], 'y': df.loc[df['state'] == selector]['recovered'].values,
             'type': 'bar', 'name': 'Recuperados', 'marker': {"color": 'blue'}})

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

    if situacao == 'ativos':
        for estado in selector:
            if estado == 'BR':
                data.append(
                    {'x': list(df[df['state'] == 'TOTAL']['date']),
                     'y': df[df['state'] == 'TOTAL']['totalCasesMS'].values
                          - df[df['state'] == 'TOTAL']['deathsMS'].values
                          - df[df['state'] == 'TOTAL']['recovered'].values,
                     'type': 'line', 'name': estado})
            else:
                data.append({'x': list(df[df['state'] == estado]['date']),
                             'y': df[df['state'] == estado]['totalCasesMS'].values
                                  - df[df['state'] == estado]['deathsMS'].values
                                  - df[df['state'] == estado]['recovered'].values,
                             'type': 'line', 'name': estado})
    else:
        for estado in selector:
            if estado == 'BR':
                data.append(
                    {'x': list(df[df['state'] == 'TOTAL']['date']), 'y': df[df['state'] == 'TOTAL'][situacao].values,
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
                )),
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
        data.append({'x': df_pb.loc[df_pb['cidade'] == selector]['data'],
                     'y': df_pb.loc[df_pb['cidade'] == selector]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append({'x': df_pb.loc[df_pb['cidade'] == selector]['data'],
                     'y': df_pb.loc[df_pb['cidade'] == selector]['recuperados'],
                     'type': 'bar', 'name': 'Recuperados', 'marker': {"color": 'blue'}})
        data.append(
            {'x': df_pb.loc[df_pb['cidade'] == selector]['data'], 'y': df_pb.loc[df_pb['cidade'] == selector]['obitos'],
             'type': 'bar', 'name': 'Óbitos', 'marker': {"color": 'black'}})
    else:
        data.append({'x': df_pb.loc[df_pb['cidade'] == selector]['data'],
                     'y': df_pb.loc[df_pb['cidade'] == selector]['confirmados'],
                     'type': 'bar', 'name': 'Confirmados', 'marker': {"color": 'crimson'}})
        data.append(
            {'x': df_pb.loc[df_pb['cidade'] == selector]['data'], 'y': df_pb.loc[df_pb['cidade'] == selector]['obitos'],
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


# Atualiza gráfico de linha Paraíba
@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities', 'value'), dash.dependencies.Input('situacao', 'value')])
def update_image_src(selector, situacao):

    # Verifica se o seletor tem alguma cidade selecionada
    if len(selector) == 0:
        selector.append('Paraíba')

    data = []

    nome_eixo_x = 'Quantidade'

    if situacao == 'ativos':
        for cidade in selector:
            data.append(
                {'x': df_pb.loc[df_pb['cidade'] == cidade]['data'],
                 'y': df_pb.loc[df_pb['cidade'] == cidade]['confirmados'] -
                      df_pb.loc[df_pb['cidade'] == cidade]['obitos'] -
                      df_pb.loc[df_pb['cidade'] == cidade]['recuperados'],
                 'type': 'line', 'name': cidade})
    elif situacao == 'letalidade':
        nome_eixo_x = 'Letalidade em (%)'
        for cidade in selector:
            data.append(
                {'x': df_pb.loc[df_pb['cidade'] == cidade]['data'],
                 'y': df_pb.loc[df_pb['cidade'] == cidade]['obitos']*100/df_pb.loc[df_pb['cidade'] == cidade]['confirmados'],
                 'type': 'line', 'name': cidade})
    else:
        for cidade in selector:
            data.append(
                {'x': df_pb.loc[df_pb['cidade'] == cidade]['data'], 'y': df_pb.loc[df_pb['cidade'] == cidade][situacao],
                 'type': 'line', 'name': cidade})
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
                title=nome_eixo_x,
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
        if valor >= 0.05:
            return "▲ {:.1f}%".format(valor)
        elif valor <= -0.05:
            return "▼ {:.1f}%".format(valor)
        else:
            return "0%"

    if len(selector) == 0:
        selecionado = 'Paraíba'
    else:
        selecionado = selector

    # ativos
    ativos_inicial = (df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-2] -
                      df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-2] -
                      df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-2])

    if ativos_inicial <= 0:
        ativos_inicial = 1

    # confirmados
    confirmados_inicial = df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-2]

    if confirmados_inicial <= 0:
        confirmados_inicial = 1

    # recuperados
    recuperados_inicial = df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-2]

    if recuperados_inicial <= 0:
        recuperados_inicial = 1

    # obitos
    obitos_inicial = df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-2]

    if obitos_inicial <= 0:
        obitos_inicial = 1

    # Mortalidade e Recuperacao
    confirmados_final = df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-1]
    confirmados_passado = confirmados_inicial

    if confirmados_final == 0:
        confirmados_final = 1

    if confirmados_passado == 0:
        confirmados_passado = 1

    mortalidade_atual = (df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-1] / confirmados_final) * 100
    mortalidade_passado = (df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-2] / confirmados_passado) * 100

    variacao_mortalidade = mortalidade_atual - mortalidade_passado

    recuperacao_atual = (df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-1] / confirmados_final) * 100
    recuperacao_passado = (df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[
                               -2] / confirmados_passado) * 100

    variacao_recuperacao = recuperacao_atual - recuperacao_passado

    # Dados de sáida

    ativos = (df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-1] -
              df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-1] -
              df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-1])

    novos_ativos = ((ativos) - (df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-2] -
                                df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-2] -
                                df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-2])) * 100 / ativos_inicial

    novos_confirmados = (df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-1] -
                         df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[
                             -2]) * 100 / confirmados_inicial

    novos_recuperados = (df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-1] -
                         df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[
                             -2]) * 100 / recuperados_inicial

    novos_obitos = (df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-1] -
                    df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-2]) * 100 / obitos_inicial

    return "{}".format(ativos), \
           formata_saida(novos_ativos), \
           "{}".format(df_pb.loc[df_pb['cidade'] == selecionado]['confirmados'].values[-1]), \
           formata_saida(novos_confirmados), \
           "{}".format(df_pb.loc[df_pb['cidade'] == selecionado]['recuperados'].values[-1]), \
           formata_saida(novos_recuperados), \
           "{}".format(df_pb.loc[df_pb['cidade'] == selecionado]['obitos'].values[-1]), \
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
    lista_styles = []
    for valores in [valor_well, valor_gas, valor_oil, valor_water, valor_mortalidade, valor_recuperacao]:
        if "▲" in valores:
            lista_styles.append({'text-align': 'center', 'color': 'green'})
        elif "▼" in valores:
            lista_styles.append({'text-align': 'center', 'color': 'red'})
        else:
            lista_styles.append({'text-align': 'center', 'color': 'black'})

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
        if valor >= 0.05:
            return "▲ {:.1f}%".format(valor)
        elif valor <= -0.05:
            return "▼ {:.1f}%".format(valor)
        else:
            return "0%"

    if len(selector) == 0 or (selector == 'BR'):
        selecionado = 'TOTAL'
    else:
        selecionado = selector

    # ATIVOS
    ativos_inicial = df.loc[df['state'] == selecionado]['totalCasesMS'].values[-2] - \
                     df.loc[df['state'] == selecionado]['deathsMS'].values[-2] - \
                     df.loc[df['state'] == selecionado]['recovered'].values[-2]

    ativos_final = df.loc[df['state'] == selecionado]['totalCasesMS'].values[-1] - \
                   df.loc[df['state'] == selecionado]['deathsMS'].values[-1] - \
                   df.loc[df['state'] == selecionado]['recovered'].values[-1]

    if ativos_inicial == 0:
        ativos_inicial = 1

    variacao_ativos = (ativos_final - (df.loc[df['state'] == selecionado]['totalCasesMS'].values[-2] -
                                       df.loc[df['state'] == selecionado]['deathsMS'].values[-2] -
                                       df.loc[df['state'] == selecionado]['recovered'].values[-2])) \
                      * 100 / ativos_inicial

    # CONFIRMADOS
    confirmado_inicial = df.loc[df['state'] == selecionado]['totalCasesMS'].values[-2]
    confirmado_final = df.loc[df['state'] == selecionado]['totalCasesMS'].values[-1]

    if confirmado_inicial == 0:
        confirmado_inicial = 1

    variacao_confirmados = (confirmado_final - df.loc[df['state'] == selecionado]['totalCasesMS'].values[
        -2]) * 100 / confirmado_inicial

    # OBITOS
    obitos_inicial = df.loc[df['state'] == selecionado]['deathsMS'].values[-2]
    obitos_final = df.loc[df['state'] == selecionado]['deathsMS'].values[-1]

    if obitos_inicial == 0:
        obitos_final = 1

    variacao_obitos = (obitos_final - df.loc[df['state'] == selecionado]['deathsMS'].values[-2]) * 100 / obitos_inicial

    # MORTALIDADE
    mortalidade_inicial = obitos_inicial * 100 / confirmado_inicial
    mortalidade_final = obitos_final * 100 / confirmado_final

    variacao_mortalidade = mortalidade_final - mortalidade_inicial

    # RECUPERADOS
    recuperados_inicial = df.loc[df['state'] == selecionado]['recovered'].values[-2]
    recuperados_final = df.loc[df['state'] == selecionado]['recovered'].values[-1]

    if recuperados_inicial == 0:
        recuperados_inicial = 1

    variacao_recuperados = (recuperados_final - df.loc[df['state'] == selecionado]['recovered'].values[
        -2]) * 100 / recuperados_inicial

    # Recuperação

    recuperacao_inicial = recuperados_inicial * 100 / confirmado_inicial
    recuperacao_final = recuperados_final * 100 / confirmado_final

    variacao_recuperacao = recuperacao_final - recuperacao_inicial

    return "{:.0f}".format(ativos_final), \
           formata_saida(variacao_ativos), \
           "{}".format(confirmado_final), \
           formata_saida(variacao_confirmados), \
           "{:.0f}".format(recuperados_final), \
           formata_saida(variacao_recuperados), \
           "{}".format(obitos_final), \
           formata_saida(variacao_obitos), \
           "{:.1f}%".format(mortalidade_final), \
           formata_saida(variacao_mortalidade), \
           "{:.1f}%".format(recuperacao_final), \
           formata_saida(variacao_recuperacao)


@app.callback(
    [
        Output('well_perc_br', 'style'),
        Output('gas_perc_br', 'style'),
        Output('water_perc_br', 'style'),
        Output('mortalidade_perc_br', 'style'),
        Output('oil_perc_br', 'style'),
        Output('recuperacao_perc_br', 'style'),
    ],
    [
        Input("well_perc_br", "children"),
        Input("gas_perc_br", "children"),
        Input("water_perc_br", "children"),
        Input("mortalidade_perc_br", "children"),
        Input("oil_perc_br", "children"),
        Input("recuperacao_perc_br", "children"),
    ])
def atualiza_style(valor_well, valor_gas, valor_water, valor_mortalidade, valor_oil, valor_recuperacao):
    lista_styles = []
    for valores in [valor_well, valor_gas, valor_water, valor_mortalidade, valor_oil, valor_recuperacao]:
        if "▲" in valores:
            lista_styles.append({'text-align': 'center', 'color': 'green'})
        elif "▼" in valores:
            lista_styles.append({'text-align': 'center', 'color': 'red'})
        else:
            lista_styles.append({'text-align': 'center', 'color': 'black'})

    return lista_styles[0], lista_styles[1], lista_styles[2], lista_styles[3], lista_styles[4], lista_styles[5]

if __name__ == '__main__':
    app.run_server()
