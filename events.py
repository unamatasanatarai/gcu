from gcu import service
import datetime

def load(calendar, maxResults = 10):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    cal = service.create(calendar)
    events_result = cal.events().list(calendarId='primary', timeMin=now,
                                        maxResults=maxResults, singleEvents=True,
                                        orderBy='startTime', timeZone="CET").execute()
    events = events_result.get('items', [])

    appointments = []
    for event in events:
        start = datetime.datetime.fromisoformat(event['start']['dateTime'])
        end = datetime.datetime.fromisoformat(event['end']['dateTime'])
        duration = end-start
        appointments.append({
            "start": start,
            "end": end,
            "duration_seconds": int(duration.total_seconds()),
            "duration_minutes": int(duration.total_seconds()/60)
        })

    return appointments

