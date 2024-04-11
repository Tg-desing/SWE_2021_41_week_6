from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    try:
        # please input list like "0 1 3 4" which seperate each element by space
        input_list = list(map(int, input("Enter the list: ").split()))
        input_target = int(input("Enter the target: "))
        output_list = twoSum(input_list, input_target)
        print("Output: " + str(output_list))
    except ValueError:
        print("Enter a integer number for list and target")
