import os
import sys
from dotenv import load_dotenv
from myfitnesspal import Client as MFPClient
from twilio.rest import Client as TwilioClient
from datetime import date
from utils import format_macro_message
import browser_cookie3

# Load environment variables
load_dotenv()

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TWILIO_WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")

def fetch_macros(mfp_client, entry_date):
    """
    Fetches macro data (calories, protein, carbs, fat) for a given date.
    """
    day = mfp_client.get_date(entry_date.year, entry_date.month, entry_date.day)
    macros = day.totals
    return {
        "calories": int(macros.get("calories", 0)),
        "protein": int(macros.get("protein", 0)),
        "carbohydrates": int(macros.get("carbohydrates", 0)),
        "fat": int(macros.get("fat", 0)),
    }

def send_whatsapp_message(twilio_client, from_number, to_number, message):
    """
    Sends a WhatsApp message using Twilio's API.
    """
    twilio_client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )

def main():
    # Validate environment variables
    for var in [
        "TWILIO_ACCOUNT_SID", 
        "TWILIO_AUTH_TOKEN", "TWILIO_WHATSAPP_FROM", "TWILIO_WHATSAPP_TO"
    ]:
        if not globals()[var]:
            print(f"Missing environment variable: {var}", file=sys.stderr)
            sys.exit(1)

    # Initialise clients
    cj = browser_cookie3.chrome(domain_name='myfitnesspal.com')
    mfp_client = MFPClient(cookiejar=cj)

    twilio_client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Fetch today's macro summary
    today = date.today()
    macros = fetch_macros(mfp_client, today)

    # Format WhatsApp message
    message = format_macro_message(today, macros)

    # Send WhatsApp message
    send_whatsapp_message(twilio_client, TWILIO_WHATSAPP_FROM, TWILIO_WHATSAPP_TO, message)

    print(f"Macros sent for {today}:\n{message}")

if __name__ == "__main__":
    main()
