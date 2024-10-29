mapping_info={}
start_mapping_info=False
assignment={}
with open("dpll.out","r") as f:
    for l in f:
        if start_mapping_info:
            idx,info=l.strip().split()
            idx=int(idx)
            mapping_info[idx]=info
            continue
        if l.strip()=="NO SOLUTION":
            with open("back_end.out","w") as f2:
                f2.write("NO SOLUTION")
            exit()

        idx=l.strip().split()[0]
        idx=int(idx)
        if idx==0:
            start_mapping_info=True
            continue
        assignment[idx]=l.strip().split()[1]
ans=[]
for key in assignment:
    if assignment[key]=="T" and mapping_info[key][0]=="J":
        ans.append(mapping_info[key])

with open("back_end.out","w") as f:
    for a in ans:
        f.write(a+"\n")