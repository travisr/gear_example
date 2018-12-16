# gear_example
Example app to show the basics of building a Flywheel gear.

This example primarily illustrates the basic mechanisms involved in building a gear, including:

* Defining the gear with manifest.json
* Using a script file to build gear logic
* Runtime elements of a gear including:
    - environment variables
    - input and output folders
    - getting gear data and configuration options from the config.json file
* Using a local gear library to simplify common gear tasks

## Docker Image
We create a docker image based on python:slim and install the flywheel python SDK

```
# Create docker image for use by gear
FROM python:slim

RUN pip install flywheel-sdk
```
## Building th Image
To build the container image, run make.sh.  This executes docker build with the resulting image named/tagged as "gear_example".  This is the container image referenced in the gear manifest.json file.



