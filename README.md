# gear_example
Example app to show the basics of building a Flywheel gear.

This example primarily illustrates the basic mechanisms involved in building a gear, including:

* Defining the Docker container image
* Building the Docker image
* Defining the gear with manifest.json
* Using a script file to build gear logic
* Runtime elements of a gear including:
    - environment variables
    - input and output folders
    - getting gear data and configuration options from the config.json file
* Using a local gear library to simplify common gear tasks

## Defining the Docker Image
We created a Dockerfile to create a docker image based on python:slim and install the flywheel python SDK.

#### Dockerfile

```
# Create docker image for use by gear
FROM python:slim

RUN pip install flywheel-sdk
```
## Building the Docker Image
To build the container image, run make.sh.  This executes docker build with the resulting image named/tagged as "gear_example".  This is the container image referenced in the gear manifest.json file.

```
docker build --tag gear-example .
```

## Creating the Gear with Gear Builder

The manifest.json and example.py files were originally created by running the Flywheel gear builder.

```
fw gear create
```

This command will prompt you through some questions to quickly generate a basic gear.  Key questions include:

* Descriptive name for the gear
* Short name for the gear
* Docker image to use with the gear
* Type of gear to be generated (Utility Gear vs Analysis Gear)

The generated files were then edited to meet the needs of this example.

One important detail is the fact the we specified the created Docker image when prompted by the gear builder utility.  If you miss this, you can always go back and edit the manifest.json file manually.

## Customized example.py script

In many cases, you can inmplement a functioning gear using only the manaifest.json file.  Commands needed for the gear logic may be specified using the "command" key.

However, since we are using this example to orient you on the key mechanisms of a gear, we chose to use the separate example.py python script.


