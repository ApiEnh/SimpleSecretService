# parameter1 = key or otherwise prompt
$keyname = $args[0]
if ("$keyname" -eq "") {
    $keyname = Read-Host "`r`nKeyname parameter empty. Enter keyname"
}

# Check if the session environment variable exists, if not prompt
# Since the session is stored in an environment variable you can run the program for a day without 
# needing to prompt again.
if ("$env:Session" -eq "") {
    echo "`r`nSimpleSecretService Session environment variable not found."

    $user = Read-Host "`r`nEnter user"
    $securePassword = Read-Host -AsSecureString "Enter password"
    $password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($securePassword))

    # get session
    $env:Session = (curl "https://api.simplesecretservice.com/session?user=$user&password=$password").Content
    echo "`r`nSession: $env:Session"

    # direct fetch option
    echo "`r`nyou can also fetch in single line without session using user and password"
    $SimpleSecret = (curl "https://api.simplesecretservice.com/value?user=$user&password=$password&key=$keyname").Content
    echo "Secret fetched directly: $SimpleSecret"
}

# fetch with session 
$SimpleSecret = (curl "https://api.simplesecretservice.com/value?session=$($env:Session)&key=$keyname").Content
echo "`r`nSecret fetched with cached session: $SimpleSecret`r`n"

