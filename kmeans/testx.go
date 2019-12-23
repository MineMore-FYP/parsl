package main

import (
	//"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	//"strconv"

	"io/ioutil"
	//"log"
	//"time"
	"strconv"
)


func simplePythonCall(progName string) [][]string {
	cmd := exec.Command("python3", progName)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os. Stderr
	if cmd.Stderr != nil { fmt.Println(cmd.Stderr); }
	//log.Println(cmd.Run())
	Accuaracy_array,_ := ioutil.ReadAll(cmd.Stdout)
	fmt.Println(Accuaracy_array)
	return Accuaracy_array
}


func main(){
	accuracy_array = [][]string
	for i := 1;  i<=10; i++ {
		//cmd := exec.Command("python3", "import kmeans; print kmeans.return_array")
    		//fmt.Println(cmd.Args)
    		//out, err := cmd.CombinedOutput()
    		//if err != nil { fmt.Println(err); }
    			//fmt.Println(string(out))
		//kmeans
		accuracy_array = simplePythonCall("kmeans.py")
		fmt.Println(accuracy_array)
                fmt.Printf("Kmeans with clusters 2,3,4,5,6,7 ran for " + strconv.Itoa(i) + " time(s).")
        }
}
