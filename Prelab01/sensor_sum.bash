#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-08-28 23:59:14 -0400 (Sun, 28 Aug 2016) $
#$Revision: 92550 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab01/sensor_sum.bash $
#$Id: sensor_sum.bash 92550 2016-08-29 03:59:14Z ee364a07 $

if [[ $# != 1 ]]
then
    echo "usage: sensor_sum.bash log"
elif [[ ! -r $1 ]]
then
    echo "error: $1 is not a readable file!"
else
    while read line; do
        name=${line%%-*}
        IFS=' ' read -r -a array <<< $line
        s1=${array[1]}
        s2=${array[2]}
        s3=${array[3]}
        ((sum=$s1+$s2+$s3))
        echo "$name $sum"
    done < $1
fi

exit 0
