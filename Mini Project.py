
import random
from datetime import datetime
import pandas as pd

# Smart Equipment Monitoring System
equipment_list = ["Motor", "Water Pump", "Generator"]
records = []

# Equipment monitoring limits
LIMITS = {
    "temperature": 80,   # degrees Celsius
    "vibration": 8,       # mm/s
    "power": 10           # kW
}


def read_sensor():
    """Simulate readings from equipment sensors."""
    return {
        "temperature": round(random.uniform(35, 100), 2),
        "vibration": round(random.uniform(1, 12), 2),
        "power": round(random.uniform(2, 15), 2)
    }


def check_status(readings):
    """Check whether equipment readings are normal or abnormal."""
    problems = []

    if readings["temperature"] > LIMITS["temperature"]:
        problems.append("High temperature")

    if readings["vibration"] > LIMITS["vibration"]:
        problems.append("High vibration")

    if readings["power"] > LIMITS["power"]:
        problems.append("High power consumption")

    if len(problems) >= 2:
        status = "CRITICAL"
        recommendation = "Inspect equipment immediately."
    elif len(problems) == 1:
        status = "WARNING"
        recommendation = "Check equipment and schedule inspection."
    else:
        status = "NORMAL"
        recommendation = "Equipment operating normally."

    return status, ", ".join(problems) if problems else "None", recommendation


def monitor_equipment():
    """Monitor all equipment once."""
    print("\n========== EQUIPMENT STATUS ==========")

    for equipment in equipment_list:
        readings = read_sensor()
        status, problems, recommendation = check_status(readings)

        print(f"\nEquipment: {equipment}")
        print(f"Temperature: {readings['temperature']} °C")
        print(f"Vibration:   {readings['vibration']} mm/s")
        print(f"Power:       {readings['power']} kW")
        print(f"Status:      {status}")

        if status != "NORMAL":
            print(f"ALERT: {problems}")

        print(f"Action: {recommendation}")

        # Save each reading
        records.append({
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Equipment": equipment,
            "Temperature_C": readings["temperature"],
            "Vibration_mm_s": readings["vibration"],
            "Power_kW": readings["power"],
            "Status": status,
            "Problem": problems,
            "Recommendation": recommendation
        })


def view_history():
    """Display previously collected readings."""
    if not records:
        print("\nNo monitoring records available yet.")
        return

    df = pd.DataFrame(records)
    print("\n========== MONITORING HISTORY ==========")
    print(df.to_string(index=False))


def save_records():
    """Export records to a CSV file."""
    if not records:
        print("\nNo records to save. Monitor equipment first.")
        return

    df = pd.DataFrame(records)
    filename = "equipment_monitoring_report.csv"
    df.to_csv(filename, index=False)

    print(f"\nReport saved successfully as: {filename}")


def main():
    print("======================================")
    print("  SMART EQUIPMENT MONITORING SYSTEM")
    print("======================================")

    while True:
        print("\n1. Monitor equipment")
        print("2. View monitoring history")
        print("3. Save report to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            monitor_equipment()
        elif choice == "2":
            view_history()
        elif choice == "3":
            save_records()
        elif choice == "4":
            print("\nThank you for using the monitoring system!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
