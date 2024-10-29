#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import signal
import re


# Global variables to store metrics
total_size = 0
status_codes_stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
lines_processed = 0
print_stats_flag = False

def parse_line(line):
    pattern = r'^(?P<ip>\S+) - \[(?P<date>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) HTTP/\d\.\d" (?P<status>\d{3}) (?P<size>\d+)$'
    match = re.match(pattern, line.strip())
    if match:
        return match.group('status'), int(match.group('size'))
    return None  # Return None if the line does not match the pattern

def print_statistics():
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[code]
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    global print_stats_flag
    print_stats_flag = True  # Set the flag instead of exiting

# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

print("Reading from stdin (press CTRL+C to print statistics and continue):")

# Reading from stdin line by line
for line in sys.stdin:
    parsed = parse_line(line)
    if parsed:  # Only process if parsed is not None
        status, size = parsed  # Unpacking the returned status and size
        total_size += size
        status_codes_stats[status] += 1
        lines_processed += 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print_statistics()
    
    # If the print_stats_flag is set, print stats and reset the flag
    if print_stats_flag:
        print_statistics()
        print_stats_flag = False  # Reset the flag to continue processing
