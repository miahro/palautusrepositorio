*** Settings ***
Resource        resource.robot

Test Setup      Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    nimi    salasana1
    Output Should Contain    New user registered

Register With Too Short Username And Valid Password
    Input Credentials    ab    salasana1
    Output Should Contain    Username too short

Register With Valid Username And Too Short Password
    Input Credentials    nimi    salas1
    Output Should Contain    Password too short

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    kalle123
    Output Should Contain    User with username kalle already exists

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    nimi1    salasana1
    Output Should Contain    Username must be minimium 3 characted [a-z]

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    nimi    salasana
    Output Should Contain    Password must not contain only letters


*** Keywords ***
Input New Command And Create User
    Create User    kalle    kalle123
    Input New Command
