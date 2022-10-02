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

 12-newest_files -  a script that displays the 10 newest files in the current directory.

Requirements:

One file per line
Sorted from the newest to the oldest

13-unique - a script that takes a list of words as input and prints only words that appear exactly once.

Input format: One line, one word
Output format: One line, one word
Words should be sorted

14-findthatword - Display lines containing the pattern “root” from the file /etc/passwd

15-countthatword - Display the number of lines that contain the pattern “bin” in the file /etc/passwd

16-whatsnext - Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

17-hidethisword - Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

18-letteronly - Display all lines of the file /etc/ssh/sshd_config starting with a letter.

include capital letters as well

19-AZ - Replace all characters A and c from input to Z and e respectively.

20-hiago -  a script that removes all letters c and C from input.

21-reverse -  a script that reverse its input

22-users_and_homes - a script that displays all users and their home directories, sorted by users.

100-empty_casks - a command that finds all empty files and directories in the current directory and all sub-directories.

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

101-gifs - a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep
