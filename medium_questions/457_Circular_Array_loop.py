class Solution:
    def circularArrayLoop(self, arr: List[int]) -> bool:

        def find_next_index(arr, is_forward, current_index):
            direction = arr[current_index] >= 0

            if is_forward != direction: 
                return -1
            
            next_index = (current_index + arr[current_index])% len(arr)

            if next_index == current_index:
                return -1
            
            return next_index

        for i in range(len(arr)):
            is_forward = arr[i] >= 0
            slow, fast = i, i

            while True:
                slow = find_next_index(arr, is_forward, slow)
                fast = find_next_index(arr, is_forward, fast)

                if fast != -1:
                    fast = find_next_index(arr, is_forward, fast)
                
                if slow == -1 or fast == -1 or slow == fast:
                    break
                
            if slow != -1 and slow == fast:
                return True
        return False