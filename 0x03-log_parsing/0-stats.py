#!/usr/bin/env python3
"""Reads stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict

# Initialize counters
total_file_size = 0
status_code_counts = defaultdict(int)

try:
    for line in sys.stdin:
        # Regex pattern
        match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] \
                         "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            # Extract file size and status code
            file_size, status_code = int(match.group(3)), int(match.group(2))
            total_file_size += file_size
            status_code_counts[status_code] += 1
            # Stats after every 10 lines
            if total_file_size % 100 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")
                print()
except KeyboardInterrupt:
    # Upon receiving a keyboard interruption
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
    print()
