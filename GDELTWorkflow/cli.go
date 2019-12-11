package main

import (
  "bufio"
  "fmt"
  "os"
  "log"
  "os/exec"
  //"strings"
)

func scanner() string {
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Scan()
  //fmt.Println(scanner.Text())
  return scanner.Text()
}

func appendFile(text string){
	f, err := os.OpenFile("workflow/userScript.py", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Println(err)
	}
	defer f.Close()
	if _, err := f.WriteString(text); err != nil {
		log.Println(err)
	}
}

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


func main() {
  fmt.Println("Enter input dataset location: ")
	inputDataset := scanner()
  fmt.Println(inputDataset)

  appendFile("#input location\ninputDataset = " + "\""+inputDataset + "\"\n")

  fmt.Println("Enter output folder location: ")
  outputLocation := scanner()
  fmt.Println(outputLocation)

  appendFile("#output locatiion\noutputLocation = " + "\"" + outputLocation + "\"\n")

  fmt.Println("Enter columns to select: ")
	selectColumns := scanner()

  appendFile("selectColumns = " + selectColumns + "\n")

  inChannelModule1 := make(chan string, 1)
	outChannelModule1 := make(chan string, 1)

	pythonCall("workflow/selection/selectUserDefinedColumns.py", inChannelModule1)
	messagePassing(inChannelModule1, outChannelModule1)
	fmt.Println(<-outChannelModule1)
/*
	//inChannelModule2 := make(chan string, 1)
	outChannelModule2 := make(chan string, 1)

	pythonCall("workflow/cleaning/dropUniqueColumns.py", outChannelModule1)
	messagePassing(outChannelModule1, outChannelModule2)

	//fmt.Println("jskdfkjdh")
	fmt.Println(<- outChannelModule2)
*/


}
