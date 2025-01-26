package main

import (
	"fmt"
	"math"
	"sort"
)

func threesum(nums []int, target int) int {
	sort.Ints(nums)
	var ans int
	closest := float64(1<<32 - 1)
	high := len(nums) - 1

	for k := 0; k < (high - 1); k++ {
		remain := target - nums[k]
		for i, j := k+1, high; i < j; {
			current_sum := nums[i] + nums[j]
			current_closest := math.Min(float64(closest), math.Abs(float64(remain)-float64(current_sum)))
			if current_closest < closest {
				closest = current_closest
				ans = nums[k] + current_sum
			}
			if remain == current_sum {
				return ans
			} else if remain > current_sum {
				i++
			} else {
				j--
			}
		}
	}

	return ans
}

func main() {
	nums := []int{-1, 2, 1, -4}
	result := threesum(nums, 1)
	fmt.Println(result)
}
