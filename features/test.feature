Feature: the login function of passport to jdb

Scenario: non_var
    given i have an mobile
    when i input the mobile number
    then i get code
    then i login system success