#!/bin/bash

# I must first build the copy of the pharo enviroment to run the test
# Fill it in
pharo_path='/usr/local/lib/pharo/pharo-wk/NBCog'
pharo_image_dir='/usr/local/lib/pharo/pharo-wk/pharo-2.0/'
pharo_image='/usr/local/lib/pharo/pharo-wk/pharo-2.0/pharo.image' #.bkup
pharo_changes='/usr/local/lib/pharo/pharo-wk/pharo-2.0/pharo.changes' #.bkup

# In order to be working with only one test script
tema_file="HojaDeCalculo-run.st"
tests_file="HojaDeCalculo-Tests.st"


# Setup a fresh pharo image before running the test, so it won't be modified between runs
command="cp $pharo_image.bkup $pharo_image"
echo $command
$command

# Setup a fresh pharo changes before running the test, so it won't be modified between runs
command="cp $pharo_changes.bkup $pharo_changes"
echo $command
$command

# Relocate the delivered .st file to where it should be
file="Algo3Tp1.st"
file_test="Algo3Tp1-Tests.st"

if [ -f $file ]
then
    echo "Archivo de Algo3Tp1.st encontrado"
else
	echo "No se encontró el archivo Algo3Tp1.st"
	exit 1
fi


if [ -f $file ]
then
    echo "Archivo de Algo3Tp1-Test.st encontrado"
else
	echo "No se encontró el archivo Algo3Tp1-Test.st"
	exit 1
fi

command="cp $file $pharo_image_dir"
echo $command
$command

command="cp $file_test $pharo_image_dir"
echo $command
$command

# I build the command
command="$pharo_path -vm-display-null $pharo_image $file $file_test $tests_file $tema_file"
echo $command
$command

# Capture the result
exit_value=$?

# Cleanup
command="rm $pharo_image_dir$file $pharo_image_dir$file_test"
echo $command
$command

# Finally exit with the returned value
exit $exit_value

