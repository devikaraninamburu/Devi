appointments = []

def book_appointment(data):

    doctor = data.get("doctor")
    date = data.get("date")
    time = data.get("time")

    for a in appointments:

        if a["doctor"] == doctor and a["date"] == date and a["time"] == time:
            return {"message": "Slot already booked"}

    appointment = {
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    return {
        "message": "Appointment booked successfully",
        "data": appointment
    }


def cancel_appointment(data):

    doctor = data.get("doctor")
    date = data.get("date")

    for a in appointments:

        if a["doctor"] == doctor and a["date"] == date:

            appointments.remove(a)

            return {"message": "Appointment cancelled"}

    return {"message": "No appointment found"}
