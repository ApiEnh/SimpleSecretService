# SimpleSecretService API

[SimpleSecretService.com](https://SimpleSecretService.com/)

Authors:
  [Peter Ashley](https://www.linkedin.com/in/petersouleashley/)

## API reference

Host: api.simplesecretservice.com  -  HTTPS only

### Session methods

Path: /session

Method: GET, POST (post also gets a session, use same parameters)<br>
Parameters:<br>
&nbsp;&nbsp;&nbsp;&nbsp;session: (optional) Previously returned session. Will be returned if still valid.<br>
&nbsp;&nbsp;&nbsp;&nbsp;user: (optional) Logon user to use if no or invalid session<br>
&nbsp;&nbsp;&nbsp;&nbsp;password: (optional) Logon password<br>
Return: New session or 404 (no session, no user/password) or 401 (logon fail)<br>
  
### Key value methods

Path: /value

Method: GET<br>
Parameters:<br>
&nbsp;&nbsp;&nbsp;&nbsp;session, user, password, key<br>
&nbsp;&nbsp;&nbsp;&nbsp;routeKey: (optional) allows override of HTTP method so GET can "PUT /value" to prevent CORS preflight<br>
Return: text value of key  or 404 (key not found) or 401 (logon fail)<br>

Method: PUT<br>
Parameters:<br>
&nbsp;&nbsp;&nbsp;&nbsp;session, user, password, key, value<br>
Return: 200 or 400<br>

Method: DELETE<br>
Parameters:<br>
&nbsp;&nbsp;&nbsp;&nbsp;session, user, password, key<br>
Return: 200 or 400<br>
  
### Key set methods

Path: /values<br>
Method: GET<br>
Parameters:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;session, user, password<br>
Return: JSON map of key values or 401 (logon fail)<br>

