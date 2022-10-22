class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        """
        1. Iterate through create list for letters and digits 
            Look at first entry to check if digit
        2. For each element in letter log list
            ["let1 art can"] -> ["art", "can", "let1"]
            ["let2 arts can"] -> ["arts", "can", "let2"]
            Sort by array 
            
        log_list = ["let1", "art", "can"]
        
        let_list = []
            
        """
        let_list = []
        dig_list = []
        
        for log in logs:
            log_list = log.split(" ")
            #print(log_list)
            if log_list[1].isdigit():
                dig_list.append(log)
            else:
                let_list.append(log)
        let_list.sort(key = lambda x:x.split()[0]) # Sort my start
        let_list.sort(key = lambda x:x.split()[1:]) # Sort my suffix
        return let_list + dig_list