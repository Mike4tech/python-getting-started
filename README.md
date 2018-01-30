# Getting Started with Formulas - Python HelloWorld Application

This repository contains all of the **python** code examples for the Getting Started
with Formula Development tutorial.

Other languages are available at the following urls:

-  [Ruby](https://github.com/geeny/ruby-getting-started)
-  [Node](https://github.com/geeny/node-getting-started)

## Dependencies (Local Python Development)

TBD

## Configure:

You can use the `config.json` configuring the app. Same approach can be used using
environment variables.

```json
{
  "GEENY_APPLICATION_ID": "<your-application-id>",
  "GEENY_APPLICATION_BROKER_SUBSCRIBER_URL": "<application-broker-url>",
  "GEENY_APPLICATION_AUTH_TOKEN": "<application-broker-authorization-token>"
}
```

### `GEENY_APPLICATION_ID`

To find value for , you can visit the [developer
dashboard](https://developers.geeny.io/applications) and find the details for your
formula, you can refer to the [Getting Started with
Formulas](https://docs.geeny.io/getting-started/formulas/).


### `GEENY_APPLICATION_AUTH_TOKEN`

_Note_: This will be deprecated once the dashboard is available.

These token is for authentication: Please do not share these tokens with anyone.

Obtaining a token for the application broker using curl: First you will need to get
an API token for your user:

```
curl https://connect.geeny.io/auth/login -H Content-Type:application/json -d '{"email": "<email address>", "password": "<password>"}'
```

Then request a token for you application:

```
curl https://developers.geeny.io/ar/applications/<application id>/runtime -H
Authorization:"JWT <token>" -v
```

For more details about which values needs to be set for
`GEENY_APPLICATION_BROKER_SUBSCRIBER_URL` and `GEENY_APPLICATION_AUTH_TOKEN`, please
visit the [API Reference](https://docs.geeny.io/api/) and [Authentication &
Authorization](https://docs.geeny.io/platform-overview/authentication/).

## Run the code:

```
pip3 install -r requirements.txt
python3 app.py
```

This example does the following:

1. Initializes the iterator if needed.
2. Gets the data of the iterator.
3. Updates the iterator to the new position.
4. Renders the data as JSON in the /messages endpoint of your formula.

Go ahead, run the Formula. If you go to "localhost:3000/messages" you
should see the messages that have been pushed to your app.

## Simulate a message with Mosquitto (MQTT Client)

*TBD*

# On Granting Permissions

The end-user (i.e., the owner of the device) should grant permission to the formula
to access the device data. This is commonly known as subscribing.

Once the formula is subscribed to users' devices, you can call the application broker
to get your user's data.

For the time being, we'll ignore this step. Geeny automatically subscribes its
developers to their own devices. This makes prototyping and playing around with data
easier and fun. We'll come back to authentication and authorization in the next step.

# License

Copyright (C) 2017 Telefónica Germany Next GmbH, Charlottenstrasse 4, 10969 Berlin.
This project is licensed under the terms of the [Mozilla Public License Version 2.0](LICENSE.md).
