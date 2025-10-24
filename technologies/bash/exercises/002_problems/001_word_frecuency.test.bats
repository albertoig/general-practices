#!/usr/bin/env bats
load '001_word_frecuency.sh'

@test "greet_user_read debug version" {
    run word_frecuency files/001_word_frecuency.txt

    [ "${lines[0]}" = '      4 the' ]
    [ "${lines[1]}" = '      3 is' ]
    [ "${lines[2]}" = '      2 sunny' ]
    [ "${lines[3]}" = '      1 day' ]
}
