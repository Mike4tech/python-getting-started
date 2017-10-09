## Python Examples for Geeny

This repository contains all the examples for the Getting Started with Formula Development

## Dependencies (Local Development)

You'd require a suitable python to run this project. We tested it with `Python 2.7
and pip 9.0.1`


```
cd Step-1
pip install -r requirements.txt
python main.py
```

By default the `main.py` will use the port 80, which requires root access.

## Dependencies (Docker Development)

To run the HelloWorld application, you must have [Docker](https://www.docker.com/)
installed.

At Geeny, we use Docker Edge 17.0.*, and this is the version we have used in our
tests. Other versions are not guaranteed to work with this tutorial.

We also use [docker-compose](https://github.com/docker/compose) to more easily
declare our app dependencies at the infrastructure level.

To run your service locally, you can run:

```
cd Step-1
docker-compose build && docker-compose up
```

The `docker-compose.yml` file conveniently re-maps the exposed port from the 80 (used
by Geeny) to 3000

Now visit http://localhost:3000 and the example should be running there.

## License

Copyright (C) 2017 Telefónica Germany Next GmbH, Charlottenstrasse 4, 10969 Berlin.

This project is licensed under the terms of the [Mozilla Public License Version 2.0](LICENSE.md).

Inconsolata font is copyright (C) 2006 The Inconsolata Project Authors. This Font Software is licensed under the [SIL Open Font License, Version 1.1](OFL.txt).
