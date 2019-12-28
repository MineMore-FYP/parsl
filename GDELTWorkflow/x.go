package main

import (
	//"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	//"os/exec"
	//"strconv"

	//"io/ioutil"
	//"log"
	//"time"
	"path/filepath"
	//"encoding/csv"
	//"io"
	"reflect"
)

func x(workflowNumber string) {

	var files []string
	var root string
	if workflowNumber == "1" {
		root = "/home/mpiuser/Documents/FYP/gdelt/rf/"		
	} else if workflowNumber == "3" {
		root = "/home/mpiuser/Documents/FYP/gdelt/kmeans/"	
	}
	/*
	cmd := exec.Command("python", "-c", "from workflow import userScript; print userScript.outputLocation3")
	out, err0 := cmd.CombinedOutput()
	if err0 != nil {
		fmt.Println(err0)
		// Exit with status 3.
    		os.Exit(3)
	}
	
	path := string(out)
    	subFolder := fmt.Sprintf("%s%s", path, "kmeans/")
	*/
	//root := string(out) + workflow
	//fmt.Println(reflect.TypeOf(root))
	err1 := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
        	files = append(files, path)
        	return nil
    	})
	if err1 != nil {
        	panic(err1)
    	}
	fmt.Println(files)
}

func main() {
	x("1")
}
