package main

import "fmt"

type artistData struct {
	Name  string
	Plays int
}

func selectionSort(artists *[]artistData) {
	array_length := len(*artists)
	for i := 0; i < (array_length - 1); i++ {
		smaller_index := i
		for j := i + 1; j < array_length; j++ {
			if (*artists)[j].Plays < (*artists)[smaller_index].Plays {
				smaller_index = j
			}
		}
		if smaller_index >= 0 {
			var smaller_play_count artistData = (*artists)[smaller_index]
			(*artists)[smaller_index] = (*artists)[i]
			(*artists)[i] = smaller_play_count
		}
	}
}

func main() {
	artists := []artistData{
		{"Artist A", 400},
		{"Artist B", 50},
		{"Artist C", 150},
		{"Artist D", 300},
	}
	selectionSort(&artists)
	fmt.Println(artists)
}
