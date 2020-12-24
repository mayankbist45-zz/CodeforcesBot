for((i = 1; i <= 1; ++i)); do
    echo $i
    A = "file"
    A = "${A}${i}"
    A = "${A}.cpp"
    echo $A
    echo g++ -Werror "$A"
	g++ "$file"
	if [[ $? == 0 ]]; then
    	diff -w <(./a < input.txt) <(output.txt) || break
	fi
done
