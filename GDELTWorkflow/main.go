package main

import (
	//"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	//"strconv"

	//"io"
	"log"
	//"time"
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

func pythonCallNormal(progName string) {
	cmd := exec.Command("python3", progName)
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

	//check if input location is available
	cmd := exec.Command("python", "-c", "from workflow import userScript; print userScript.inputDataset")
	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	}else if out!=nil {
		//input dataset from disk
		inputDataset := string(out)[:len(out)-1]
		fmt.Print(inputDataset)
		pythonCallNormal("workflow/selection/selectUserDefinedColumns.py")

		//channel
		//creat chan here

	}

	//get chan as parameter to next function


/*


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
/*
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
	/*
	go pythonCall("workflow/cleaning/dropUniqueColumns.py", output)
	fmt.Println("test3")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test4")
	fmt.Println("Drop unique columns complete")
*/
}
