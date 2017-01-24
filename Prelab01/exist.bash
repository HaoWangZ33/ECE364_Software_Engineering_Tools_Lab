#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-08-28 22:04:15 -0400 (Sun, 28 Aug 2016) $
#$Revision: 92495 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab01/exist.bash $
#$Id: exist.bash 92495 2016-08-29 02:04:15Z ee364a07 $

for input in $@
do
    if [[ -r $input ]]
    then
        echo "File $input is readable!"
    elif [[ ! -r $input || ! -e $input ]]
    then
        touch $input
    fi
done

exit 0
