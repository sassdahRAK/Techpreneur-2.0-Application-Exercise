'''End-to-End AI Mini-Pipeline run_pipeline(filepath)'''
'''Note: Library allows 
        1. pandas,
        2. requests, 
        3. time.'''
''' – Skip rows where review_text is empty or null — do not pass blank strings to the API.
    – sentiment_rate values are percentages rounded to 1 decimal place.
    – most_positive_product is the product with the highest POSITIVE count. If tied, return the one that appears first alphabetically.
    – most_negative_product follows the same tie-breaking rule.
    – If the file is missing, empty, or has no valid rows, return an empty dictionary.
    – Export the function so it can be imported by the evaluator directly.'''

""" Instruction: Combine your skills from Tasks 01 and 02 
    to build a simple end-to-end pipeline. 
    Given a path to a CSV file containing customer reviews,
    your function must: load and clean the data,
    classify the sentiment of each review using the Hugging Face API, 
    and return a summary report as a dictionary."""