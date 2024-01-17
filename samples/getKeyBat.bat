@echo off

for /f "delims=" %%a in ('curl -X "GET" "https://api.simplesecretservice.com/value?user=USER&password=PASSWORD!&key=KEY"') do (
    set "myVar=%%a"
)

echo %myVar%