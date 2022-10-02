Shell Inpu and Output Redirection, Shell Filters
Resources
Read or watch:

Shell, I/O Redirection
Special Characters
man or help:

echo
cat
head
tail
find
wc
sort
uniq
grep
tr
rev
cut
passwd (5) (i.e. man 5 passwd)


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
You are not allowed to use sed or awk

0-hello_world - a script that prints “Hello, World”, followed by a new line to the standard output.

1-confused_smiley - a script that displays a confused smiley "(Ôo)'.

2-hellofile - Display the content of the /etc/passwd file.

3-twofiles - Display the content of /etc/passwd and /etc/hosts

4-lastlines  -  Display the last 10 lines of /etc/passwd

5-firstlines - Display the first 10 lines of /etc/passwd

6-third_line - a script that displays the third line of the file iacta.

8-cwd_state - a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

9-duplicate_last_line - a script that duplicates the last line of the file iacta

10-no_more_js -  a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

11-directories - a script that counts the number of directories and sub-directories in the current directory.
