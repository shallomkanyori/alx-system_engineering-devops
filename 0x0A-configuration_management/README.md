## Configuration management

#### Task 0
[0-create_a_file.pp](0-create_a_file.pp) is a Puppet manifest that creates a file in `/tmp`.
Requirements:
- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

#### Task 1
[1-install_a_package.pp](1-install_a_package.pp) is a Puppet manifest that installs `flask` from `pip3`.
Requirements:
- Install `flask`
- Version `2.1.0`

#### Task 2
[2-execute_a_command.pp](2-execute_a_command.pp) is a Puppet manifest that kills a process named `killmenow`.
Requirements:
- Uses the `exec` Puppet resource
- Uses `pkill`
