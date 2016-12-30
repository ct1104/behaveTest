Feature: the login function of passport with variable input

Scenario Outline: with example
    given i have an valid "<mobile>"
    when input the mobile
    then get the "<code>"
    
    Examples: validmobile
    | mobile        | code        |
    | 13755199114   | 1234        |
    | 15801204212   | 1289        |