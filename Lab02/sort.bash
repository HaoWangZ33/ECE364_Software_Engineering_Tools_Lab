#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-09-06 10:55:07 -0400 (Tue, 06 Sep 2016) $
#$Revision: 93104 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab02/sort.bash $
#$Id: sort.bash 93104 2016-09-06 14:55:07Z ee364a07 $

if (( $# != 1 ))
then
    echo "Usage: ./sort.bash <filename>"
    exit 1
elif [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist."
    exit 2
else
    echo "The 5 fastest CPUs:"
    sort -t',' -k5 -n $1 | head -n 5
    echo
    echo "The 3 most efficient CPUs:"
    sort -t',' -k4 -n $1 | head -n 3
    echo
    echo "The CPUs with cache size 4:"
    sort -t',' -k5 -n $1 | while read line;
    do
        IFS=',' read -r -a array <<< $line
        if [[ "${array[1]}" == "4" ]]
        then
            echo "$line"
        fi
    done
    echo
    read -p "Enter a value for n: " num_n
    echo "The $num_n slowest CPUs:"
    sort -t',' -k5 -n -r $1 | head -n $num_n
    echo
    sort -t',' -k1,1 -k4,4 $1 >> sorted_CPI.txt
fi
exit 0
