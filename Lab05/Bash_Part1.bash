#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-09-27 11:18:44 -0400 (Tue, 27 Sep 2016) $
#$Revision: 94061 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab05/Bash_Part1.bash $
#$Id: Bash_Part1.bash 94061 2016-09-27 15:18:44Z ee364a07 $

function func_a 
{
    # Fill out your answer here.
    return
}

function func_b
{
    output=$(diff foo1.txt foo2.txt)
    if [[ $output == "" ]]
    then
        echo "Files are simliar."
    else
    	echo "Files are different."
    return
}

function func_c 
{
    # Fill out your answer here
    return
}

function func_d 
{
    # Fill out your answer here
    return 
}

function func_e
{
    # Fill out your answer here
    return
}

#
# To test your function, you can call it below like this:
#
# func_b
#
