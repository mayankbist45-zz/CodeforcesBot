for((i = 1100; i >= 1011; --i)); do
    echo $i
    A="file"
    A="${A}${i}"
    A="${A}.cpp"
    # g++ "$A" 
    output=$(g++ ${A} 2>&1 -DONLINE_JUDGE=1)
    if [[ $? != 0 ]]; then
    # There was an error, display the error in $output
    echo -e "Error:\n$output"
    else
    # Compilation successfull
    
    ./a.out < input.txt > out.txt   
    diff -q -i -Z output.txt out.txt
    fi
done

