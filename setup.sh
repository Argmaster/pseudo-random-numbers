#!/bin/bash

# Find latest Python version
PYTHON_PATH=$(ls /usr/bin | grep -P '^python3\.[0-9]+$' | sort --version-sort | tail -n 1)

# Check if Python was found
if [[ -z "$PYTHON_PATH" ]]
then
    echo "Python not found"
    exit 1
fi

# Use the latest Python version to install Poetry
"/usr/bin/$PYTHON_PATH" -m pip install --user poetry

# Check if Poetry was installed successfully
if [[ $? -ne 0 ]]
then
    echo "Poetry installation failed"
    exit 1
fi

# Run poetry install --sync
"$HOME/.local/bin/poetry" install --sync

# Check if poetry install --sync was successful
if [[ $? -ne 0 ]]
then
    echo "poetry install --sync failed"
    exit 1
fi

echo Finished
exit 0