import time
import csv

from datetime import datetime

# Color library
from colorama import Fore, Style, init

# Initialize colorama
init()

# =========================
# CREATE CSV REPORT FILE
# =========================

with open("report.csv", "w", newline="") as csv_file:

    writer = csv.writer(csv_file)

    # CSV header row
    writer.writerow([

        "Timestamp",

        "Severity",

        "Message"

    ])

print(
    Fore.CYAN +
    "LOG MONITORING SYSTEM STARTED...\n"
)

# Infinite monitoring loop
while True:

    # =========================
    # READ SERVER LOG FILE
    # =========================

    with open("server.log", "r") as file:

        # Read all log lines
        logs = file.readlines()

    # =========================
    # READ EXISTING ALERTS
    # =========================

    with open("alerts.txt", "r") as alert_file:

        # Store old alerts
        existing_alerts = alert_file.readlines()

    # =========================
    # COUNTERS
    # =========================

    error_count = 0
    warning_count = 0
    critical_count = 0

    # =========================
    # OPEN ALERT FILE
    # =========================

    with open("alerts.txt", "a") as alert_file:

        # Loop through logs
        for line in logs:

            # Current timestamp
            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            # Remove extra spaces/newlines
            clean_line = line.strip()

            # =========================
            # CRITICAL DETECTION
            # =========================

            if "CRITICAL" in line:

                # Avoid duplicate alerts
                if line not in existing_alerts:

                    print(
                        Fore.MAGENTA +
                        "\nCRITICAL ALERT:"
                    )

                    print(
                        Fore.MAGENTA +
                        f"[{timestamp}] {clean_line}"
                    )

                    # Save alert with timestamp
                    alert_file.write(
                        f"[{timestamp}] {line}"
                    )

                    print(
                        Fore.MAGENTA +
                        "Critical alert saved."
                    )

                    # =========================
                    # SAVE TO CSV REPORT
                    # =========================

                    with open(
                        "report.csv",
                        "a",
                        newline=""
                    ) as csv_file:

                        writer = csv.writer(csv_file)

                        writer.writerow([

                            timestamp,

                            "CRITICAL",

                            clean_line

                        ])

                else:

                    print(
                        Fore.MAGENTA +
                        f"\nAlready monitored: {clean_line}"
                    )

                # Increase counter
                critical_count += 1

            # =========================
            # ERROR DETECTION
            # =========================

            elif "ERROR" in line:

                # Avoid duplicate alerts
                if line not in existing_alerts:

                    print(
                        Fore.RED +
                        "\nERROR FOUND:"
                    )

                    print(
                        Fore.RED +
                        f"[{timestamp}] {clean_line}"
                    )

                    # Save alert with timestamp
                    alert_file.write(
                        f"[{timestamp}] {line}"
                    )

                    print(
                        Fore.RED +
                        "New error saved."
                    )

                    # =========================
                    # SAVE TO CSV REPORT
                    # =========================

                    with open(
                        "report.csv",
                        "a",
                        newline=""
                    ) as csv_file:

                        writer = csv.writer(csv_file)

                        writer.writerow([

                            timestamp,

                            "ERROR",

                            clean_line

                        ])

                else:

                    print(
                        Fore.RED +
                        f"\nAlready monitored: {clean_line}"
                    )

                # Increase counter
                error_count += 1

            # =========================
            # WARNING DETECTION
            # =========================

            elif "WARNING" in line:

                # Avoid duplicate alerts
                if line not in existing_alerts:

                    print(
                        Fore.YELLOW +
                        "\nWARNING DETECTED:"
                    )

                    print(
                        Fore.YELLOW +
                        f"[{timestamp}] {clean_line}"
                    )

                    # Save warning with timestamp
                    alert_file.write(
                        f"[{timestamp}] {line}"
                    )

                    print(
                        Fore.YELLOW +
                        "Warning saved."
                    )

                    # =========================
                    # SAVE TO CSV REPORT
                    # =========================

                    with open(
                        "report.csv",
                        "a",
                        newline=""
                    ) as csv_file:

                        writer = csv.writer(csv_file)

                        writer.writerow([

                            timestamp,

                            "WARNING",

                            clean_line

                        ])

                else:

                    print(
                        Fore.YELLOW +
                        f"\nAlready monitored: {clean_line}"
                    )

                # Increase counter
                warning_count += 1

    # =========================
    # SUMMARY DASHBOARD
    # =========================

    print(
        Fore.CYAN +
        "\nSUMMARY:"
    )

    print(
        Fore.RED +
        f"Errors: {error_count}"
    )

    print(
        Fore.YELLOW +
        f"Warnings: {warning_count}"
    )

    print(
        Fore.MAGENTA +
        f"Critical Alerts: {critical_count}"
    )

    print(
        Fore.CYAN +
        "\nChecking again in 5 seconds..."
    )

    # Reset terminal color
    print(Style.RESET_ALL)

    # Wait before next scan
    time.sleep(5)