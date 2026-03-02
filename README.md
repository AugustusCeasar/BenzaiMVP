# BenzaiMVP
this is a repository to host the code for the HDAT mvp api and other prerelease demos and experiments of Benzai

## Installation
- `pip install requirements.txt` installs all the base dependencies required to run the inference.
- Install pytorch as instructed to do so for your local architecture, find details at [pytorch.org/get-started](https://pytorch.org/get-started/locally/). It is theoretically possible to run most of this repo without cuda enabled, but inference times may be unusably slow.
- `pip install server_requirements.txt` if you want to run the api and demonstration codes in addition to inference.
- `pip install testing_requirements.txt` to additionally run the unit tests. Note that this also requires everything in server_requirements and will automatically install them.

## Usage
`visualize_tests.bat` runs all tests and outputs a html visualization of the results.
