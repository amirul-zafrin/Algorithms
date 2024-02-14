package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func max(a, b int) int {
  if a>b {
    return a
  }
  return b
}

func main() {
  input, err := os.Open("input.txt")
  if err != nil {
    log.Fatal(err)
  }
  defer input.Close()

  scanner := bufio.NewScanner(input)

  currCal := 0
  maxCal := 0

  for scanner.Scan() {
    if len(scanner.Text()) > 0 {
      calories, err := strconv.Atoi(scanner.Text())
      if err != nil {
        log.Fatal(err)
      }
      currCal += calories
    } else {
      maxCal = max(maxCal, currCal)
      currCal = 0
    }
  }
  maxCal = max(maxCal, currCal)
  if err := scanner.Err(); err != nil {
    log.Fatal(err)
  }
  log.Println(maxCal)
}

