import random
FILE_PATH="Budget-HC.in"
with open(FILE_PATH,"r") as f:
    line=f.readline().split()
    target_value=int(line[0])
    budget=int(line[1])
    mode=line[2]
    retry=line[3]
    data=f.readlines()
    objs=[]
    for l in data:
        objs.append(l.split())

def calc_error(objs)->int:
    global budget
    global target_value
    cost=0
    value=0
    for o in objs:
        value+=int(o[1])
        cost+=int(o[2])
    return max(0,target_value-value)+max(0,cost-budget)
        
def search(objs,left,value,cost):
    objs.sort(key=lambda x:x[0])
    left.sort(key=lambda x:x[0])
    min_error=float('inf')
    min_args=[]
    if calc_error(objs)==0:
        print(f"Found solution: \n {{{' '.join([a[0] for a in objs])}}}. Value = {value}. Cost = {cost}. ")
        return 1
    if mode[0]=='V':
        print("Neighbors:")
    for e in left:#add 
        args=[objs+[e],[l for l in left if l!=e],value+int(e[1]),cost+int(e[2])]
        if mode[0]=='V':
            print(f"{{{' '.join([a[0] for a in args[0]])}}}. Value = {args[2]}. Cost = {args[3]}. Error = {calc_error(args[0])}")
        if(calc_error(args[0])<min_error):
            min_args=args
            min_error=calc_error(args[0])
    for e in objs:#remove
        args=[[o for o in objs if o!=e],left+[e],value-int(e[1]),cost-int(e[2])]
        if mode[0]=='V':
            print(f"{{{' '.join([a[0] for a in args[0]])}}}. Value = {args[2]}. Cost = {args[3]}. Error = {calc_error(args[0])}")
        if(calc_error(args[0])<min_error):
            min_args=args
            min_error=calc_error(args[0])
    if min_error>=calc_error(objs):
        return 0
    if mode[0]=='V':
        print(f"\nMove to {{{' '.join([a[0] for a in min_args[0]])}}}. Value = {min_args[2]}. Cost = {min_args[3]}. Error = {calc_error(min_args[0])}.")
    return search(*min_args)

found=0
for i in range(int(retry)):
    if mode[0]=='V':
        print("Randomly chosen starting state: ")
    st=[]
    left=[]
    value=0
    cost=0
    for o in objs:
        if(random.random()<0.5):
            st.append(o)
            value+=int(o[1])
            cost+=int(o[2])
        else:
            left.append(o)
    if mode[0]=='V':
        print(f"{{{' '.join([a[0] for a in st])}}}. Value = {value}. Cost = {cost}. Error = {calc_error(st)}.")
    stat=search(st,left,value,cost)
    if stat==0:
        if mode[0]=='V':
            print("Search failed.\n")
    else:
        found=1
        break
    
if found==0:
    print("No Solution")
