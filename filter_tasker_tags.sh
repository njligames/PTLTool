#!/bin/bash

plt='"platinum_tasker_coder"'
yourfilenames=`ls ./taskers/*.json`
for eachfile in $yourfilenames
do
    N=`jq '.tags | length' $eachfile`
    b=0
    for ((i = 0 ; i < $N ; i++ )); do
        name=`jq ".tags[$i].name" $eachfile`
        if [ "$name" == "$plt" ]; then b=1; fi
    done

    if [ $b -eq 1 ]
    then
        echo "$eachfile yes"
    else
        echo "$eachfile no"
    fi
done

