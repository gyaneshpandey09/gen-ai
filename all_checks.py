#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """Returns true if computer has a pending reboot. """
    print("in check_reboot")
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns true if there isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    precentage_free = 100*du.free/du.total
    # Calculate free space in GB
    free_gb = du.free/2**30
    if precentage_free < min_percent or free_gb < min_gb:
        return True
    return False

def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
    if check_disk_full(disk="/",min_gb= 2,min_percent= 10):
        print("Disk Full.")
        sys.exit(1)

main()
