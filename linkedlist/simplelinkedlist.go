package main

import (
	"fmt"
)

type Node struct {
	value int
	next  *Node
}

type Linkedlist struct {
	head *Node
}

func (l *Linkedlist) Append(value int) {
	node := &Node{value: value, next: nil}
	if l.head == nil {
		l.head = node
		return
	}

	currentNode := l.head
	for currentNode.next != nil {
		currentNode = currentNode.next
	}
	currentNode.next = node
}

func (l *Linkedlist) Prepend(value int) {
	node := &Node{value: value, next: nil}
	node.next = l.head
	l.head = node
}

func (l Linkedlist) PrintLinkedList() {
	currentNode := l.head
	for currentNode != nil {
		fmt.Println(currentNode.value)
		currentNode = currentNode.next
	}
}

func (l *Linkedlist) Remove(value int) {
	currentNode := l.head
	var lastNode *Node
	for currentNode != nil {
		if currentNode.value == value {
			if lastNode == nil {
				l.head = currentNode.next
			} else {
				lastNode.next = currentNode.next
			}
			break
		}
		lastNode = currentNode
		currentNode = currentNode.next
	}
}

func (l Linkedlist) CountNodes() {
	count := 0
	currentNode := l.head
	for currentNode != nil {
		count += 1
		currentNode = currentNode.next
	}
	fmt.Printf("Total number of nodes: %v\n", count)
}

func main() {
	l := Linkedlist{}
	l.Append(1)
	l.Append(2)
	l.Append(3)
	l.Append(4)
	l.Append(5)
	l.Prepend(0)
	l.PrintLinkedList()
	l.CountNodes()
	l.Remove(3)
	l.PrintLinkedList()
	l.CountNodes()
}
