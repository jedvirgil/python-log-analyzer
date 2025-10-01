import pandas as pd
import re

def parse_log_file(log_file_path):
    """Parses a log file and returns a list of dictionaries."""
    parsed_data = []
    # Example regex for a simple log format: YYYY-MM-DD HH:MM:SS - LEVEL: MESSAGE
    log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (INFO|WARNING|ERROR|DEBUG): (.*)")

    with open(log_file_path, 'r') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                timestamp, level, message = match.groups()
                parsed_data.append({
                    'Timestamp': timestamp,
                    'Level': level,
                    'Message': message
                })
    return parsed_data

def convert_log_to_excel(log_file_path, excel_file_path):
    """Converts a log file to an Excel file."""
    data = parse_log_file(log_file_path)
    if data:
        df = pd.DataFrame(data)
        df.to_excel(excel_file_path, index=False)
        print(f"Log data successfully converted to {excel_file_path}")
    else:
        print("No data parsed from the log file.")

if __name__ == "__main__":
    log_file = "example.log" # Replace with your log file name
    output_excel = "log_output.xlsx" # Desired output Excel file name

    # Create a dummy log file for demonstration
    with open(log_file, 'w') as f:
        f.write("2023-10-26 10:00:01 - INFO: Application started.\n")
        f.write("2023-10-26 10:00:05 - DEBUG: Processing user request.\n")
        f.write("2023-10-26 10:00:10 - ERROR: Database connection failed.\n")
        f.write("2023-10-26 10:00:15 - WARNING: Low disk space.\n")

    convert_log_to_excel(log_file, output_excel)
