#!/usr/bin/env bash
a=1
for i in *.jpg; do
	newName=$(printf "%04d.jpg" "$a")
	mv -- "$i" "$newName"
	let a=a+1
done
