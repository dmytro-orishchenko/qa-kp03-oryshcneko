*** Settings ***
Library    Process
Library    OperatingSystem
*** Variables ***
${cli}    /home/yurii/Documents/GitHub/qa-kp01-Severyn/lab3/main.py

*** Test Cases ***
Dir root create
    ${result} =    Run Process    python3   ${cli}    get    directory    name\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir inner create
    ${result} =    Run Process    python3   ${cli}    post    directory    parent\=root    name\=child    max_elems\=8
    Should Contain    ${result.stdout}   Status code: 201

Dir create not exists
    ${result} =    Run Process    python3   ${cli}    post    directory    parent\=root    name\=child    max_elems\=8
    Should Contain    ${result.stdout}   Status code: 400

Dir move
    ${result} =    Run Process    python3   ${cli}    patch    directory    name\=child    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir delete
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=child
    Should Contain    ${result.stdout}   Status code: 200

Dir delete not exists
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=child
    Should Contain    ${result.stdout}   Status code: 400



Buffer create
    ${result} =    Run Process    python3   ${cli}    post    bufferfile    parent\=root    max_size\=100    name\=bufferfile
    Should Contain    ${result.stdout}   Status code: 201

Buffer create already exists
    ${result} =    Run Process    python3   ${cli}    post    bufferfile    parent\=root    max_size\=100    name\=bufferfile
    Should Contain    ${result.stdout}   Status code: 400

Buffer read
    ${result} =    Run Process    python3   ${cli}    get    bufferfile        name\=bufferfile
    Should Contain    ${result.stdout}   Status code: 200

Buffer move
    ${result} =    Run Process    python3   ${cli}    patch    bufferfile    parent\=root    name\=bufferfile
    Should Contain    ${result.stdout}   Status code: 200

Buffer push
    ${result} =    Run Process    python3   ${cli}    patch    bufferfile    name\=bufferfile    append\=test_text
    Should Contain    ${result.stdout}   Status code: 201

Buffer consume
    ${result} =    Run Process    python3   ${cli}    patch    bufferfile    name\=bufferfile    consume\=true
    Should Contain    ${result.stdout}   Status code: 200

Buffer delete
    ${result} =    Run Process    python3   ${cli}    delete    bufferfile    name\=bufferfile
    Should Contain    ${result.stdout}   Status code: 200

Buffer delete not exists
    ${result} =    Run Process    python3   ${cli}    delete    bufferfile    name\=bufferfile 
    Should Contain    ${result.stdout}   Status code: 400



Bin create
    ${result} =    Run Process    python3   ${cli}    post    binaryfile    name\=binaryfile    parent\=root    info\=test
    Should Contain    ${result.stdout}   Status code: 201

Bin create already exists
    ${result} =    Run Process    python3   ${cli}    post    binaryfile    name\=binaryfile    parent\=root    info\=test
    Should Contain    ${result.stdout}   Status code: 400

Bin read
    ${result} =    Run Process    python3   ${cli}    get    binaryfile    name\=binaryfile
    Should Contain    ${result.stdout}   Status code: 200

Bin move
    ${result} =    Run Process    python3   ${cli}    patch    binaryfile    name\=binaryfile    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

Bin delete
    ${result} =    Run Process    python3   ${cli}    delete    binaryfile    name\=binaryfile
    Should Contain    ${result.stdout}   Status code: 200

Bin delete not exists
    ${result} =    Run Process    python3   ${cli}    delete    binaryfile    name\=binaryfile 
    Should Contain    ${result.stdout}   Status code: 400



Log create
    ${result} =    Run Process    python3   ${cli}    post    logtextfile    name\=logtextfile    parent\=root    info\=test
    Should Contain    ${result.stdout}   Status code: 201

Log create already exists
    ${result} =    Run Process    python3   ${cli}    post    logtextfile    name\=logtextfile    parent\=root    info\=test
    Should Contain    ${result.stdout}    Status code: 400

Log read
    ${result} =    Run Process    python3   ${cli}    get    logtextfile    name\=logtextfile
    Should Contain    ${result.stdout}   Status code: 200

Log move
    ${result} =    Run Process    python3   ${cli}    patch    logtextfile    name\=logtextfile    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

Log append
    ${result} =    Run Process    python3   ${cli}    patch    logtextfile    name\=logtextfile    append\=test1
    Should Contain    ${result.stdout}   Status code: 201

Log delete
    ${result} =    Run Process    python3   ${cli}    delete    logtextfile    name\=logtextfile
    Should Contain    ${result.stdout}   Status code: 200

Log delete not exists
    ${result} =    Run Process    python3   ${cli}    delete    logtextfile    name\=logtextfile 
    Should Contain    ${result.stdout}   Status code: 400