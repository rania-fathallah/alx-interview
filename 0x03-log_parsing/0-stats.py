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
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    match = re.fullmatch(log_fmt, line)
    if match:
        status_code = match.group('status')
        file_size = int(match.group('size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
        return info
    return None 

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

# Reading from stdin line by line
for line in sys.stdin:
    parsed = parse_line(line)
    if parsed:  # Only process if parsed is not None
        status = parsed['status_code']  # Access the status code
        size = parsed['file_size']  # Access the file size
        total_size += size
        status_codes_stats[status] += 1
        lines_processed += 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print_statistics()
