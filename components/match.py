import dash_bootstrap_components as dbc
from dash import html

# Spielart
# Farbsolo / Wenz / Geier / Sauspiel

# Sauspiel Paramter
# Spielpartner

# Farbsolo Parameter
# Tout

# Generelle Parameter
# Anzahl Lfd.

# Ausgang
# Gewonnen / Verloren

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