#!/data/data/com.termux/files/usr/bin/bash

# Run the HRM income scout Python script
python ~/ai_helper/hrm_income_scout.py

# Send a Termux notification
termux-notification --title "HRM Scout" --content "AI Scout ran successfully"
