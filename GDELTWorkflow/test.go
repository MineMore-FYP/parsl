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
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
	msg := ("Module Completed: " + progName)
	inChannel <- msg
}

func messagePassing(inChannel <- chan string, outChannel chan <- string ){
	msg := <- inChannel
	outChannel <- msg
}

func main(){

	//check if input location is available
	cmd := exec.Command("python", "-c", "from workflow import userScript; print userScript.inputDataset")
	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
		// Exit with status 3.
    os.Exit(3)
	}
	//input dataset from disk
	inputDataset := string(out)[:len(out)-1]
	fmt.Print(inputDataset)

	inChannelModule1 := make(chan string, 1)
	outChannelModule1 := make(chan string, 1)

	pythonCall("workflow/selection/selectUserDefinedColumns.py", inChannelModule1)
	messagePassing(inChannelModule1, outChannelModule1)
	fmt.Println(<-outChannelModule1)

	//inChannelModule2 := make(chan string, 1)
	outChannelModule2 := make(chan string, 1)

	pythonCall("workflow/cleaning/dropUniqueColumns.py", outChannelModule1)
	messagePassing(outChannelModule1, outChannelModule2)

	fmt.Println("jskdfkjdh")
	fmt.Println(outChannelModule2)

}
