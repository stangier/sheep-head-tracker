import dash_bootstrap_components as dbc
from dash import html


def generate_player_buttons():
    player_buttons = [
        # Each button represents a player
        dbc.Button("Player One", color="primary", class_name="btn-player", id="btn-player-1"),
        dbc.Button("Player Two", color="primary", class_name="btn-player", id="btn-player-2"),
        dbc.Button("Player Three", color="primary", class_name="btn-player", id="btn-player-3"),
        dbc.Button("Player Four", color="primary", class_name="btn-player", id="btn-player-4")
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
                    html.Div(id="modal-body"),
                    dbc.Button("Add to Score", id="confirm-add", color="success", className="mt-2")
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal", className="ml-auto")
                ),
            ],
            id="modal",
            is_open=False,
        )
    ]
)

def generate_table_rows(data):
    return [html.Tr([html.Td(value) for value in row]) for row in data]

def generate_table_totals(data):
    return html.Tr([html.Td(total) for total in data], className="total-row")