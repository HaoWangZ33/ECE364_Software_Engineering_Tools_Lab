#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-08-30 10:55:52 -0400 (Tue, 30 Aug 2016) $
#$Revision: 92599 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab01/mini_shell.bash $
#$Id: mini_shell.bash 92599 2016-08-30 14:55:52Z ee364a07 $

read -p "Enter a command: " command
while [[ $command != "quit" ]]
do
    if [[ $command == "hello" ]]
    then
        echo "Hello $USER"
        echo
        read -p "Enter a command: " command
    elif [[ $command == "compile" ]]
    then
        for file in $(ls *.c)
        do
            IFS='.' read -r -a array <<< $file
            name=${array[0]}
            gcc -Wall -Werror $file -o $name.o
            if (( $?==0 ))
            then
                echo "Compilation succeeded for: $file"
            else
                echo "Compilation failed for: $file"
            fi
        done
        echo
        read -p "Enter a command: " command
    elif [[ $command == "run" ]]
    then
        read -p "Enter filename: " filename
        read -p "Enter arguments: " arg
        if [[ -e $filename && -x $filename ]]
        then
            $filename $arg
        else
            echo "Invalid filename"
        fi
        echo
        read -p "Enter a command: " command
    else
        echo "Error: unrecognized input"
        echo
        read -p "Enter a command: " command
    fi
done
echo "Goodbye"
exit 0
