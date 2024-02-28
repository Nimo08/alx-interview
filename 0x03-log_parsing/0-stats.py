#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys
import re


def print_stats(total_size, status_codes):
    """Prints stats"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    """Computes metrics"""
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\]\
                             "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
                             line)
            if match:
                status_code = match.group(1)
                if status_code in status_codes:
                    status_codes[status_code] += 1

                total_size += int(match.group(2))
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
                    print()
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
