#!/bin/bash

# I must first build the copy of the pharo enviroment to run the test
# Fill it in
pharo_path='/usr/local/lib/pharo/pharo-wk/NBCog'
pharo_image_dir='/usr/local/lib/pharo/pharo-wk/pharo-2.0/'
pharo_image='/usr/local/lib/pharo/pharo-wk/pharo-2.0/pharo.image' #.bkup
pharo_changes='/usr/local/lib/pharo/pharo-wk/pharo-2.0/pharo.changes' #.bkup

# In order to be working with only one test script
tema_file="tp1.st"
tests_file="MaquinaDeCafe-Tests.st"


# Setup a fresh pharo image before running the test, so it won't be modified between runs
command="cp $pharo_image.bkup $pharo_image"
echo $command
$command

# Setup a fresh pharo changes before running the test, so it won't be modified between runs
command="cp $pharo_changes.bkup $pharo_changes"
echo $command
$command

# Relocate the delivered .st file to where it should be
files_list=`ls | grep ^[0-9]\\\+.st$`
delivery_file=`echo $files_list | cut -d" " -f1`

if [ -z $delivery_file ]
	then
		echo "No se pudo encontrar el archivo de la entrega."
		exit 1
fi

command="cp $delivery_file $pharo_image_dir"
echo $command
$command

echo "st files found: $files_list"
echo "file used: $delivery_file"

# I build the command
command="$pharo_path -vm-display-null $pharo_image $delivery_file $tests_file $tema_file"
echo $command
$command

# Capture the result
exit_value=$?

# Cleanup
command="rm $pharo_image_dir$delivery_file"
echo $command
$command

# Finally exit with the returned value
exit $exit_value

