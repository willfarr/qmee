echo "Creating a space seperated version of $1 ..."
cat $1 | tr "," " " > $1space.txt
echo "Done!"
exit