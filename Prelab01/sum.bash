#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-08-28 22:01:43 -0400 (Sun, 28 Aug 2016) $
#$Revision: 92491 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab01/sum.bash $
#$Id: sum.bash 92491 2016-08-29 02:01:43Z ee364a07 $

sum=0

for input in $@
do
    ((sum=$sum+$input))
done

echo "$sum"

exit 0
