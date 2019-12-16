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

func pythonCall(progName string, inChannel chan <- string) {
	cmd := exec.Command("python3", progName)
	//cmd.Stdout = os.Stdout
	//cmd.Stderr = os.Stderr
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

func readLines(commandsArray [20]string, progName string){
    file, err := os.Open(progName)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    i := 0
    for scanner.Scan() {
        command := scanner.Text()
				if command[0:2] == "##" {
					commandsArray[i] = command[2:len(command)]
					i++
				}
    }
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
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
		fmt.Print(inputDataset)
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
		//input dataset from disk
		//check if empty
		outputDataset := string(out1)[:len(out)-1]
		fmt.Print(outputDataset)
	}

	//start module execution from here onwards

	numOfWorkflowStages = numOfFiles("workflow/userScripts")

	for i := 0; i < numOfFiles; i++ {
		//each userScript files

	}




	inChannelModule1 := make(chan string, 1)
	outChannelModule1 := make(chan string, 1)

	pythonCall("workflow/selection/selectUserDefinedColumns.py", inChannelModule1)
	messagePassing(inChannelModule1, outChannelModule1)
	fmt.Println(<-outChannelModule1)

	//inChannelModule2 := make(chan string, 1)
	outChannelModule2 := make(chan string, 1)

	pythonCall("workflow/cleaning/dropUniqueColumns.py", outChannelModule1)
	messagePassing(outChannelModule1, outChannelModule2)

	//fmt.Println("jskdfkjdh")
	fmt.Println(<- outChannelModule2)



}
