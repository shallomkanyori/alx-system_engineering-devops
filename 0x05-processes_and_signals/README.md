## Process and signals

####Task 0: What is my PID
[0-what-is-my-pid](0-what-is-my-pid) is a Bash script that displays its own PID.

###Task 1: List your processes
[1-list_your_processes](1-list_your_processes) is a Bash script that displays a list of currently running processes.
- Shows all processes, for all users, including those which might not have a TTY
- Displays in a user-oriented format
- Shows process hierarchy

####Task 2:  Show your Bash PID
[2-show_your_bash_pid](2-show_your_bash_pid) is a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

###Task 3: Show your Bash PID made easy
[3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy) is a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash` without using  `ps`.

####Task 4: To infinity and beyond
[4-to_infinity_and_beyond](4-to_infinity_and_beyond) is a Bash script that displays `To infinity and beyond` indefinitely.
- In between each iteration of the loop, `sleep 2`

####Task 5: Don't stop me now!
[5-dont_stop_me_now](5-dont_stop_me_now) is a Bash script that stops `4-to_infinity_and_beyond` process using `kill`

###Task 6: Stop me if you can
[6-stop_me_if_you_can](6-stop_me_if_you_can) is a Bash script that stops `4-to_infinity_and_beyond` process without using `kill` or `killall`

####Task 7: Highlander
[7-highlander](7-highlander) is a Bash script that displays:
- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a SIGTERM signal

####Task 8: Beheaded process
[8-beheaded_process](8-beheaded_process) is a Bash script that kills the process `7-highlander`.

####Task 9: Process and PID file
[100-process_and_pid_file](100-process_and_pid_file) is a Bash script that:
- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a SIGTERM signal
- Displays `Y U no love me?!` when receiving a SIGINT signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

####Task 10: Manage my process
[manage_my_process](manage_my_process) is a Bash script that:
- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for 2 seconds

[101-manage_my_process](101-manage_my_process) is a Bash (init) script that manages `manage_my_process`.
- When passing the argument `start`:
	- Starts `manage_my_process`
	- Creates a file containing its PID in `/var/run/my_process.pid`
	- Displays `manage_my_process started`
- When passing the argument `stop`:
	- Stops `manage_my_process`
	- Deletes the file `/var/run/my_process.pid`
	- Displays `manage_my_process stopped`
- When passing the argument `restart`
	- Stops `manage_my_process`
	- Deletes the file `/var/run/my_process.pid`
	- Starts `manage_my_process`
	- Creates a file containing its PID in `/var/run/my_process.pid`
	- Displays `manage_my_process restarted`
- Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed
