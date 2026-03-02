# BenzaiMVP
this is a repository to host the code for the HDAT mvp api and other prerelease demos and experiments of Benzai

## Installation
- `pip install requirements.txt` installs all the base dependencies required to run the inference.
- Install pytorch as instructed to do so for your local architecture, find details at [pytorch.org/get-started](https://pytorch.org/get-started/locally/). It is theoretically possible to run most of this repo without cuda enabled, but inference times may be unusably slow.
- `pip install server_requirements.txt` if you want to run the api and demonstration codes in addition to inference.
- `pip install testing_requirements.txt` to additionally run the unit tests. Note that this also requires everything in server_requirements and will automatically install them.

## Usage
`python server/benzai_api.py` starts the api on localhost:5000
`python debug/send_api_requests.py` can then be used to send requests to the api and examine responses.
Alternatively, any http tool like curl can be used to send and recieve data directly in console. Example curl usage provided in debug/send_api_requests_curl.bat`

`visualize_tests.bat` runs all tests and outputs a html visualization of the results. This requires package xunit-viewer, installable via `npm i -g xunit-viewer`. Alternatively, just running `pytest` in the tests folder returns a text log of the tests in the console. 
