class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        If the amount exceeds 1000 its invalid
        If it occurs within 60 minites of another transaction 
            t1 and t2
            abs(t1[1] - t2[1]) <= 60
            t1[0] == t2[0] same name
            t1[3] != t2[3] different cities 
            
        1. Create list of transactions
        2. Sort by time
        3. create {name : [[time, amount, city], ...]}
        4. For each name iterate through list and if time between adjacent nodes <= 60 add to invalid 
        """
        
        transList = [st.split(',') for st in transactions]
        
        nameToTrans = collections.defaultdict(list)
        for trans in transList:
            nameToTrans[trans[0]].append(trans[1:])
            
        res = []
        for name in nameToTrans.keys():
            sameNameTrans = nameToTrans[name]
            
            for i in range(len(sameNameTrans)):
                curTrans = sameNameTrans[i]
                
                itime = int(curTrans[0])
                iamount = int(curTrans[1])
                icity = curTrans[2]
                
                if iamount > 1000:
                    res.append(name+ "," + ",".join(nameToTrans[name][i]))
                    continue
                
                invalid = False
                
                for j in range(len(sameNameTrans)):
                    if j == i:
                        continue
                    jTrans = sameNameTrans[j]
                    jtime = int(jTrans[0])
                    jamount = int(jTrans[1])
                    jcity = jTrans[2]
                    
                    if abs(jtime - itime) <= 60 and jcity != icity:
                        invalid = True
                if invalid:
                    res.append(name+ "," + ",".join(nameToTrans[name][i]))
        
        return res         
                
            
            
            
            
        """
        l = 0
            r = len(sameNameTrans)-1
            
            while l <= r:
                lTime = int(sameNameTrans[l][0])
                rTime = int(sameNameTrans[r][0])
                
                lCity = sameNameTrans[l][2]
                rCity = sameNameTrans[r][2]
                
                rAmount = int(sameNameTrans[r][1])
                lAmount = int(sameNameTrans[l][1])
                
                if (l != r and lTime == rTime) or (rTime - lTime <= 60 and lCity != rCity):
                    for i in range(l, r+1):
                        res.append(name+ "," + ",".join(nameToTrans[name][i]))
                    l = r+1
                elif rAmount > 1000:
                    res.append(name+ "," + ",".join(nameToTrans[name][r]))
                    r-=1
                elif lAmount > 1000:
                    res.append(name+ "," + ",".join(nameToTrans[name][l]))
                    l+=1
                l+=1
        
        for r in range(len(sameNameTrans)):
                lTime = int(sameNameTrans[l][0])
                rTime = int(sameNameTrans[r][0])
                
                lCity = sameNameTrans[l][2]
                rCity = sameNameTrans[r][2]
                
                rAmount = int(sameNameTrans[r][1])
                
                if rAmount > 1000:
                    res.append(name+ "," + ",".join(nameToTrans[name][r]))
                elif rTime - lTime > 60:
                    l += 1
                    continue
                elif lCity != rCity:
                    for 
                    res.append(name+ "," + ",".join(nameToTrans[name][l]))
                    res.append(name+ "," + ",".join(nameToTrans[name][r]))
        
        i = 0
        while i < (len(nameToTrans[name])):
            if i != len(nameToTrans[name])-1 and abs(int(nameToTrans[name][i][0]) - int(nameToTrans[name][i+1][0])) <= 60 and nameToTrans[name][i][2] != nameToTrans[name][i+1][2]:
                res.append(name+ "," + ",".join(nameToTrans[name][i]))
                res.append(name+ "," + ",".join(nameToTrans[name][i+1]))
                i += 2
                continue
            elif int(nameToTrans[name][i][1]) > 1000:
                res.append(name+ "," + ",".join(nameToTrans[name][i]))
            i += 1
        """
        
                