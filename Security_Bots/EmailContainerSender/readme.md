# Information regarding installation or working

Consider following the following to have your own SMTP server for local development:

- Create a normal non-persistent server
  - docker run -p 3000:80 -p 2525:25 -d --name smtpdev rnwood/smtp4dev
- Create a server with persistent data
  - docker run -p 3000:80 -p 2525:25 -v ./smtp-data:/smtp4dev -d --name smtpdev rnwood/smtp4dev

You can test this server with the following PowerShell script

````Powershell
Send-MailMessage -To “test@test.com” -From “admin@test.com”  -Subject “MyMail” -Body “This is the test” -SmtpServer "localhost" -Port "2525"
````

Port 2525 is for the local SMTP messaging. 3000 is so you can see it on a UI.
