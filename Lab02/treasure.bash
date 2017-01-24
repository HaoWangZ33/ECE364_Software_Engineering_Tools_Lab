#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-09-08 15:09:34 -0400 (Thu, 08 Sep 2016) $
#$Revision: 93305 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab02/treasure.bash $
#$Id: treasure.bash 93305 2016-09-08 19:09:34Z ee364a07 $

if (( $# != 1 ))
then
    echo "Usage: ./treasure.bash <filename>"
    exit 1
else
    xcoor=0
    ycoor=0
    x=0
    y=0
    echo "(0,0)"
    line1=$(head -n1 $1)
    IFS=' ' read -r -a array <<< $line1
    first=${array[0]}
    xcoor=${first:0:1}
    ycoor=${first:1:2}
    while (( $xcoor != $x || $ycoor != $y))
    do
        countx=0
        #echo "$xcoor $ycoor     $x $y"
        while read line;
        do
            if (( $xcoor == $countx ))
            then
                IFS=' ' read -r -a array <<< $line
                loca=${array[$ycoor]}
                x=$xcoor
                y=$ycoor
                xcoor=${loca:0:1}
                ycoor=${loca:1}
                echo "($x,$y)"
            fi
            ((countx=$countx+1))
        done < $1
    done
    echo "Treasure found at: ($xcoor,$ycoor)"
fi
exit 0
