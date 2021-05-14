
import requests
import dash
import dash_core_components as dcc
from event_plotter import plotEvents
from dash.dependencies import Input, Output, State
from team_radar import team_radar_builder
import dash_html_components as html
import glob
import dash_bootstrap_components as dbc
from fig_generator import fig_from_json
from initial_figures import (
    initial_figure_radar,
    initial_figure_simulator,
    initial_figure_events,
)
import dash_daq as daq

# Create list of event csv files available to select from via a pulldown menu
event_file_list = glob.glob("data/**/*.csv",recursive=True)
event_files = [w.replace("data/", "") for w in event_file_list]
event_files = [s for s in event_files if "Event" in s]

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SUPERHERO],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},],)


server = app.server
style={'background-color': "black"}
# Configure controls using Dash Design Kit
static_graph_controls = [
    dbc.FormGroup(
        [
            dbc.Label("Match: ",style={'text-align': 'center','font-size': "200%","font-family":'Amiri', "color": "white"}),
            dbc.Select(style={'background-color': "floralwhite",'font-size': "200%"},
                id="event-file",
                options=[{"label": i, "value": i} for i in event_files],
                value=False,
                placeholder="Select a file for events",
            ),
        ],style={'background-color': "black"}
    ),
    dbc.FormGroup(
        [
            dbc.Label("Équipe:",style={'text-align': 'center','font-size': "200%","font-family":'Amiri', "color": "white"}),
            dbc.Select(style={'background-color': "floralwhite",'font-size': "200%"},
                id="team-dropdown",
                options=[{"label": i, "value": i} for i in ["Home", "Away"]],
                value="Home",
                placeholder="Select a file for events",
            ),
        ],style={'background-color': "black"}
    ),
    dbc.FormGroup(
        [
            dbc.Label("Joueur:",style={'text-align': 'center', 'font-size': "200%", "font-family": 'Amiri', "color": "white"}),
            dbc.Select(style={'background-color': "floralwhite", 'font-size': "200%"},
                id="team-dropdown1",
                options=[{"label": i, "value": i} for i in ["Home", "Away"]],
                value="Home",
                placeholder="Select a file for events",
                ),
        ], style={'background-color': "black"}
    ),]
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


