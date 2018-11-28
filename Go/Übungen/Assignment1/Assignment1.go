package main

// Requirement for GO Upload 01 about Concurrency:
//
//
// a) Comments required: Add your Name
//    remove this comments or other unused lines of code
//
// b) Multithreading:
//    Simulate concurrent "downloading of x files with the size of 7 MB each"
//    return the final amount of MB downloaded.
//    REQUIRED: a go function for each download,
//             (concurrent) waiting 2 secs for each download
//              use of channels for synchronisation
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
	res = myalgo(input)                          // caluclate the result
	fmt.Printf("RESULT: '%v'", res)              // return the result
}

func startDownload(c chan int) {
	time.Sleep(2 * time.Second)
	c <- 7

}

func myalgo(input string) string { // input string
	val, _ := strconv.Atoi(input)
	sum := 0
	//fmt.Printf("Just if you need it... the value converted to integer: %d\n", val)

	ch := make(chan int)

	for i := 1; i <= val; i++ {
		go startDownload(ch)
	}

	for i := 1; i <= val; i++ {
		sum += <-ch
	}

	return strconv.Itoa(sum) // return string
}
