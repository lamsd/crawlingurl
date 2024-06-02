import requests
import json

url = "https://ieeexplore.ieee.org/rest/search"

payload = json.dumps({
    "newsearch": True,
    "queryText": "\"quantum machine learning\"",
    "highlight": True,
    "returnFacets": ["ALL"],
    "returnType": "SEARCH",
    "pageNumber":"2",
    "rowsPerPage": "100",
    "matchPubs": True
})
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept":"application/json, text/plain, */*",
    "Accept-Language":"en-US,en;q=0.5",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "X-Security-Request":"required",
    "Content-Type":"application/json",
    "Origin":"https://ieeexplore.ieee.org",
    "Connection":"keep-alive",
    "Referer":"https://ieeexplore.ieee.org/search/searchresult.jsp?",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "TE":"trailer"
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
