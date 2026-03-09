*** Settings ***
Documentation     Simple example test

Library    ../libraries/custom_library.py

*** Variables ***
${NAME}    World

*** Test Cases ***
My First Test
     Say Hello    ${NAME}

Quick Hello Test
    Log To Console    Hello Robot Framework!