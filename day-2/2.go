package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func DayTwoPartTwo() {
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

		if IsSafeEnoughLevel(level) {
			safeLevels++
		}
	}

	fmt.Println(safeLevels)
	defer file.Close()
}

func IsSafeEnoughLevel(level []int) bool {
	if IsSafeLevel(level) {
		return true
	}

	for i := 0; i < len(level); i++ {
		levelWithoutOne := make([]int, 0, len(level)-1)
		levelWithoutOne = append(levelWithoutOne, level[:i]...)
		levelWithoutOne = append(levelWithoutOne, level[i+1:]...)

		if IsSafeLevel(levelWithoutOne) {
			return true
		}
	}
	return false
}
