# Lab 1: Grade Evaluator & Archiver

## Overview 
This project calculates student's final academic standing based on pre-existing CSV file of course grades, and build a bash script to archive and reset the grades file after each processing run.

## Files
- grade-evaluator.py: A python script that validates grades and weights, calculates gpa, final decision (pass/fail), logic resubmission.
- organizer.sh: A bash shell that archives the current location (grades.csv), timestamps for current time and date, resets the workspace, and logs each run.

## Requirments
- Python 3
- Bash shell

* First cd Lab1_lkamikazi1

## How to run grade-evaluator.py
- python3 grade-evaluator.py

## How to run organizer.sh
- chmod +x organizer.sh
- ./organizer.sh

