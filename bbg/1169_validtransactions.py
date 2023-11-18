class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        name_dict = defaultdict(list)

        for transaction in transactions:

            templist = transaction.split(",")
            name, time, amount, city = templist[0], templist[1], templist[2], templist[3]
            name_dict[name].append((time,amount,city))


        ans = []

        for name, values in name_dict.items():
            values.sort(key = lambda x:int(x[0]))
            # print("sorted values" + str(values))

            idxes = set()

            for idx in range(len(values)):

                iterator = idx+1

                if int(values[idx][1]) > int(1000):
                    idxes.add(idx)
 
                #for every idx, check + 60 mins ahead init
                while iterator < len(values) and int(values[iterator][0]) - int(values[idx][0]) <= 60:
                    # print(int(values[iterator][0]) - int(values[idx][0]))
                    if values[iterator][2] != values[idx][2]:
                        # print(values[iterator])
                        # print(values[idx])
                        idxes.add(idx)
                        idxes.add(iterator)

                    iterator += 1 

            for idx in idxes:
                ans.append(",".join((name,values[idx][0], values[idx][1], values[idx][2])))

        return ans
    
         esm