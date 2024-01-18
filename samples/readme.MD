### OpenAI Full Chat GPT demo
```Python
python3 chatGpt.py
```
# Curl examples

### Curl
```
curl -X "GET" "https://api.simplesecretservice.com/value?user=USERNAME&password=PASSWORD!&key=MYKEYNAME"
```
### Linux variable
```
export secret="$(curl 'https://api.SimpleSecretService.com/value?user=USER&password=PASS!&key=NAME')"
```
### Powershell variable
```
$SimpleSecret = (curl "https://api.SimpleSecretService.com/value?user=$user&password=$password&key=$keyname").Content
```
### Windows batch file variable
```
for /f "delims=" %%a in ('curl -X "GET" "https://api.simplesecretservice.com/value?user=USER&password=PASSWORD!&key=KEY"') do (<
  set "myVar=%%a"
```
