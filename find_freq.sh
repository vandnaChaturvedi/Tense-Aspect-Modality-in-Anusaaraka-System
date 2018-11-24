path=$HOME/TAM_Problem/prog/IITB.en-hi.hi
if [ -e $2 ]
then
	echo " File already exists "
else
	echo " File extracting the required words "
	grep -i -n " standing " $1 > $2
fi
if [ ! -s $2 ]
then
	echo " File is empty, has no matching sentence "
else
	python find_sent.py $2 $path > $2_1
fi
echo " Work completed "
