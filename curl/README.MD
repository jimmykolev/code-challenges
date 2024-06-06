# curl

For this challenge we’re going to build a curl clone that is focused on making the HTTP requests we might use for a RESTful API. Our curl clone will be able to connect to a server and send the HTTP methods: GET, DELETE, POST and PUT.
  
[Link to challenge](https://codingchallenges.fyi/challenges/challenge-curl).


## Usage
python curll.py

Followed by some optional arguments:
- -v: Verbose mode.
- -X <method>: Specify the HTTP method to use.
- -H <header-option>: Pass a string to include in the headers
- -d <data>: JSON data to include when using POST/PUT

Finally the HTTP URL to send a request.

Example command:

```python curll.py -X POST http://eu.httpbin.org/post \-d '{"key": "value"}' \ -H "Content-Type: application/json"```