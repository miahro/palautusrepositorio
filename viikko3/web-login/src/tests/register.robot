*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Register User


*** Test Cases ***
Register With Valid Username And Password
    Set Username    ville
    Set Password    salasana1
    Set Confirmation    salasana1
    Submit Userdetails
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    ab
    Set Password    salasana1
    Set Confirmation    salasana1
    Submit Userdetails
    Register Should Fail With Message    Username too short

Register With Valid Username And Invalid Password
    Set Username    galle
    Set Password    salasana
    Set Confirmation    salasana
    Submit Userdetails
    Register Should Fail With Message    Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username    galle
    Set Password    salasana1
    Set Confirmation    salasana2
    Submit Userdetails
    Register Should Fail With Message    Passwords differ


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Submit Userdetails
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}

Register User
    Create User    kalle    kalle123
    Go To Register Page
    Register Page Should Be Open
