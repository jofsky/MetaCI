*** Settings ***
Library         Browser
Suite Teardown  Close browser  ALL
*** Test Cases ***
Example
    New Browser  chromium  headless=true
    New Page     https://the-internet.herokuapp.com/

    Wait until network is idle
    Take screenshot
