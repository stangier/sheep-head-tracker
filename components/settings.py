import enum
import typing
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Tuple

import dash_bootstrap_components as dbc
from dash import html, Output, Input, State, dcc

settings_storage = dcc.Store('settings_storage', 'session')

ID_ = str
TITLE = str
DATATYPE = typing.Any | None
DEFAULT_VALUE = typing.Any
MIN = int | None
MAX = int | None

class MatchType(enum.Enum):
    Partnerspiel = "partnerspiel"
    Solospiel = "solo"
    Other = "other"

class SettingsType(enum.Enum):
    Global = "global"
    Specialized = "specialized"


@dataclass
class PointSettings:
    default_value: DEFAULT_VALUE
    min: MIN
    max: MAX


@dataclass
class Settings:
    title: str
    settings_type: SettingsType
    match_type: MatchType
    point_settings: PointSettings
    laufende_settings: PointSettings
    default_enabled: bool

SETTINGS_CONFIG = {
    "global": "Global Settings",
    "stock": Settings("Stock", SettingsType.Global, MatchType.Other, None, None, True),
    "partnerspiel": Settings("Partnerspiel", SettingsType.Global, MatchType.Partnerspiel,
                             PointSettings(10, 0, None), PointSettings(3, 1, 14), True),
    "solo": Settings("Solospiel", SettingsType.Global, MatchType.Solospiel,
                     PointSettings(20, 0, None), PointSettings(3, 1, 14), True),
    "specific": "Specific Settings",
    "sauspiel": Settings("Sauspiel", SettingsType.Specialized, MatchType.Partnerspiel,
                         PointSettings(10, 0, None), PointSettings(3, 1, 14), True),
    "hochzeit": Settings("Hochzeit", SettingsType.Specialized, MatchType.Partnerspiel,
                         PointSettings(10, 0, None), PointSettings(3, 1, 14), False),
    "geier": Settings("Geier", SettingsType.Specialized, MatchType.Solospiel,
                         PointSettings(20, 0, None), PointSettings(3, 1, 8), False),
    "farbgeier": Settings("Farb-Geier", SettingsType.Specialized, MatchType.Solospiel,
                         PointSettings(20, 0, None), PointSettings(3, 1, 11), False),
    "wenz": Settings("Wenz", SettingsType.Specialized, MatchType.Solospiel,
                         PointSettings(20, 0, None), PointSettings(3, 1, 8), True),
    "farbwenz": Settings("Farb-Wenz", SettingsType.Specialized, MatchType.Solospiel,
                         PointSettings(20, 0, None), PointSettings(3, 1, 11), False),
    "farbsolo": Settings("Farbsolo", SettingsType.Specialized, MatchType.Solospiel,
                         PointSettings(20, 0, None), PointSettings(3, 1, 14), True),
}  # type: Dict[ID_: Settings]


def generate_settings_button():
    return dbc.Button(html.Img(src="assets/img/gears.svg", className="image-on-button"),
                      class_name="image-button",
                      id="btn-settings")

def generate_settings_modal(app):
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Settings")),
            dbc.ModalBody(generate_settings_body(app), id="modal-settings-body"),
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


def create_collapse_callbacks(app, collapse_name, collapse_button):
    @app.callback(
        Output(collapse_name, "is_open"),
        Input(collapse_button, "value")
    )
    def toggle_collapse(n):
        return not n

def create_edit_callback(app, edit_names):
    @app.callback(
        Output("settings_storage", "data"),
        [Input(a[3], 'value') for a in edit_names]
    )
    def values(*kwargs):
        data_dict = defaultdict(lambda: defaultdict(dict))
        for i, (settings_type, settings_key, value, _) in enumerate(edit_names):
            data_dict[settings_type][settings_key][value] = kwargs[i]
        from pprint import pprint
        data_dict = {key: dict(value) for key, value in data_dict.items()}
        pprint(data_dict)
        return ""

def generate_settings_body(app):
    children = []
    safe_keys = []
    for settings_key, settings_value in SETTINGS_CONFIG.items():
        if type(settings_value) is str:
            if len(children) > 0:
                children += [html.Hr()]
            children += [html.H3(settings_value, id=f"{settings_key}-title")]
        else:
            children += [html.H4(settings_value.title, id=f"{settings_key}-title")]
            if settings_value.settings_type == SettingsType.Global:
                children += [dbc.Switch(label="Activate?", id=f"{settings_value.match_type.value}-toggle", value=settings_value.default_enabled)]
            elif settings_value.settings_type == SettingsType.Specialized:
                children += [dbc.Switch(label="Activate?", id=f"{settings_key}-toggle", value=settings_value.default_enabled)]
            safe_keys += [(settings_value.settings_type.value, settings_key, "enabled", f"{settings_value.match_type.value}-toggle")]
            settings_collapse_children = []
            if settings_value.point_settings:
                settings_collapse_children += [
                    dbc.InputGroup(
                    [
                        dbc.InputGroupText("Geld"),
                        dbc.Input(id=f"{settings_key}-money-input",
                                  type="number",
                                  value=settings_value.point_settings.default_value,
                                  min=settings_value.point_settings.min, max=settings_value.point_settings.max,
                                  step=1)
                    ],
                    className="mb-3")]
                safe_keys += [(settings_value.settings_type.value, settings_key, "money", f"{settings_key}-money-input")]
            if settings_value.laufende_settings:
                settings_collapse_children += [
                        dbc.InputGroup([
                        dbc.InputGroupText("Laufende"),
                        dbc.Input(id=f"{settings_key}-laufende-input",
                                  type="number",
                                  value=settings_value.laufende_settings.default_value,
                                  min=settings_value.laufende_settings.min, max=settings_value.laufende_settings.max,
                                  step=1)], className="mb-3")]
                safe_keys += [(settings_value.settings_type.value, settings_key, "laufende", f"{settings_key}-laufende-input")]
            if settings_collapse_children:
                children += [dbc.Collapse(settings_collapse_children, id=f"{settings_key}-collapse",
                                          is_open=settings_value.settings_type == SettingsType.Global)]
            if settings_value.settings_type == SettingsType.Specialized:
                create_collapse_callbacks(app, f"{settings_key}-collapse",
                                          f"{settings_value.match_type.value}-toggle")
    create_edit_callback(app, safe_keys)
    return children



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

