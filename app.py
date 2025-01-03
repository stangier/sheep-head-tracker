# Import necessary libraries and components
import flask
from dash import Dash, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from components import overview, match, settings
from components.settings import settings_storage

# Initialize the Dash app with a Bootstrap theme
server = flask.Flask(__name__)  # define flask app.server
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css], server=server)

# Main player buttons
player_buttons = overview.generate_player_buttons()
div_player_buttons = html.Div(player_buttons, className="div-player-buttons")

# Score keeping table
data = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55]
]

table_header = overview.generate_table_header()
table_rows = overview.generate_table_rows(data)
table_rows.append(overview.generate_table_totals(data)) # Append totals
table_body = [html.Tbody(table_rows)]

div_table = html.Div(dbc.Table(table_header + table_body, bordered=True, id="tbl-points"),
                     id="tbl-points-wrapper")

# General toggle switches applicable for all players
toggles = overview.generate_toggles()
div_toggles = html.Div(toggles)

# Match components
modal_match = match.generate_modal()
div_modal_match = html.Div(modal_match)
match.register_callbacks(app)

# Settings components
settings_button = settings.generate_settings_button()
div_settings = html.Div(settings_button)
modal_settings = settings.generate_settings_modal(app)
div_modal_settings = html.Div(modal_settings)
settings.register_callbacks(app)

# Main layout of the app
div_main = html.Div([
    settings_storage,
    div_player_buttons,
    div_table,
    div_toggles,
    div_modal_match,
    div_settings,
    div_modal_settings
])
app.layout = div_main

@app.callback(
    Output("tbl-points", "children"),
    State("score-input", "value"),
    Input("confirm-add", "n_clicks"),
    prevent_initial_call=True
)
def update_scores(n_clicks, score_to_add):
    new_table_rows = overview.generate_table_rows(data)

    return [html.Tbody(new_table_rows)]

if __name__ == "__main__":
    app.run(debug=True)
