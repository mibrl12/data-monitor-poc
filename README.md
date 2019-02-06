# data-monitor-poc

This is a PoC of a system which includes generation of data, its ingest, storage and consistency check.

## Run

- clone this repository
- run `docker-compose up -d`

## Components

### datahub

A service that provides an API for storing the time series data into MongoDb.

### data-reporter

A simulator that sends data to the `datahub` API.

### data-monitor

A service that pulls data from MongoDb and detect problems.

todos:
- store offset on disk
- make outlier/late-arrival rules configurable
- detect missing values
