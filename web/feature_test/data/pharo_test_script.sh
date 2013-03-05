#!/bin/bash

# I must first build the copy of the pharo enviroment to run the test
# Fill it in
pharo_path='/usr/local/lib/pharo/pharo-wk/NBCog'
pharo_image_dir='/usr/local/lib/pharo/pharo-wk/pharo-2.0/'
pharo_image='/usr/local/lib/pharo/pharo-wk/pharo-2.0/pharo.image' #.bkup
pharo_changes='/usr/local/lib/pharo/pharo-wk/pharo-2.0/pharo.changes' #.bkup

# Setup a fresh pharo image before running the test, so it won't be modified between runs
command="cp $pharo_image.bkup $pharo_image"
echo $command
$command

# Setup a fresh pharo changes before running the test, so it won't be modified between runs
command="cp $pharo_changes.bkup $pharo_changes"
echo $command
$command

st_files="tema1.st"

# Relocate the delivered .st file to where it should be
st_to_be_tested=`ls|grep '\.st$'`
delivery_files=""
for file in $st_to_be_tested; do
	cp $file $pharo_image_dir
	delivery_files="$delivery_files $file"
	st_files="$file $st_files"
done

# I build the command
command="$pharo_path -vm-display-null $pharo_image $st_files"
echo $command
exit 1
$command

# Capture the resultado
exit_value=$?

# Cleanup
cd $pharo_image_dir
if [ "$delivery_files" != '' ]
	then
		command="rm $delivery_files"
		echo $command
		$command
fi

# Finally exit with the returned value
exit $exit_value

