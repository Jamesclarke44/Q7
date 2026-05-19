from config import SOON_THRESHOLD

def label(text):
    return text.replace("_", " ").title()

def get_next_due_status(km_now, name, spec, last_km):
    interval = spec.get("interval_km")
    if not interval:
        return None

    if last_km is None:
        return {
            "service": name,
            "status": "never",
            "due_km": None,
            "remaining": None
        }

    due_km = last_km + interval
    remaining = due_km - km_now

    if km_now >= due_km:
        status = "overdue"
    elif remaining <= SOON_THRESHOLD:
        status = "soon"
    else:
        status = "ok"

    return {
        "service": name,
        "status": status,
        "due_km": due_km,
        "remaining": remaining
    }