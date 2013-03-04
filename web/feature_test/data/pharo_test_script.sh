#!/bin/bash

# I must first build the copy of the pharo enviroment to run the test
# Fill it in
workdir='/usr/local/lib/pharo/pharo-wk'
bkupdir='/usr/local/lib/pharo/pharo-wk-bkup'

# Setup a fresh pharo image before running the test, so it won't be modified between runs
cp $bkupdir/pharo-2.0/Pharo-2.0.image $workdir/pharo-2.0/

# Setup a fresh pharo changes before running the test, so it won't be modified between runs
cp $bkupdir/pharo-2.0/Pharo-2.0.changes $workdir/pharo-2.0/

# Copy the test.st script also from bkupdir
cp $bkupdir/pharo-2.0/tema1.st $workdir/pharo-2.0/

# Relocate the delivered .st file to where it should be
st_to_be_tested=`ls|grep '\.st'`

for file in $st_to_be_tested; do
	cp $file $workdir/pharo-2.0/
done

# To generate the list of test files I change to the directory where the image is
cd $workdir/pharo-2.0/

files_list=`ls|grep '\.st'`
concatenated_list=""
for i in $files_list; do
	concatenated_list="$concatenated_list $i"
done

# Now I move back to where the pharo cog is located
cd ..

# I build the command
command="./NBCog -vm-display-null ./pharo-2.0/Pharo-2.0.image $concatenated_list"
# And the invoke it
$command

# Capture the resultado
exit_value=$?

# Cleanup
cd $workdir/pharo-2.0/
rm $concatenated_list

# Finally exit with the returned value
exit $exit_value

