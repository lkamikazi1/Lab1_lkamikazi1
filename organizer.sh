#!/bin/bash

#Archival Directory

if [ ! -d "archive" ]; then
    mkdir archive
fi

# Timstamp Generation

timestamp=$(date +%Y%m%d-%H%M%S)

# The Archival Process

original_file="grades.csv"
archived_name="grades_${timestamp}.csv"

if [ -f "$original_file" ]; then
    mv "$original_file" "archive/$archived_name"
    echo "$timestamp | Original: $original_file | Archived as: archive/$archived_name" >> organizer.log
    echo "Archiving complete. $original_file archived as: archive/$archived_name"
else
    echo "Warning: $orginal_file not found, skipping archival."
fi

# Workspace Reset

touch grades.csv
