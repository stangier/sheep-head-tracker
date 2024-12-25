# Import necessary libraries and components
from dash import html
import dash_bootstrap_components as dbc

# Define player buttons for interaction
player_buttons = [
    # Each button represents a player
    dbc.Button("Player One", color="primary", class_name="btn-player", id="btn-player-1"),
    dbc.Button("Player Two", color="primary", class_name="btn-player", id="btn-player-2"),
    dbc.Button("Player Three", color="primary", class_name="btn-player", id="btn-player-3"),
    dbc.Button("Player Four", color="primary", class_name="btn-player", id="btn-player-4")
]

# Define the table header
table_header = [
    # Table columns for each player
    html.Thead(html.Tr([html.Th("Player One"), html.Th("Player Two"), html.Th("Player Three"), html.Th("Player Four")]))
]

# Wrap the table in a div for styling and scrolling
def create_table(table_body):
    return [
        html.Div(
            dbc.Table(table_header + table_body, bordered=True, id="tbl-points"),
            id="tbl-points-wrapper"
        )
    ]

# Define a modal for player information and score input
modal = html.Div(
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
