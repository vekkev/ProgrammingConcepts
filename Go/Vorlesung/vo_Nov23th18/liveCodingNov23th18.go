package vo_Nov23th18

import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

// G0 "Concurrency with gofunctions and channels"
// 24. November 2018 11:30 - 13:45 ONL 2 https://meet.lync.com/fhjoanneum-edu/lynctest10/KPL4JFMQ
//  execute this etherpad at your computer in the terminal using:
// curl 'https://houston.fh-joanneum.at/ep_moodle/p/g.j0sipZRZSFg892ea$moodle/export/txt' > /tmp/tst.go 2>/dev/null; go run /tmp/tst.go

// Anwesenheitsliste:
// jfeiner, asowinka, mleitold, asackl, lhaidacher, nsucher, nkaehling, aschadler, aklautzer,
// kschmid, cradlingmayer, dspanner,  bmaderer, akraus, cfressl, lleopold, afeichtinger,abektas, igrasenick, pdvorak, mwalzl,  jbaier, ekatic, jgassner, ftrenchevski,hgschwend, lwechtitsch, sfilipovic, mklug, kkoch, asauer, lladinig,mtomberger, nolah,awagner, mprem, kgruber,  lsarcevic, akozlova, dreindl,mfeil

// See Here you soon at 11:30 :)

// Agenda:

// (1) Coding online by students: G, H, K, ...

// (a) Design overall idea (what is it good for?) E.g. "zahlen raten (Password Cracker)": Brute Force, Random, Rainbow-Tables, ... (today: simple one/two chars, or numbers 0000-9999, or ... )
// input? int / zahl der userin Bsp.: 17
// timeout vorgeben
// strategien: vergleichen mit (a) table v. werten [4, 55, 77, 27],
//                                            (b) 0,1,2,... schleife: brute force
//                                            (c) random
//                                            (d) ??? aufteilen / segementieren / ... binärsuche / ...
// hauptprog: -> einzelne Funkt (z.B.: 1. random-generator) -> result - gefunden
// hauptprog: -> einzelne Funkt (z.B.: 2. brute force) -> result - gefunden
// result wenn: lösung gefunden
// dann evtl. auch andere "worker" stoppen
// (b) Design relevant parts (functions, input, output, states, ..):
// z.B.: random: generiere zahlen, dann generierte zahl vergleichen mit user-input
// (c) Run a first Go-program (compile, run)
// (d) implement independent "Status-Output" - Functionality
// (e) implement workers/players/gamers - Functionality
// (f) main only starts concurrent tasks and finally reports results

// Coffee & coding until 13:30

// (2) Coding on you own: (1/2 - 1h?)
// (a)  sleep time <= random
// (b) collect values (number of calculations) of gofunctions

// (optional) improve code: design way to stop all gofunctions
// (optional) implement with another channel ( using switch... ): stop all running gofunctions

// 13:35 - 13:45 Besprechung


package main
import (
"fmt"
"strconv"
"time"
"math/rand"
)



func bruteforce(x int, start int, end int, channel chan int, progress chan int) {
	fmt.Println("searching from ", start, "to", end)
	for i := start; i < end; i++ {
		// until 13:35
		// (a) RANDOMIZE sleep time z.B.: 2-4 sec oder 0.1 bis 0.7 sec whatever
		tm := rand.Intn(10)
		time.Sleep(time.Duration(tm) * time.Millisecond)
		progress <- tm
		// st := rand.Int(1000)
		//time.Sleep(st* time.Millisecond)
		if x == i {
			fmt.Println(strconv.Itoa( x ),  "you are cracked")
			channel <- x
			//var temp = <-progress

			break
		} else {
			// fmt.Println("try again")
		}
	}
	channel <- -1
}
func main() {
	c := make(chan int)
	progress := make(chan int)
	var text string
	fmt.Print("Scanln. Enter text: ")
	fmt.Scanln(&text)
	x, _ := strconv.ParseInt(text, 10, 64)
	fmt.Println("with Scanln: ", text)
	print("We guess a number!\n")

	for i := 0; i < 10000; i++ { // segmentierung
		go bruteforce(int(x), i*1000, (i+1)*1000, c, progress) // 10 x concurrent
	}

	// live sum up values
	sum := 0
	for {
		//
		// select {                        case v = <- c1 :
		sum +=  <- progress
		fmt.Println("All together 'calculated' time: ",sum)
	}
	// Lsg folgt nächste Einheit....

	answer := <-c
	fmt.Println(progress)
	fmt.Println(answer)
}


// Auf Wiedersehen bis zum nächsten Mal.... schönes Wochenende...


