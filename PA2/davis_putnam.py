import sys
lim=[]
mx_idx=0
ans=[]
def dpll(cur_index,limit_list,cur_ans):
    global ans
    #print(cur_index,len(limit_list),cur_ans)
    """
        doing dpll algorithm
        Parameters:
            - cur_index: the variable that enumerating right now
            - limit_list: list of unsolved limits
            - cur_ans: current assignment
    """
    if len(limit_list)==0:
        ans=cur_ans.copy() #solution found
        for i in range(1,mx_idx+1):
            if not ((i in ans) or (-i in ans)):
                ans.append(-i)
        return 1
    if cur_index>mx_idx:
        return 0 #search failed
    
    possible_assignment=[-cur_index,cur_index] #positive means true, negative means false
    for a in possible_assignment:
        new_limit=[]
        invalid=False
        for l in limit_list:
            if a in l:#limit satisfied
                continue
            else: #didn't satisfied right now
                #print("hi")
                clause=l.copy()
                if -a in clause:
                    clause.remove(-a)
                if len(clause)==0:
                    invalid=True
                    break
                new_limit.append(clause) 
        if invalid:
            continue
        new_ans=cur_ans.copy()
        new_ans.append(a)
        re=dpll(cur_index+1,new_limit,new_ans)
        if(re):
            return 1

mapping_info=[]
start_mapping_info=False
with open("frontend.out","r") as f:
    for l in f:
        if start_mapping_info:
            mapping_info.append(l)
            continue
        ints=list(map(int,l.strip().split()))
        if ints[0]==0:
            start_mapping_info=True
            continue
        lim.append(ints)
        for e in ints:
            mx_idx=max(mx_idx,e)

re=dpll(1,lim,[])
with open("dpll.out","w") as f:
    sys.stdout=f
    if re==0:
        print("NO SOLUTION")
    else:
        for a in ans:
            val='T'
            if a<0:
                val='F'
            print(f"{abs(a)} {val}")
    print(0)
    for l in mapping_info:
        print(l.strip())
