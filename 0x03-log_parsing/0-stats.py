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

def parse_line(line):
    # Regex pattern to match the expected log format
    pattern = r'^(?P<ip>\S+) - \[(?P<date>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) HTTP/\d\.\d" (?P<status>\d{3}) (?P<size>\d+)$'
    match = re.match(pattern, line.strip())
    if match:
        return match.group('ip'), match.group('date'), int(match.group('status')), int(match.group('size'))
    return None

def print_statistics():
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[code]
        if count > 0:
            print(f"{code}: {count}")
 
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)  # Exit gracefully after handling the signal

# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Reading from stdin line by line
for line in sys.stdin:
    parsed = parse_line(line)
    if parsed:
        status, size = parsed
        total_size += size
        status_codes_stats[status] += 1
        lines_processed += 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print_statistics()