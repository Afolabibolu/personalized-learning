# Working with APIs and Web Data

## What is an API?

An **Application Programming Interface (API)** is an **agreed way for one program to ask another for data or an action**. A website returns HTML for people; an API returns **structured data, usually JSON**, for programs. Like ordering in a restaurant, the client (your program) reads the menu (the documentation), places an order (the request) and receives the dish (the response), but never walks into the kitchen (the server's database).

A request has a **method** (**GET reads data; POST sends new data**), a **URL or endpoint** (such as `/api/v1/forecast`), **query parameters** that filter the result (`?latitude=7.3775&longitude=3.947`) and **headers** (keys, content type, identity). The response carries a **status code**, headers and a body.

## Status codes

**2xx means success, 4xx means your mistake and 5xx means the server's problem.** **200 OK** means success; **201 Created** means a new item was created after a POST; **400 Bad Request** means wrong parameters; **401 Unauthorized** means a missing or wrong API key; **404 Not Found** means the resource does not exist; **429 Too Many Requests** means you are calling too fast, so wait (Retry-After) and try again; and **500** is a server error.

## JSON

JSON maps almost one-to-one to Python: an object `{}` becomes a **dict**, an array `[]` a **list**, true/false become **True/False** and null becomes **None**. JSON keys must use **double quotes**, and JSON has **no comments or trailing commas**. The json module has four functions, remembered in pairs: **`json.loads()`** (string → Python) and **`json.dumps()`** (Python → string) end in "s" and work with **strings**, while **`json.load()`** and **`json.dump()`** work with **files**. Use `.get()` to return a default instead of a KeyError.

## Requests

`requests.get(url, params=params, timeout=10)` sends a GET; `.status_code` gives the code and `.json()` parses the body. **Always set a timeout**, or a program can hang forever. requests **does not raise an error on a 400 by itself**, so check `status_code` or `.ok`, or call `raise_for_status()`, which raises **HTTPError**. Other exceptions are **Timeout**, **ConnectionError** and their parent **RequestException**. `requests.post(url, json=data)` sends data. Keep real API keys in environment variables, never in shared code. Paginated APIs are read in a loop until `next` is None, and `pd.json_normalize()` flattens nested records into a DataFrame.

## Web scraping, responsibly

Before scraping, check the **terms of use**, **robots.txt** (paths bots must avoid and a crawl delay) and **whether there is an API**, which should be used instead. Send a User-Agent header, go slowly and never collect personal data you have no right to. **BeautifulSoup** parses HTML: `find()` returns the first match and `find_all()` a list, using `class_` because class is a Python keyword.

Source: API and Web Data.pptx (Week 8)
