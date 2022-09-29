# Shell permissions Directory

Requirements
General
Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 20.04 LTS
All your scripts should be exactly two lines long ($ wc -l file should print 2)
All your files should end with a new line (why?)
The first line of all your files should be exactly #!/bin/bash
A README.md file, at the root of the folder of the project, describing what each script is doing
You are not allowed to use backticks, &&, || or ;
All your files must be executable


0-iam_betty script - a script that switches the current user to the user betty.

1-who_am_i script - a script that prints the effective username of the current user.

2-groups script - a script that prints all the groups the current user is part of.

3-new_owner script -  a script that changes the owner of the file hello to the user betty.

4-empty script - a script that creates an empty file called hello.

5-execute script - a script that adds execute permission to the owner of the file hello.

6-multiple_permissions script - a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody script - a script that adds execution permission to the owner, the group owner and the other users, to the file hello

8-James_Bond script -  a script that sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions

