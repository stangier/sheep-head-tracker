from dash import Dash, html
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


div_main = html.Div([div_player_buttons])
app.layout = div_main

if __name__ == '__main__':
    app.run(debug=True)