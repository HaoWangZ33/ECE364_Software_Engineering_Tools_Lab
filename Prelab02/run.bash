#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-09-04 21:24:37 -0400 (Sun, 04 Sep 2016) $
#$Revision: 93030 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab02/run.bash $
#$Id: run.bash 93030 2016-09-05 01:24:37Z ee364a07 $

if (( $# != 2 ))
then
    echo "Usage: ./run.bash <filename of simulator source code> <output filename>"
    exit 1
fi

IFS='.' read -r -a array <<< $1
name=${array[0]}
if [[ -e $name ]]
then
    rm $name
fi
gcc $1 -o $name
if (( $? != 0 ))
then
    echo "error: quick_sim could not be compiled!"
    exit 2
fi

if [[ -e $2 ]]
then
    read -p "$2 exists. Would you like to delete it? " choice
    if [[ $choice == 'y' || $choice == 'yes' ]]
    then
        rm $2
        filename=$2
    elif [[ $choice == 'n' || $choice == 'no' ]]
    then
        read -p "Enter a new filename: " filename
    fi
else
    filename=$2
fi

fast_name=' '
fast_exetime=99999999
fast_cache=0
fast_width=0
for cache in 1 2 4 8 16 32
do
    for width in 1 2 4 8 16
    do
        cpu='AMD Opteron'
        output=$($name $cache $width a)
        IFS=':' read -r -a array <<< $output
        CPI=${array[7]}
        exetime=${array[9]}
        echo "$cpu:$cache:$width:$CPI:$exetime" >> $filename
        if (( $exetime < $fast_exetime ))
        then
            fast_exetime=$exetime
            fast_name=$cpu
            fast_cache=$cache
            fast_width=$width
        fi

        cpu='Intel Core i7'
        output=$($name $cache $width i)
        IFS=':' read -r -a array <<< $output
        CPI=${array[7]}
        exetime=${array[9]}
        echo "$cpu:$cache:$width:$CPI:$exetime" >> $filename
        if (( $exetime < $fast_exetime ))
        then
            fast_exetime=$exetime
            fast_name=$cpu
            fast_cache=$cache
            fast_width=$width
        fi
    done
done
echo "Fastest tun time achieved by $fast_name with cache size $fast_cache and issue width $fast_width was $fast_exetime"
exit 0
