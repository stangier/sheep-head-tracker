# Import necessary libraries and components
from dash import Dash, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

# Initialize the Dash app with a Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

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

# Sample data for dynamic rows representing player scores
data = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55]
]

# Calculate total for each column
def calculate_totals(data):
    """Calculate the total for each column."""
    return [sum(column) for column in zip(*data)]

totals = calculate_totals(data)

# Create table rows dynamically
def create_table_rows(data):
    """Create table rows from data."""
    return [html.Tr([html.Td(value) for value in row]) for row in data]

# Generate initial table rows and add a total row
table_rows = create_table_rows(data)
# Add total row
# Add total row
table_rows.append(html.Tr([html.Td(total) for total in totals], className="total-row"))

# Combine table header and body
table_body = [html.Tbody(table_rows)]

# Wrap the table in a div for styling and scrolling
table_points = [
    html.Div(
        dbc.Table(table_header + table_body, bordered=True, id="tbl-points"),
        id="tbl-points-wrapper"
    )
]
div_player_buttons = html.Div(player_buttons + table_points, className="div-player-buttons")


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

# Main layout of the app
div_main = html.Div([div_player_buttons, modal])
app.layout = div_main

# Callback to toggle the modal visibility
@app.callback(
    # Outputs and inputs for the callback
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
        # No button was clicked
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
    # Toggle modal and display which button was clicked

# Callback to update scores when the "Add to Score" button is clicked
@app.callback(
    # Output to update table, input for button click, and state for input value
    Output("tbl-points", "children"),
    Input("confirm-add", "n_clicks"),
    State("score-input", "value"),
    prevent_initial_call=True
)
def update_scores(n_clicks, score_to_add):
    if n_clicks is None or score_to_add is None:
        # No action if button not clicked or input is empty
        return table_body

    # Update each player's score with the input value
    for row in data:
        for i in range(len(row)):
            row[i] += score_to_add

    # Recalculate totals after updating scores
    new_totals = calculate_totals(data)

    # Create new table rows with updated scores and totals
    new_table_rows = create_table_rows(data)
    new_table_rows.append(html.Tr([html.Td(total) for total in new_totals], className="total-row"))

    return [html.Tbody(new_table_rows)]

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
