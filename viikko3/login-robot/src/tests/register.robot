*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  yess  yes12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  yes54321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  abcd1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  abc  abcd123
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abcd  abcdefgh
    Output Should Contain  Password must contain combination of numbers(0-9) and letters(a-z)

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command