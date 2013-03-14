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

# Relocate the delivered .st file to where it should be
files_list=`ls | grep ^[0-9]\\\+.st$`
delivery_file=`echo $files_list | cut -d" " -f1`

command="cp $delivery_file $pharo_image_dir"
echo $command
$command

echo "st files found: $files_list"
echo "file used: $delivery_file"

digit=${delivery_file:4:1}
echo "ultimo digito del padron: $digit"

tema_file="tema1.st"

case $digit in
    [012] )
        tema_file="tema1.st";;
    [345] )
        tema_file="tema2.st";;
    [6789] )
        tema_file="tema3.st";;
	*)
		echo "nombre del archivo inesperado $delivery_file"
		exit 1
esac

# I build the command
command="$pharo_path -vm-display-null $pharo_image $delivery_file $tema_file"
echo $command
$command

# Capture the resultado
exit_value=$?

# Cleanup
command="rm $pharo_image_dir$delivery_file"
echo $command
$command

# Finally exit with the returned value
exit $exit_value

