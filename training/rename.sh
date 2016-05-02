a=1
for i in *.txt; do
	newName=$(printf "%04d.jpg" "$a")
	mv -- "$i" "$newName"
	let a=a+1
done
