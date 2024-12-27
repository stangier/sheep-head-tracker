# Import necessary libraries and components
import flask
from dash import Dash, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import src.components as components
import src.components_settings as components_settings

# Initialize the Dash app with a Bootstrap theme
server = flask.Flask(__name__)  # define flask app.server
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css], server=server)

# Main player buttons
player_buttons = components.generate_player_buttons()
div_player_buttons = html.Div(player_buttons, className="div-player-buttons")

# Score keeping table
data = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55]
]

table_header = components.generate_table_header()
table_rows = components.generate_table_rows(data)
table_rows.append(components.generate_table_totals(data)) # Append totals
table_body = [html.Tbody(table_rows)]

div_table = html.Div(dbc.Table(table_header + table_body, bordered=True, id="tbl-points"),
                     id="tbl-points-wrapper")

# General toggle switches applicable for all players
toggles = components.generate_toggles()
div_toggles = html.Div(toggles)

# Modal components showing when clicking on a player button
modal_match = components.generate_modal()
div_modal_match = html.Div(modal_match)

# Settings button
settings_button = components_settings.generate_settings_button()
div_settings = html.Div(settings_button)

# Modal components showing when clicking on a player button
modal_settings = components_settings.generate_settings_modal()
div_modal_settings = html.Div(modal_settings)


@app.callback(
    Output("modal-settings", "is_open"),
    Input("btn-settings", "n_clicks"),
    Input("close-modal-settings", "n_clicks"),
    State("modal-settings", "is_open"),
)
def toggle_modal_settings(settings_btn, close_btn, is_open):
    if settings_btn or close_btn:
        return not is_open
    return is_open


# Main layout of the app
div_main = html.Div([
    div_player_buttons,
    div_table,
    div_toggles,
    div_modal_match,
    div_settings,
    div_modal_settings
])
app.layout = div_main

# Callback to toggle the modal visibility
@app.callback(
    # Outputs and inputs for the callback
    Output("modal-match", "is_open"),
    Output("modal-match-body", "children"),
    Input("btn-player-1", "n_clicks"),
    Input("btn-player-2", "n_clicks"),
    Input("btn-player-3", "n_clicks"),
    Input("btn-player-4", "n_clicks"),
    Input("close-modal-match", "n_clicks"),
    State("modal-match", "is_open"),
)
def toggle_modal_match(n1, n2, n3, n4, n_close, is_open):
    if not ctx.triggered:
        return is_open, ""

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "close-modal-match":
        return not is_open, ""

    player_map = {
        "btn-player-1": "Player One",
        "btn-player-2": "Player Two",
        "btn-player-3": "Player Three",
        "btn-player-4": "Player Four",
    }

    return not is_open, f"Action originated from {player_map[button_id]}"

@app.callback(
    Output("tbl-points", "children"),
    State("score-input", "value"),
    Input("confirm-add", "n_clicks"),
    prevent_initial_call=True
)
def update_scores(n_clicks, score_to_add):
    new_table_rows = components.generate_table_rows(data)

    return [html.Tbody(new_table_rows)]

if __name__ == "__main__":
    app.run(debug=True)
