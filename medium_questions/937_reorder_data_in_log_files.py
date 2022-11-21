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

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        All letter logs before digit logs
        Sort letter logs first by the contents and then by the identifier
        
        Step 1:
        digitLogs = ["dig1 8 1 5 1","dig2 3 6",]
        letterLogs = ["let1 art can","let2 own kit dig","let3 art zero"]
        
        Step 2: Sort letterLogs by identifiers
        digitLogs = ["dig1 8 1 5 1","dig2 3 6"]
        letterLogs = ["let1 art can","let2 own kit dig", "let3 art zero"]
        
        step 3: Sort letterLogs by contents
        digitLogs = ["dig1 8 1 5 1","dig2 3 6"]
        letterLogs = ["let1 art can","let3 art zero", "let2 own kit dig"]
        
        Step 4:
        return letterLogs + digitLogs

        """
        
        # Step 1
        digitLogs = []
        letterLogs = []
        
        for log in logs:
            elements = log.split()
            if elements[1].isdigit():
                digitLogs.append(elements)
            else:
                letterLogs.append(elements)
        
        # Step 2
        letterLogs.sort()
        
        # Step 3
        letterLogs.sort(key = lambda x: x[1:])
        
        # Step 4
        res = []
        for log in letterLogs:
            res.append(" ".join(log))
        
        for log in digitLogs:
            res.append(" ".join(log))
        return res