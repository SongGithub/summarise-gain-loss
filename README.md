# summarise-gain-loss

a simple tool to calculate gains and losses from a series of stdin

## How to run the app

`cat <path-to-data-file> | docker-compose run summarise`

for example: `cat tests/fixtures/original_sample | docker-compose run summarise`

expected result is
```
34.35
-7.67
```

## How to run unittest

`docker-compose run test`

## How to develop

`docker-compose run dev`

*Note: In case you need to update Docker image, i.e. after you modified
requirements.txt during development process, please do run `docker-compose build --no-cache`
to refresh the image*

## Assumptions
- There is only one numeric string per line in input data
- There are at least 2 entries in input data.
- In each entry, resolution is up to cent. (there must be 2 digits after decimal point)
