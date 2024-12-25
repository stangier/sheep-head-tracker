from dash import Dash, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.DARKLY])

player_buttons = [
    dbc.Button("Player One", color="primary", class_name="btn-player", id="btn-player-1"),
    dbc.Button("Player Two", color="primary", class_name="btn-player", id="btn-player-2"),
    dbc.Button("Player Three", color="primary", class_name="btn-player", id="btn-player-3"),
    dbc.Button("Player Four", color="primary", class_name="btn-player", id="btn-player-4")
]

table_header = [
    html.Thead(html.Tr([html.Th("Player One"), html.Th("Player Two"), html.Th("Player Three"), html.Th("Player Four")]))
]
table_row_1 = html.Tr([html.Td("10"), html.Td("20"), html.Td("30"), html.Td("40")])
table_row_2 = html.Tr([html.Td("10"), html.Td("20"), html.Td("30"), html.Td("40")])
table_row_3 = html.Tr([html.Td("10"), html.Td("20"), html.Td("30"), html.Td("40")])
table_row_4 = html.Tr([html.Td("10"), html.Td("20"), html.Td("30"), html.Td("40")])

table_body = [html.Tbody([table_row_1,
                         table_row_2,
                         table_row_3,
                         table_row_4])]

table_points = [dbc.Table(table_header + table_body, bordered=True, id="tbl-points")]
div_player_buttons = html.Div(player_buttons + table_points, className="div-player-buttons")


modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Player Information")),
                dbc.ModalBody(id="modal-body"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal", className="ml-auto")
                ),
            ],
            id="modal",
            is_open=False,
        )
    ]
)

div_main = html.Div([div_player_buttons, modal])
app.layout = div_main

@app.callback(
    Output("modal", "is_open"),
    Output("modal-body", "children"),
    Input("btn-player-1", "n_clicks"),
    Input("btn-player-2", "n_clicks"),
    Input("btn-player-3", "n_clicks"),
    Input("btn-player-4", "n_clicks"),
    Input("close-modal", "n_clicks"),
    State("modal", "is_open"),
)
def toggle_modal(n1, n2, n3, n4, n_close, is_open):
    if not ctx.triggered:
        return is_open, ""

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "close-modal":
        return not is_open, ""

    player_map = {
        "btn-player-1": "Player One",
        "btn-player-2": "Player Two",
        "btn-player-3": "Player Three",
        "btn-player-4": "Player Four",
    }

    return not is_open, f"Action originated from {player_map[button_id]}"

app.run(debug=True)
