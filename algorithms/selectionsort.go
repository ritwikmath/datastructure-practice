package main

import "fmt"

type artistData struct {
	Name  string
	Plays int
}

func selectionSort(artists *[]artistData) {
	array_length := len(*artists)
	for i := 0; i < array_length; i++ {
		bigger_index := -1
		for j := i; j < array_length; j++ {
			if (*artists)[j].Plays > (*artists)[i].Plays {
				bigger_index = j
			}
			if bigger_index >= 0 {
				var bigger_play_count artistData = (*artists)[bigger_index]
				(*artists)[bigger_index] = (*artists)[i]
				(*artists)[i] = bigger_play_count
			}
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
