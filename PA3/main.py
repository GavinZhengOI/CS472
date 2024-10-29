import numpy as np
import random
with open("input.in","r",encoding="utf8") as f:
    s=f.read()
NDice,NSides,LTarget,UTarget,NGames,M=map(int,s.split())
win_count=np.zeros((LTarget,LTarget,NDice+1))
loss_count=np.zeros((LTarget,LTarget,NDice+1))

def roll_dice(k):
    """roll NDice dices (with NSides sides)"""
    result=sum([int(random.random()*(NSides+1)) for i in range(k)])
    return result

def choose_dice(x_points,y_points):
    best_k,max_p,T=0,0,0
    total_p=0
    f=np.zeros(NDice+1)
    for k in range(1,NDice+1):
        T+=win_count[x_points][y_points][k]+loss_count[x_points][y_points][k]
        if win_count[x_points][y_points][k]+loss_count[x_points][y_points][k]==0:
            p=0.5
        else:
            p=win_count[x_points][y_points][k]/(win_count[x_points][y_points][k]+loss_count[x_points][y_points][k])
        f[k]=p
        if p>max_p:
            max_p=p
            best_k=k
        total_p+=p
    p=np.zeros(NDice+1)
    s=total_p-max_p
    p[best_k]=(T*max_p+M)/(T*max_p+NDice*M)
    for k in range(1,NDice+1):
        if k!=best_k:
            p[k]=(1-p[best_k])*((T*f[k]+M)/(s*T+(NDice-1)*M))
    return random.choices([k for k in range(1,NDice+1)],p[1:])[0]

def play_game():
    x_points,y_points=0,0
    x_past_state,y_past_state=[],[]
    while x_points<LTarget:#y goes first
        x_points,y_points=y_points,x_points
        x_past_state,y_past_state=y_past_state,x_past_state
        ndice_roll=choose_dice(x_points,y_points)
        points=roll_dice(ndice_roll)
        x_past_state.append([x_points,y_points,ndice_roll])
        x_points+=points
    if x_points<=UTarget:#last player won
        for e in x_past_state:
            win_count[e[0]][e[1]][e[2]]+=1
        for e in y_past_state:
            loss_count[e[0]][e[1]][e[2]]+=1
    else:#last player lost (becasue overflow)
        for e in x_past_state:
            loss_count[e[0]][e[1]][e[2]]+=1
        for e in y_past_state:
            win_count[e[0]][e[1]][e[2]]+=1

for i in range(NGames):
    play_game()


for x in range(LTarget):
    for y in range(LTarget):
        k=choose_dice(x,y)
        print(k,end=" ")
    print()

for x in range(LTarget):
    for y in range(LTarget):
        k=choose_dice(x,y)
        tot=win_count[x][y][k]+loss_count[x][y][k]
        if tot==0:
            p=0
        else:
            p=win_count[x][y][k]/tot
        print(p,end=" ")
    print()


