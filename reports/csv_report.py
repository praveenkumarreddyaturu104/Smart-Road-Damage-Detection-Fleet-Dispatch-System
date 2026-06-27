"""
Generate CSV reports for road damages.
"""

import csv


def generate_csv_report(damages, filepath):
    """
    Write damages list to CSV file at filepath.
    """
    headers = [
        "ID",
        "Image Name",
        "Damage Type",
        "Confidence",
        "Severity",
        "Latitude",
        "Longitude",
        "Timestamp"
    ]
    
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for r in damages:
            writer.writerow([
                r["id"],
                r["image_name"],
                r["damage_type"],
                f"{r['confidence'] * 100:.1f}%",
                r["severity"],
                r["latitude"],
                r["longitude"],
                r["timestamp"]
            ])
            
    print(f"CSV report written to {filepath}")
