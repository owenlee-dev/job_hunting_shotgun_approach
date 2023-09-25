import json
from pprint import pprint
from filter import filter_job_listings

with open('example_response.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
 
job_listings=data['data']

filter_job_listings(job_listings)

    