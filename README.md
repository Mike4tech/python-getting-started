# Getting Started with Formulas - Python HelloWorld Application

This repository contains all of the **Python** code examples for the Getting
Started with Formula Development tutorial. Each step in the tutorial is
separated into its own directory, e.g., `Step1`.

Other languages:

-  [Node.js](https://github.com/geeny/node-getting-started)
-  [Ruby](https://github.com/geeny/ruby-getting-started)

## Dependencies (Local Development)

You need [Python 2.7 or greater](https://www.ruby-lang.org/en/downloads/) and 
[pip](https://pypi.python.org/pypi/pip) to
develop this project locally. This project has been tested with `Python 2.7`
and `pip 9.0.1`.

To install the dependencies and run the application, execute the following in
the command line:

```
cd Step-1
pip install -r requirements.txt
python main.py
```

By default, the application (`main.py`) will use port 80, which requires root
access.

## Dependencies (Docker Development)

To run the HelloWorld application, you must have [Docker](https://www.docker.com/)
installed.

At Geeny, we use Docker Edge 17.0.*, and this is the version we have used in our
tests. Other versions are not guaranteed to work with this tutorial.

We also use [docker-compose](https://github.com/docker/compose) to more easily
declare our app dependencies at the infrastructure level.

To run the Docker image locally, you can execute the following:

```
cd Step-1
docker-compose build && docker-compose up
```

The `docker-compose.yml` file re-maps the exposed port from 80 (used by Geeny)
to 3000.

When you execute the above commands, visit http://localhost:3000 and
the example should be running there.

## License

Copyright (C) 2017 Telefónica Germany Next GmbH, Charlottenstrasse 4, 10969 Berlin.

This project is licensed under the terms of the [Mozilla Public License Version 2.0](LICENSE.md).
