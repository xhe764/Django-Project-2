import json
import urllib.parse # Py3
import urllib.request
import requests
from IPython.display import HTML

 # Add your Microsoft Account Key to a file called bing.key

def read_bing_key():

    """
    Reads the BING API key from a file called 'bing.key'.
    returns: a string which is either None, i.e. no key found, or with a key.
    Remember: put bing.key in your .gitignore file to avoid committing it!
    """
    # See Python Anti-Patterns - it's an awesome resource!
    # Here we are using "with" when opening documents.
    # http://docs.quantifiedcode.com/python-anti-patterns/maintainability/
    bing_api_key = None

    try:
        with open('bing.key','r') as f:
         bing_api_key = f.readline().rstrip()
    except:
        raise IOError('bing.key file not found')

    return bing_api_key

def run_query(search_terms):

    """
    Given a string containing search terms (query),
    returns a list of results from the Bing search engine.
    """
    bing_api_key = read_bing_key()

    if not bing_api_key:
         raise KeyError("Bing Key Not Found")

     # Specify the base url and the service (Bing Search API 2.0)
    root_url = 'https://api.bing.microsoft.com/v7.0/search'
    #search_url = "https://api.bing.microsoft.com/v7.0/search"
    service = 'Web'

     # Specify how many results we wish to be returned per page.
     # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 10
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)

    # Turn the query into an HTML encoded string, using urllib.
    # Use the line relevant to your version of Python.
    query = urllib.parse.quote(query) # Py3

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    #search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(root_url, service, results_per_page,offset,query)

    headers = {"Ocp-Apim-Subscription-Key": bing_api_key}
    params = {"q": search_terms, "textDecorations": True, "textFormat": "HTML", "count": results_per_page, "offset": offset}
    response = requests.get(root_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    output_results = []
    keys = ["webPages", "images", "videos"]
    url = {"webPages": "url", "images": "hostPageUrl", "videos": "hostPageUrl"}
    summary = {"webPages": "snippet", "images": "", "videos": "description"}
    for key in keys:
        if key in search_results.keys():
            for result in search_results[key]["value"]:
                if key != "images":
                    output_results.append({"category": key, "title": result["name"], "link": result[url[key]], "summary": result[summary[key]]})
                else:
                    output_results.append({"category": key, "title": result["name"], "link": result[url[key]], "summary": "None"})
    return output_results

"""
    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''

    # Setup a password manager to help authenticate our request.
    # Watch out for the differences between Python 2 and 3!
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm() # Py3

    # The below line will work for both Python versions.
    password_mgr.add_password(None, search_url, username, bing_api_key)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        # Python 3 import (three lines)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr) # Py3
        print("step 1")
        opener = urllib.request.build_opener(handler) # Py3
        print("step 2")
        urllib.request.install_opener(opener) # Py3
        print("step 3")
        # Connect to the server and read the response generated.
        response = urllib.request.urlopen(search_url).read() # Py3
        print("step 4")
        response = response.decode('utf-8') # Py3
        print("step 5")
        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)
        print("step 6")
        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            results.append({'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description']})
    except:
        print("Error when querying the Bing API")

    # Return the list of results to the calling function.
    return results
"""
def main():
    print("Please type your terms for Bing search:")
    search_term = input()
    search_results=run_query(search_term)

    for v in search_results:
        page = "Category: {0}\nTitle: {1}\nLink: {2}\nSummary: {3}\n\n".format(v["category"], v["title"], v["link"], v["summary"])
        print(page)


if __name__ == '__main__':
    main()
