#!/bin/bash
current_time=$(date +"%H:%M")
work_end="17:00"  # Assuming work day ends at 5 PM
time_left=$(date -u -d @$(( ($(date -d "$work_end" +%s) - $(date +%s)) )) +"%H hours and %M minutes")

echo "Current time: $current_time"
echo "Work day ends in: $time_left"

