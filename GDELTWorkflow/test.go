package main

import (
	"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	//"strconv"

	"io/ioutil"
	"log"
	//"time"
)

func pythonCall(progName string, inChannel chan <- string, workflowNumber string) {
	cmd := exec.Command("python3", progName, workflowNumber)
	out, err := cmd.CombinedOutput()
	log.Println(cmd.Run())

	if err != nil {
		fmt.Println(err)
		// Exit with status 3.
    os.Exit(3)
	}
	fmt.Println(string(out))
	//check if msg is legit
	msg := string(out)[:len(out)-1]
	//msg := ("Module Completed: " + progName)
	inChannel <- msg
}

func messagePassing(inChannel <- chan string, outChannel chan <- string ){
	msg := <- inChannel
	outChannel <- msg
}

func numOfFiles(folder string) int{
    files,_ := ioutil.ReadDir(folder)
    return len(files)
}

//reads a file and returns an array of comments beginning with ##
func readLines( progName string) [20]string{
		var commandsArray [20]string
    file, err := os.Open(progName)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    i := 0
    for scanner.Scan() {
        command := scanner.Text()
				//fmt.Println(len(command))
				if len(command) >1{
					//fmt.Println("dh")
					if command[0:2] == "##" {
						//fmt.Println(command[2:len(command)])
						commandsArray[i] = command[2:len(command)]
						i++
					}
				}
    }
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

		return commandsArray
}

func main(){

	//check if input location is available
	cmd := exec.Command("python", "-c", "from workflow import userScript; print userScript.inputDataset")
	out, err := cmd.CombinedOutput()

	if err != nil {
		fmt.Println(err)
		// Exit with status 3.
    os.Exit(3)
	} else if out == nil{
		os.Exit(3)
	} else {
		//input dataset from disk
		//check if empty
		inputDataset := string(out)[:len(out)-1]
		fmt.Print(inputDataset+"\n")
	}


	//check if output location is available
	cmd1 := exec.Command("python", "-c", "from workflow import userScript; print userScript.outputLocation")
	out1, err1 := cmd1.CombinedOutput()

	if err1 != nil {
		fmt.Println(err1)
		// Exit with status 3.
		os.Exit(3)
	} else if out1 == nil{
		os.Exit(3)
	} else {
		//output dataset from disk
		//check if empty
		outputDataset := string(out1)[:len(out1)-1]
		fmt.Print(outputDataset+"\n")
	}


	commandsArray := readLines("workflow/userScript.py")
	fmt.Println(commandsArray)

	//start module execution from here onwards
	inChannelModule1 := make(chan string, 1)
	outChannelModule1 := make(chan string, 1)
	pythonCall("workflow/"+commandsArray[0], inChannelModule1,"1")
	//pythonCall("workflow/selection/selectUserDefinedColumns.py", inChannelModule1)
	messagePassing(inChannelModule1, outChannelModule1)
	fmt.Println(<-outChannelModule1)
/*
	outChannelModule2 := make(chan string, 1)
	pythonCall("workflow/"+commandsArray[1], outChannelModule1, "1")
	//pythonCall("workflow/cleaning/dropUniqueColumns.py", outChannelModule1)
	messagePassing(outChannelModule1, outChannelModule2)
	fmt.Println(<- outChannelModule2)

	outChannelModule3 := make(chan string, 1)
	pythonCall("workflow/"+commandsArray[2], outChannelModule2, "1")
	//pythonCall("workflow/cleaning/dropColumnsCriteria.py", outChannelModule2)
	messagePassing(outChannelModule2, outChannelModule3)
	fmt.Println(<- outChannelModule3)

	outChannelModule4 := make(chan string, 1)
	//pythonCall("workflow/cleaning/dropRowsCriteria.py", outChannelModule3)
	pythonCall("workflow/"+commandsArray[3], outChannelModule3, "1")
	messagePassing(outChannelModule3, outChannelModule4)
	fmt.Println(<- outChannelModule4)

	outChannelModule5 := make(chan string, 1)
	pythonCall("workflow/"+commandsArray[4], outChannelModule4, "1")
	//pythonCall("workflow/cleaning/removeDuplicateRows.py", outChannelModule4)
	messagePassing(outChannelModule4, outChannelModule5)
	fmt.Println(<- outChannelModule5)

	outChannelModule6 := make(chan string, 1)
	//pythonCall("workflow/cleaning/missingValuesMode.py", outChannelModule5)
	pythonCall("workflow/"+commandsArray[5], outChannelModule5, "1")
	messagePassing(outChannelModule5, outChannelModule6)
	fmt.Println(<- outChannelModule6)
*/
/*
	outChannelModule7 := make(chan string, 1)
	pythonCall("workflow/"+commandsArray[6], outChannelModule6, "1")
	//pythonCall("workflow/transformation/normalize.py", outChannelModule6)
	messagePassing(outChannelModule6, outChannelModule7)
	fmt.Println(<- outChannelModule7)
*/
/*
	outChannelModule8 := make(chan string, 1)
	//pythonCall("workflow/transformation/splitIntoRows.py", outChannelModule8)
	pythonCall("workflow/"+commandsArray[6], outChannelModule6, "1")
	messagePassing(outChannelModule6, outChannelModule8)
	fmt.Println(<- outChannelModule8)
*/
}
