# Google Calendar utilities

List 10 upcoming Google Calendar appointments

## How to install&use

1. Place `calendarname.credentials.json` inside the `credentials` directory.

import gcu
gcu.credentials_dir = "path to directory"
gcu.load(calendarname, howmany)

## How to use

Upon first launch, a browser window will appear and you will have to authorize the app.

## How to obtain the credentials.json?

- it takes some clicking through, but start with:
https://developers.google.com/calendar/quickstart/python

there is a big blue button "Enable the Google Calendar API"

# Documentation from Google:
https://developers.google.com/calendar/v3/reference/
