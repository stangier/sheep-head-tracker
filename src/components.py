import dash_bootstrap_components as dbc
from dash import html


def generate_player_buttons():
    player_buttons = [
        # Each button represents a player
        html.Div([
            dbc.Button("Player One", color="primary", class_name="btn-player", id="btn-player-1"),
            dbc.Button(html.Img(src="assets/img/knocking_fist.svg", className="fist-image image-on-button"),
                       class_name="fist-button image-button",
                       id="btn-fist-player-1")
        ], id="div-btn-player-1"),
        html.Div([
            dbc.Button("Player Two", color="primary", class_name="btn-player", id="btn-player-2"),
            dbc.Button(html.Img(src="assets/img/knocking_fist.svg", className="fist-image image-on-button"),
                       class_name="fist-button image-button",
                       id="btn-fist-player-2")
        ], id="div-btn-player-2"),
        html.Div([
            dbc.Button("Player Three", color="primary", class_name="btn-player", id="btn-player-3"),
            dbc.Button(html.Img(src="assets/img/knocking_fist.svg", className="fist-image image-on-button"),
                       class_name="fist-button image-button",
                       id="btn-fist-player-2")
        ], id="div-btn-player-3"),
        html.Div([
            dbc.Button("Player Four", color="primary", class_name="btn-player", id="btn-player-4"),
            dbc.Button(html.Img(src="assets/img/knocking_fist.svg", className="fist-image image-on-button"),
                       class_name="fist-button image-button",
                       id="btn-fist-player-2")
        ], id="div-btn-player-4")
    ]
    return player_buttons

def generate_table_header():
    table_header = [
        html.Thead(html.Tr([html.Th("Player One"), html.Th("Player Two"), html.Th("Player Three"), html.Th("Player Four")]))
    ]
    return table_header

def generate_modal():
    return html.Div(
    # Modal structure with header, body, and footer
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Player Information")),
                dbc.ModalBody([
                    html.Div("Enter a number to add to the player's score:"),
                    dbc.Input(type="number", id="score-input", placeholder="Enter number"),
                    html.Div(id="modal-match-body"),
                    dbc.Button("Add to Score", id="confirm-add", color="success", className="mt-2")
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal-match", className="ml-auto")
                ),
            ],
            id="modal-match",
            is_open=False,
        )
    ]
)

def calculate_totals(data):
    """Calculate the total for each column."""
    return [sum(column) for column in zip(*data)]

def generate_table_rows(data):
    return [html.Tr([html.Td(value) for value in row]) for row in data]

def generate_table_totals(data):
    totals = calculate_totals(data)
    return html.Tr([html.Td(total) for total in totals], className="total-row")

def generate_toggles():
    return dbc.Checklist(
            options=[
                {"label": "Stock", "value": 1},
                {"label": "Geklopft", "value": 2},
            ],
            value=[],
            id="toggles",
            switch=True
        )