# Configure main app layout
app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Header([html.H1("Wydad Football Science", style={'text-align': "center",'color': "red","font-family": 'Brush Script MT','font-size': "600%"})]

                    ),
        html.Div([
        html.Img(src='/assets/logo1.png',style={
                'height': '15',
                'width': '15'})],style={'textAlign': 'center'}),

        dbc.Card(
            dbc.Row([dbc.Col(c) for c in static_graph_controls], form=True), body=True,style={'background-color': "black"}

        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon1",
                                children=[
                                    dcc.Graph(style={'background-color': "black"},
                                        id="radar-graph",
                                        figure=initial_figure_radar(),
                                        config={
                                            "modeBarButtonsToRemove": [
                                                "toggleSpikelines",
                                                "pan2d",
                                                "autoScale2d",
                                                "resetScale2d",
                                            ]
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon2",
                                children=[
                                    dcc.Graph(style={'background-color': "black"},
                                        id="events-shots",
                                        figure=initial_figure_events(),
                                        config={
                                            "modeBarButtonsToAdd": [
                                                "drawline",
                                                "drawopenpath",
                                                "drawcircle",
                                                "drawrect",
                                                "eraseshape",
                                            ],
                                            "modeBarButtonsToRemove": [
                                                "toggleSpikelines",
                                                "pan2d",
                                                "autoScale2d",
                                                "resetScale2d",
                                            ],
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
            ],
            form=True,
            no_gutters=False,
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon3",
                                children=[
                                    dcc.Graph(style={'background-color': "black"},
                                        id="events-assists",
                                        figure=initial_figure_events(),
                                        config={
                                            "modeBarButtonsToAdd": [
                                                "drawline",
                                                "drawopenpath",
                                                "drawcircle",
                                                "drawrect",
                                                "eraseshape",
                                            ],
                                            "modeBarButtonsToRemove": [
                                                "toggleSpikelines",
                                                "pan2d",
                                                "autoScale2d",
                                                "resetScale2d",
                                            ],
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon4",
                                children=[
                                    dcc.Graph(style={'background-color': "black"},
                                        id="events-progressive-passes",
                                        figure=initial_figure_events(),
                                        config={
                                            "modeBarButtonsToAdd": [
                                                "drawline",
                                                "drawopenpath",
                                                "drawcircle",
                                                "drawrect",
                                                "eraseshape",
                                            ],
                                            "modeBarButtonsToRemove": [
                                                "toggleSpikelines",
                                                "pan2d",
                                                "autoScale2d",
                                                "resetScale2d",
                                            ],
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
            ],
            form=True,
            no_gutters=False,
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon5",
                                children=[
                                    dcc.Graph(style={'background-color': "black"},
                                        id="events-crosses",
                                        figure=initial_figure_events(),
                                        config={
                                            "modeBarButtonsToAdd": [
                                                "drawline",
                                                "drawopenpath",
                                                "drawcircle",
                                                "drawrect",
                                                "eraseshape",
                                            ],
                                            "modeBarButtonsToRemove": [
                                                "toggleSpikelines"
                                            ],
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        children=[
                            dcc.Loading(
                                id="loading-icon6",
                                children=[
                                    dcc.Graph(style={'background-color': "black"},
                                        id="events-set-plays",
                                        figure=initial_figure_events(),
                                        config={
                                            "modeBarButtonsToAdd": [
                                                "drawline",
                                                "drawopenpath",
                                                "drawcircle",
                                                "drawrect",
                                                "eraseshape",
                                            ],
                                            "modeBarButtonsToRemove": [
                                                "toggleSpikelines",
                                                "pan2d",
                                                "autoScale2d",
                                                "resetScale2d",
                                            ],
                                        },
                                    )
                                ],
                                type="default",
                            )
                        ]
                    ),
                ),
            ],
            form=True,
            no_gutters=False,
        ),
        html.Footer(
            [html.H6("Wydad Football Science | 2021 - REMIDI Kamal ©", style={'text-align': "center", 'color': "white", "font-size": "15px"})]),

    ],
style={'background-color':"black"},
)

# Callback for events data
@app.callback(
    [
        Output("events-shots", "figure"),
        Output("events-assists", "figure"),
        Output("events-progressive-passes", "figure"),
        Output("events-crosses", "figure"),
        Output("events-set-plays", "figure"),
    ],
    [Input("event-file", "value"), Input("team-dropdown", "value")],
    prevent_initial_call=True,
)
def event_graph(event_file, team):
    if team is not None and event_file is not None:
        fig_shots = plotEvents("Shots", event_file, team, "Home")
        fig_assists = plotEvents("Assists to Shots", event_file, team, "Home")
        fig_crosses = plotEvents("Crosses", event_file, team, "Home")
        fig_set_plays = plotEvents("Set Plays", event_file, team, "Home")
        fig_progressive_passes = plotEvents(
            "Progressive Passes", event_file, team, "Home"
        )
        for x in [
            fig_shots,
            fig_assists,
            fig_crosses,
            fig_set_plays,
            fig_progressive_passes,
        ]:
            # Change modebar drawing item colour so that it stands out (vs. grey)
            x.update_layout(newshape=dict(line_color="#00aaff"))
        return (
            fig_shots,
            fig_assists,
            fig_crosses,
            fig_set_plays,
            fig_progressive_passes,
        )

    else:
        fig = initial_figure_events()
        return fig, fig, fig, fig, fig


# Callback for KPI Radar
@app.callback(
    Output("radar-graph", "figure"),
    [Input("event-file", "value"), Input("team-dropdown", "value")],
    prevent_initial_call=True,
)
def radar_graph(radar_file, team):
    if team is not None:
        fig = team_radar_builder(radar_file, team)
        return fig
    else:
        fig = initial_figure_radar()
        fig.update_layout(margin=dict(l=80, r=80, b=30, t=55))
        # Disable zoom. It just distorts and is not fine-tunable
        fig.layout.xaxis.fixedrange = True
        fig.layout.yaxis.fixedrange = True
        return fig

if __name__ == "__main__":
    app.run_server(debug=False)
