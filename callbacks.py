from dash import Output, Input, State, ctx
from app import app
from components import create_table_rows, calculate_totals, data, table_body

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
