#!/bin/bash

# Check if the script is being run with necessary permissions
if [[ $EUID -ne 0 ]]; then
   echo "This script might require root permissions to delete folders. Run with sudo if needed."
fi

# Specify the directories to delete
TARGETS=("__pycache__" "media")

# Loop through each target and delete
for TARGET in "${TARGETS[@]}"; do
  echo "Deleting all '$TARGET' directories..."
  find . -type d -name "$TARGET" -exec rm -rf {} +
done

echo "Deletion complete!"
