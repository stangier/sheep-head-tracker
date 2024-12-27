import dash_bootstrap_components as dbc
from dash import html


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
