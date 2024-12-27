import dash_bootstrap_components as dbc
from dash import html, Output, Input, State, ctx


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


def register_callbacks(app):
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

