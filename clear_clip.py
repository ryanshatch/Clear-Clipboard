# ****************************************************************************************
# Title: Clear Clipboard           *******************************************************
# Developed by: Ryan Hatch         *******************************************************
# Date: August 10th 2023           *******************************************************
# Last Updated: August 10th 2023   *******************************************************
# Version: 1.0.0                   *******************************************************
# ****************************************************************************************

import os

def clear_clip():
    """Clear the clipboard."""
    os.system("echo off | clip")
    print("Clipboard cleared.")

def main():
    """Clear the clipboard until the user says to stop."""
    yes_responses = {"y", "yes", "yeah", "yep", "yah", "yea", "yee", "yis", "indeed", "si", "oui", "ja", "da", "hai", "porfavor"}
    """Set of recognized positive responses for continuing clipboard clearing."""
    
    while True:
        input("Press Enter to clear the clipboard.")
        clear_clip()
        choice = input("Clear again? (y/n) ").lower()
        if choice not in yes_responses:
            break

if __name__ == "__main__":
    main()