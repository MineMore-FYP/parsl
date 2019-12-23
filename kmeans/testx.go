package main

import (
	//"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	"io"
	//"io/ioutil"
	"log"
	//"time"
	"strconv"
	//"reflect"
	"path/filepath"
	"bufio"
    	"encoding/csv"
	"encoding/json"
	//"io.ReadSeeker"
)


func simplePythonCall(progName string, itr string) string{
	cmd := exec.Command("python3", progName, itr)
	out, err := cmd.CombinedOutput()
    	if err != nil { fmt.Println(err); }
    	//fmt.Println(reflect.TypeOf(out))
	return string(out)
}

func removeIt(ss Accuracy_class, ssSlice []Accuracy_class) []Accuracy_class {
    for idx, v := range ssSlice {
        if v == ss {
            return append(ssSlice[0:idx], ssSlice[idx+1:]...)
        }
    }
    return ssSlice
}

type Accuracy_class struct {
    Clusters int64 `json:"clusters"`
    Accuracy float64 `json:"accuracy"`
}

func main(){
	
	for i := 1;  i<=10; i++ {
		
		var x = simplePythonCall("kmeans.py", strconv.Itoa(i))
		fmt.Println(x)
		
                fmt.Printf("Kmeans with clusters 2,3,4,5,6,7 ran for " + strconv.Itoa(i) + " time(s).\n")
        }

	var files []string

    	root := "/home/mpiuser/Documents/FYP/gdelt/kmeans/"
    	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
        	files = append(files, path)
        	return nil
    	})
    	if err != nil {
        	panic(err)
    	}

	var Accuracy_set []Accuracy_class

    	for _, file := range files {
        	//if directory ignore
		fi, err := os.Stat(file)
		    if err != nil {
			fmt.Println(err)
			return
		    }
		     
		    var mode = fi.Mode(); 
		    if mode.IsDir() == true {
			continue
		    }			


		csvFile, _ := os.Open(file)
		
    		reader := csv.NewReader(bufio.NewReader(csvFile))
		
		    for {
			line, error := reader.Read()
			if error == io.EOF {
			    break
			} else if error != nil {
			    log.Fatal(error)
			}
			var clusters int64
			var accuracy float64
			clusters, _ = strconv.ParseInt(line[0],10,0)
			accuracy, _ = strconv.ParseFloat(line[1],64)
			//fmt.Println(reflect.TypeOf(newc))
			Accuracy_set = append(Accuracy_set, Accuracy_class{
			    Clusters: clusters,
			    Accuracy: accuracy,
			})
		    }
		    
		    //Accuracy_set = removeIt(Accuracy_class{"No_of_clusters", "Accuracy"}, Accuracy_set)
		    
    	}
	accuracyJson, _ := json.Marshal(Accuracy_set)
	fmt.Println(string(accuracyJson))
	
}
