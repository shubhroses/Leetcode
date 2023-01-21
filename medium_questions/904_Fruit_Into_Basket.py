class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Find the longest subarray in fruits made up of only 2 characters 

        Brute force:
            Start at every index, count length of array that only has two unique characters

        As soon as you see the third character and length is less than max, can increment the left pointer
        0 1 2 3 4
        1 2 3 2 2
        l
            r

        res = 0
        window = {1, 2}

        """
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
        # Once we finish the iteration, the indexes left and right 
        # stands for the longest valid subarray we encountered.
        return right - left + 1