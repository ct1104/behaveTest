Feature: the login function of passport with variable input

Scenario: Stronger opponent
    given i have an valid mobile and a right code
    | mobile        | code        |
    | 13755199114   | 1234        |
    | 15801204212   | 1289        |
    when input mobile "13755199114"
    then get the code "1234"