#!/usr/bin/env bats

@test "greet_user_read debug version" {
    run bash -c '
        source "'"$BATS_TEST_DIRNAME"'/002_functions_w_read.sh"
        printf "Alberto\n" | greet_user_read
    '
    
    [ "${lines[0]}" = "Hello user, can you tell me your name?" ]
    [ "${lines[1]}" = "Hello, lovely Alberto" ]
}
