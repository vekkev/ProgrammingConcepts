package main

// Requirement for GO Upload 02 about Concurrency Paradigms:
//
//
// a) Comments required: Add your Name
//    remove this comments or other unused lines of code
//
// b) Concurrency:
//    Simulate Producer/Consumer
//    REQUIRED: a producer creating values 1,2,3....
//              a consumer consuming every second values
//              the consumer stops after consuming max (given input) values
//              combine numbers to output an overall resulting string
//              use of buffered (3 "slots") channel for synchronisation
// NOTE: ONLY ONE OUTPUT is allowed
//       keep line 34: fmt.Printf("RESULT: '%v'", res)
//       remove / comment all other print statements in your code

import (
	"bufio" // input = we read (buffered) text from stdin
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	res := ""
	scanner := bufio.NewReader(os.Stdin)         // read from STDIN
	input, _ := scanner.ReadString('\n')         // read FIRST line
	input = strings.Replace(input, "\n", "", -1) // remove line break

	res = myalgo(input) // caluclate the result

	fmt.Printf("RESULT: '%v'", res) // return the result
}

//
// START -- YOUR CODE
//

func myalgo(input string) string { // input string e.g. "7"
	val, _ := strconv.Atoi(input)
	//fmt.Printf("Just if you need it... the value converted to integer: %d\n", val)

	//
	// add whatever functionality you need
	//
	return "TODO" // return string e.g.: "1234567"
}

//
// END -- YOUR CODE
//
