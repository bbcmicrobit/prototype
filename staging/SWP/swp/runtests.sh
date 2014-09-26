#!/bin/bash

for i in `ls progs/*.p`; do 
   echo $i
   echo $i | sed -e "s/./=/g"
   ./P.sh $i
   echo
done