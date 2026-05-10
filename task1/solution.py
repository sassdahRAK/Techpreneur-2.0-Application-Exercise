'''01 Data Analysis & Aggregation analyse_sales(filepath)'''
'''Note: Library allows 
        1. pandas,
        2. numpy. '''
''' – total_revenue = sum of (units_sold × unit_price) per row; avg_unit_price = mean of unit_price values in that category, rounded to 2 decimal places.
    – best_month is determined by total revenue in that month for that category — return the full month name (e.g. 'March', not '03').
    – If the file is missing or empty, return an empty dictionary — do not raise.
    – Export the function so it can be imported by the evaluator directly.'''

#groupAndAggregate(data)
""" Instruction: Given a path to a CSV 
    file containing product sales data, 
    load and analyse the data using pandas.
    Return a dictionary where each key is
    a product category and each value is a summary object containing total_units_sold,
    total_revenue, avg_unit_price,
    and best_month — the month name with the
    highest total revenue for that category."""