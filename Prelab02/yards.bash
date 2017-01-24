#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-09-04 17:42:24 -0400 (Sun, 04 Sep 2016) $
#$Revision: 92998 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab02/yards.bash $
#$Id: yards.bash 92998 2016-09-04 21:42:24Z ee364a07 $

if (( $# != 1 ))
then
    echo "Usage: yards.bash <filename>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
else
    max=0
    while read line; do
        IFS=' ' read -r -a array <<< $line
        name=${array[0]}
        unset array[0]
        array=("${array[@]}")
        count=${#array[*]}
        sum=0
        for item in ${array[*]}
        do
            ((sum=$sum+$item))
        done
        ((average=$sum/$count))
        var_sum=0
        for item in ${array[*]}
        do
            ((var_sum=$var_sum+($item-$average)*($item-$average)))
        done
        ((var=$var_sum/$count))
        echo "$name schools averaged $average yards receiving with a variance of $var"
        if (( $average > $max ))
        then
            max=$average
        fi
    done < $1
    echo "The largest average yardage was $max"
fi
exit 0
