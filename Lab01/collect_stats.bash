#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-08-30 10:06:17 -0400 (Tue, 30 Aug 2016) $
#$Revision: 92567 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab01/collect_stats.bash $
#$Id: collect_stats.bash 92567 2016-08-30 14:06:17Z ee364a07 $


if (( $# != 2 ))
then
    echo "Usage: ./collect_stats.bash <file> <sport>"
    exit 1
elif [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist"
    exit 2
else
    sum_ath=0
    sum_medal=0
    most=0
    name=' '
    while read line; do
        IFS=',' read -r -a array <<< $line
        if [[ ${array[1]} == $2 ]]
        then
            ((sum_ath=$sum_ath+1))
            ((sum_medal=$sum_medal+${array[2]}))
            if (( ${array[2]} > $most ))
            then
                ((most=${array[2]}))
                name=${array[0]}
            fi
        fi
    done < $1
    echo "Total athletes: $sum_ath"
    echo "Total medals won: $sum_medal"
    echo "$name won the most medals: $most"

fi
exit 0
