*** Settings ***
Resource        resource.robot

Test Setup      Create User And Input Login Command


*** Test Cases ***
Login With Correct Credentials
    Input Credentials    kalle    kalle123
    Output Should Contain    Logged in

Login With Incorrect password
    Input Credentials    kalle    vaara
    Output Should Contain    Invalid username or password

Login With Nonexistent username
    Input Credentials    ${EMPTY}    pwd
    Output Should Contain    Username and password are required


*** Keywords ***
Create User And Input Login Command
    Create User    kalle    kalle123
    Input Login Command
