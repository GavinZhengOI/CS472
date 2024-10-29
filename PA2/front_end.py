import sys
routes=[]
all_jumps=[]
all_pegs=[]
ans=[]
jump_id={}
peg_id={}

with open("input.in","r") as f:
    n,empty_hole=map(int,f.readline().split())
    for l in f:
        a,b,c=map(int,l.split())
        routes.append([a,b,c])# a->b->c
        routes.append([c,b,a])# c->b->a

for r in routes:
    for t in range(1,n-1):
        all_jumps.append([*r,t])# every element in all_jumps is like [a,b,c,t] where a->b->c at time t
        jump_id[(*r,t)]=len(all_jumps)

for p in range(1,n+1):
    for t in range(1,n):
        all_pegs.append([p,t])# every element in all_pegs is like [p,t] where p means peg and t means time
        peg_id[(p,t)]=len(all_pegs)+len(all_jumps)

jump_count=len(all_jumps)

for j in all_jumps: #Precondition axioms
    a,b,c,t=j
    ans.append([-jump_id[tuple(j)],peg_id[(a,t)]])
    ans.append([-jump_id[tuple(j)],peg_id[(b,t)]])
    ans.append([-jump_id[tuple(j)],-peg_id[(c,t)]])

for j in all_jumps: #Causal axioms
    a,b,c,t=j
    ans.append([-jump_id[tuple(j)],-peg_id[(a,t+1)]])
    ans.append([-jump_id[tuple(j)],-peg_id[(b,t+1)]])
    ans.append([-jump_id[tuple(j)],peg_id[(c,t+1)]])

for peg in all_pegs: #Frame axioms-A
    p,t=peg
    if t==n-1:
        continue
    lim=[-peg_id[(p,t)],peg_id[(p,t+1)]]
    for j in all_jumps:
        a,b,c,i=j
        if (b==p and t==i) or (a==p and t==i):
            lim.append(jump_id[tuple(j)])
    ans.append(lim)

for peg in all_pegs: #Frame axioms-B
    p,t=peg
    if t==n-1:
        continue
    lim=[peg_id[(p,t)],-peg_id[(p,t+1)]]
    for j in all_jumps:
        a,b,c,i=j
        if (c==p and t==i):
            lim.append(jump_id[tuple(j)])
    ans.append(lim)

for j1 in all_jumps: #One action at a time
    for j2 in all_jumps:
        if j1!=j2 and j1[3]==j2[3]:
            ans.append([-jump_id[tuple(j1)],-jump_id[tuple(j2)]])

for i in range(1,n+1): #Starting state
    if i==empty_hole:
        continue
    ans.append([peg_id[(i,1)]])

for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            ans.append([-peg_id[(i,n-1)],-peg_id[(j,n-1)]])



with open("frontend.out","w") as f:
    sys.stdout=f
    for a in ans:
        print(*a)
    print(0)
    for j in all_jumps:
        a,b,c,t=j
        print(f"{jump_id[tuple(j)]} Jump({a},{b},{c},{t})")
    for peg in all_pegs:
        p,t=peg
        print(f"{peg_id[tuple(peg)]} Peg({p},{t})")

