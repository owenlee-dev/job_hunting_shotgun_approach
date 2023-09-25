import requests
from .keys.constants import JSEARCH_KEY
import json

url = "https://jsearch.p.rapidapi.com/search"
query_title = "Product Owner in Berlin, Germany"


def get_jobs(query_title):
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

    #  API Testing
    with open("assets/test_response.json", "r") as read_file:
        jobs = json.load(read_file)
    return jobs

  # Api Request
    # response = requests.get(url, headers=headers, params=querystring)
    # jobs = response.json()["data"]

    # # Get testing example result
    # with open('assets/test_response.json','w') as f:
    #   json.dump(jobs,f)
      


# return jobs[0]
