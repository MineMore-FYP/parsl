package main

import (
	//"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	"strconv"

	//"io"
	"log"
	"time"
)

func SendValue(s string, c chan string) {
	//send value through channel c
	c <- s
}

func work(messages chan<- string) {
	messages <- "golangcode.com"
}

func pythonCall(progName string, dataset string) {
	cmd := exec.Command("python3", progName, dataset)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
	//time.Sleep(2 * time.Millisecond)
}

func pythonCallOneParam(progName string, dataset string, para string) {
	cmd := exec.Command("python3", progName, dataset, para)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
	//time.Sleep(2 * time.Millisecond)
}

func main() {

	//get input dataset location
	cmd := exec.Command("python", "-c", "from workflow import userScript; print userScript.inputDataset")
	//fmt.Println(cmd.Args)

	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	}
	//input dataset from disk
	inputDataset := string(out)[:len(out)-1]
	//fmt.Print(inputDataset)

	//get output dataset location
	cmd1 := exec.Command("python", "-c", "from workflow import userScript; print userScript.outputDataset")
	//fmt.Println(cmd1.Args)

	out1, err1 := cmd1.CombinedOutput()

	if err1 != nil {
		fmt.Println(err1)
	}
	//input dataset from disk
	outputDataset := string(out1)[:len(out1)-1]
	//fmt.Print(outputDataset)

	//get wait time from user script
	cmdWT := exec.Command("python", "-c", "from workflow import userScript; print userScript.waitTime")
	outWT, errWT := cmdWT.CombinedOutput()
	if errWT != nil {
		fmt.Println(errWT)
	}

	waitTimeUS := string(outWT)[:len(outWT)-1]
	fmt.Println(waitTimeUS)
	waitTime, errWTInt := strconv.Atoi(waitTimeUS)
	if errWTInt == nil {
		fmt.Println(waitTime)
	}

	///////////////////////////*****************SELECTION************************////////////////////////

	//select user defined cols
	go pythonCall("workflow/selection/selectUserDefinedColumns.py", inputDataset)
	fmt.Println("test1")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test2")
	fmt.Println("Select User Defined Columns Complete")

	//channel
	channel := make(chan string)
	defer close(channel)
	go SendValue(outputDataset, channel)
	output := <-channel
	time.Sleep(10000 * time.Millisecond)

	///////////////////////////*****************CLEANING************************////////////////////////

	//drop unique cols
	go pythonCall("workflow/cleaning/dropUniqueColumns.py", output)
	fmt.Println("test3")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test4")
	fmt.Println("Drop unique columns complete")

	//channel
	channel1 := make(chan string)
	defer close(channel1)
	go SendValue(outputDataset, channel1)
	output1 := <-channel1
	time.Sleep(10000 * time.Millisecond)

	//#drop columns according to user defined empty value percentage
	go pythonCall("workflow/cleaning/dropColumnsCriteria.py", output3)
	fmt.Println("test9")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test10")
	fmt.Println("Drop user defined rows complete")

	//channel
	channel5 := make(chan string)
	defer close(channel5)
	go SendValue(outputDataset, channel5)
	output5 := <-channel5
	time.Sleep(10000 * time.Millisecond)

	//drop rows according to user defined empty value percentage
	go pythonCall("workflow/cleaning/dropRowsCriteria.py", output5)
	fmt.Println("test11")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test12")
	fmt.Println("Drop row criteria complete")

	//channel
	channel6 := make(chan string)
	defer close(channel6)
	go SendValue(outputDataset, channel6)
	output6 := <-channel6
	time.Sleep(10000 * time.Millisecond)

	//#remove duplicate rows
	go pythonCall("workflow/cleaning/removeDuplicateRows.py", output6)
	fmt.Println("test13")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test14")
	fmt.Println("Remove duplicate rows complete")

	//channel
	channel7 := make(chan string)
	defer close(channel7)
	go SendValue(outputDataset, channel7)
	output7 := <-channel7
	time.Sleep(10000 * time.Millisecond)

	//mode for user defined columns
	go pythonCall("workflow/cleaning/missingValuesMode.py", output8)
	fmt.Println("test17")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test18")
	fmt.Println("Missing values mode complete")

	//channel
	channel9 := make(chan string)
	defer close(channel9)
	go SendValue(outputDataset, channel9)
	output9 := <-channel9
	time.Sleep(10000 * time.Millisecond)


	fmt.Println("test27")

	time.Sleep(60000 * time.Millisecond)
	fmt.Println("test28")
	fmt.Println("Workflow Complete")
}

