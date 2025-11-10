#!/bin/bash

greet_user () {
    local user_name="$1"
    echo "Hello, lovelly $user_name"
}

# Only execute if the script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "This script is starting!"
    read -r -p "Hello user, can you tell me your name? " user_name
    result=$(greet_user "$user_name")
    echo "The result is: $result"
fi
