import requests
from datetime import datetime, timezone
import smtplib
import time

while True:
    time.sleep(60)
    MY_LAT = 
    MY_LONG = 

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.


    if 35 <= iss_latitude <= 46 and -79<= iss_longitude <= -68:
        if time_now >= sunset or time_now <=sunrise:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
                my_email = ""
                connect.starttls()
                connect.login(user=my_email, password="")

                connect.sendmail(from_addr=my_email, to_addrs="",
                                 msg=f"ISS is over head!\n\n Its current position is lat:{iss_latitude}, "
                                     f"lgt:{iss_longitude}")
