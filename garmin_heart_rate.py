import os
from datetime import datetime, timedelta
from garminconnect import Garmin
import json

def get_heart_rate_data(email: str, password: str, days: int = 7):
    try:
        client = Garmin(email, password)
        client.login()

        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        print(f"Fetching heart rate data from {start_date.date()} to {end_date.date()}")
        print("-" * 50)

        for i in range(days):
            date = (end_date - timedelta(days=i)).strftime("%Y-%m-%d")
            try:
                heart_rates = client.get_heart_rates(date)
                
                if heart_rates:
                    print(f"\nDate: {date}")
                    print(f"  Min HR: {heart_rates.get('minHeartRate', 'N/A')}")
                    print(f"  Max HR: {heart_rates.get('maxHeartRate', 'N/A')}")
                    print(f"  Resting HR: {heart_rates.get('restingHeartRate', 'N/A')}")
                    
                    if 'heartRateValues' in heart_rates:
                        samples = heart_rates['heartRateValues']
                        print(f"  Total samples: {len(samples)}")
                        
                        if samples:
                            last_timestamp_ms = samples[-1][0]
                            last_hr = samples[-1][1]
                            last_time = datetime.fromtimestamp(last_timestamp_ms / 1000).strftime("%Y-%m-%d %H:%M:%S")
                            print(f"  LAST HR: {last_hr} bpm at {last_time}")
                else:
                    print(f"\nDate {date}: No data")
            except Exception as e:
                print(f"\nDate {date}: Error - {str(e)}")

        client.logout()
        print("\n" + "-" * 50)
        print("Done!")

    except Exception as e:
        print(f"Login error: {str(e)}")

if __name__ == "__main__":
    email = os.getenv("GARMIN_EMAIL")
    password = os.getenv("GARMIN_PASSWORD")

    if not email or not password:
        print("Please set environment variables:")
        print("  set GARMIN_EMAIL=your_email")
        print("  set GARMIN_PASSWORD=your_password")
    else:
        get_heart_rate_data(email, password)
