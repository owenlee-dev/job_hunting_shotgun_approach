import requests
from .keys.constants import JSEARCH_KEY
import json

url = "https://jsearch.p.rapidapi.com/search"


def get_jobs(query_title, is_live):
    querystring = {
        "query": query_title,
        "page": "1",
        "num_pages": "1",
        "employment_types": "FULLTIME",
        "country": "de",
        "language": "en",
    }

    headers = {
        "X-RapidAPI-Key": JSEARCH_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
    }

    if is_live:
        response = requests.get(url, headers=headers, params=querystring)
        jobs = response.json()["data"]
    else:
        with open("assets/test_response.json", "r") as read_file:
            jobs = json.load(read_file)
    return jobs

    # Get testing example result
    # with open('assets/test_response.json','w') as f:
    # json.dump(jobs,f)
