import dash_bootstrap_components as dbc
from dash import html, Output, Input, State


def generate_settings_button():
    return dbc.Button(html.Img(src="assets/img/gears.svg", className="image-on-button"),
                      class_name="image-button",
                      id="btn-settings")

def generate_settings_modal():
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Settings")),
            dbc.ModalBody(["LOREM IPSUM"], id="modal-settings-body"),
            dbc.ModalFooter(
                dbc.Button(
                    "Close",
                    id="close-modal-settings",
                    className="ms-auto",
                    n_clicks=0,
                )
            ),
        ],
        id="modal-settings",
        scrollable=True,
        is_open=False,
    ),

def register_callbacks(app):
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

