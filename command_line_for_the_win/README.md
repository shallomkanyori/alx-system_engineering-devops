## Command line for the win

**Background Context**

[CMD CHALLENGE](https://cmdchallenge.com/) is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!


**Requirements**

Create a screenshot, showing that you completed the required levels. Push this screenshot with the right name to GitHub, in either the PNG or JPEG format. Additionally, demonstrate the use of the `SFTP` (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.


**Using the SFTP command-line tool.**

1. Take the screenshots of the completed levels as mentioned in the requirements.
2. Open a terminal or command prompt on your local machine.
3. Use the `SFTP` command-line tool to establish a connection to the sandbox environment:
	```
	sftp 3b84b4ffb1bd@3b84b4ffb1bd.923e441a.alx-cod.online
	3b84b4ffb1bd@3b84b4ffb1bd.923e441a.alx-cod.online's password:
	Connected to 3b84b4ffb1bd.923e441a.alx-cod.online.
	sftp>
	```
4. Navigate to the directory where you want to upload the screenshots:
	```
	sftp> cd /root/alx-system_engineering-devops/command_line_for_the_win
	sftp> pwd
	Remote working directory: /root/alx-system_engineering-devops/command_line_for_the_win
	sftp>
	```
5. Use the SFTP `put` command to upload the screenshots from your local machine to the sandbox environment:
	```
	sftp> put 0-first_9_tasks.png
	Uploading 0-first_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/0-first_9_tasks.png
	0-first_9_tasks.png									100%   55KB  64.3KB/s   00:00
	sftp>
	```
6. Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
7. Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the requirements.
