#!/bin/bash

greet_user_read() {
    echo "Hello user, can you tell me your name?"
    read -r user_name
    echo "Hello, lovely $user_name"
}

# Only execute if the script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "This script is starting!"
    greet_user_read
fi
