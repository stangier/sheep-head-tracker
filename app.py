# Import necessary libraries and components
from dash import Dash
import dash_bootstrap_components as dbc
from components import player_buttons, create_table, modal
from callbacks import *
from components import data, create_table_rows, calculate_totals

# Initialize the Dash app with a Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Generate initial table rows and add a total row
table_rows = create_table_rows(data)
# Add total row
totals = calculate_totals(data)
table_rows.append(html.Tr([html.Td(total) for total in totals], className="total-row"))

# Combine table header and body
table_body = [html.Tbody(table_rows)]

# Main layout of the app
div_player_buttons = html.Div(player_buttons + create_table(table_body), className="div-player-buttons")
div_main = html.Div([div_player_buttons, modal])
app.layout = div_main

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
