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

	inChannelModule1 := make(chan string, 1)
	outChannelModule1 := make(chan string, 1)

	if err != nil {
		fmt.Println(err)
	} else if out != nil {
		//input dataset from disk
		//inputDataset := string(out)[:len(out)-1]
		//fmt.Print(inputDataset)

		pythonCall("workflow/selection/selectUserDefinedColumns.py", inChannelModule1)
		messagePassing(inChannelModule1, outChannelModule1)

	}
	fmt.Println(<-outChannelModule1)


}
