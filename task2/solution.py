'''02 Calling an AI Model API classify_sentiments(texts)'''
'''Note: Library allows 
        1. requests, 
        2. time '''
''' No Hugging Face SDK — use raw HTTP calls only.
– Your API token must be read from an environment variable named HF_API_TOKEN — never hard-code credentials in your file.
– Handle an empty input list — return an empty list, do not call the API.
– Batch all texts in a single API call where possible — do not loop one request per text.
– Export the function so it can be imported by the evaluator directly.'''

""" Write a function that accepts a list
    of short text strings and returns a list
    of sentiment labels — one per input — by calling
    the Hugging Face Inference API. Use the public 
    distilbert-base-uncased-finetuned-sst-2-english model.
    Each label must be one of: POSITIVE, NEGATIVE."""

import requests 
import time 

"""for my current knowlegde only can solve exercise1, I have learn request http in express js but not python"""