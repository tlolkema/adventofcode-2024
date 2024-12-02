package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func DayTwoPartOne() {
	file, err := os.Open("./day-2/input-full.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
	}

	scanner := bufio.NewScanner(file)
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}

	var safeLevels int
	for scanner.Scan() {
		line := scanner.Text()
		items := strings.Split(line, " ")

		var level []int
		for _, char := range items {
			num, err := strconv.Atoi(char)
			if err != nil {
				fmt.Println("Error converting string to int:", err)
			}
			level = append(level, num)
		}

		if IsSafeLevel(level) {
			safeLevels++
		}
	}

	fmt.Println(safeLevels)
	defer file.Close()
}

func IsSafeLevel(level []int) bool {
	var isIncreasing, isDecreasing bool
	for i := 0; i < len(level)-1; i++ {
		diff := level[i+1] - level[i]
		if diff == 0 || diff < -3 || diff > 3 {
			return false
		} else if diff > 0 {
			if isDecreasing {
				return false
			}
			isIncreasing = true
		} else {
			if isIncreasing {
				return false
			}
			isDecreasing = true
		}
	}
	return true
}
