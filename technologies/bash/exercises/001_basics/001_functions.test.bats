#!/usr/bin/env bats

load '001_functions.sh'

@test "greet_user function outputs correct messages" {
    # Capture the output of the function
    run greet_user "Alice"
    
    # Check that both lines are in the output
    [ "${lines[0]}" = "Hello, lovelly Alice" ]
}

@test "greet_user function handles empty name" {
    run greet_user ""

    [ "${lines[0]}" = "Hello, lovelly " ]
}

@test "greet_user function with different names" {
    run greet_user "John"
    [ "${lines[0]}" = "Hello, lovelly John" ]
    
    run greet_user "Sarah"
    [ "${lines[0]}" = "Hello, lovelly Sarah" ]
}
