FILE_PATH="Budget-ID.in"
def search(chosed,index,depth,depth_lim,value,cost)->int:
    global budget,target_value,objs
    if depth>depth_lim or budget<cost:
        return 0
    if len(chosed) and mode[0]=='V':
        print(f"{{{' '.join(chosed)}}}. Value = {value}. Cost = {cost}.")
    if target_value<=value:
        print(f"Found solution {{{' '.join(chosed)}}}. Value = {value}. Cost = {cost}.")
       
        return 1
    if len(objs)<=index:
        return 0
    for i in range(index,len(objs)):
        stat=search(chosed+[objs[i][0]],i+1,depth+1,depth_lim,value+int(objs[i][1]),cost+int(objs[i][2]))
        if stat:
            return 1
    
    return 0

with open(FILE_PATH,"r") as f:
    line=f.readline().split()
    target_value=int(line[0])
    budget=int(line[1])
    mode=line[2]
    data=f.readlines()
    objs=[]
    for l in data:
        objs.append(l.split())
found=0
for d in range(len(objs)+1):
    if d and mode[0]=='V':
        print(f"Depth = {d}")
    stat=search([],0,0,d,0,0)
    if stat:
        found=1
        break
    if d and mode[0]=='V':
        print("")
    
if not found:
    print("No Solution")

    