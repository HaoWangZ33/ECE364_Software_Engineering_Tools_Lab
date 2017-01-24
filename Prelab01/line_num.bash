#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-08-28 22:27:23 -0400 (Sun, 28 Aug 2016) $
#$Revision: 92501 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab01/line_num.bash $
#$Id: line_num.bash 92501 2016-08-29 02:27:23Z ee364a07 $

if [[ $# != 1 ]]
then
    echo "Usage: line_num.bash <filename>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 2
else
    num=1
    while read line; do
        echo "$num:$line"
        ((num=$num+1))
    done < $1
fi

exit 0
