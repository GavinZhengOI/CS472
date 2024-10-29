# Midterm

### Problem 1

A. DFS tree is the second part of the image.

B. BFS tree is the first part of image.

![image-20240306111647374](/Users/zhengzihan/Library/Application Support/typora-user-images/image-20240306111647374.jpg)

### Problem 2

{A}'s neighbors: {} {AB} {AC} {AD} {AE} {AF}   Best->{AF} 

{AF}'s neighbors: {A} {F} ..... Best->{ABF}

{ABF}'s neighbors: {AF} {BF} {AB}.... Best->{None}

So in the end we stuck at ABF. 

Algorithm end.

### Problem 3

A. $\lnot (In(A)\land In(D))$  equals to $\lnot In(A) \lor \lnot In(D)$

B. $Size(3)\implies \lnot Order(C,5)$

C. $Size(3)\implies Order(S_1,2)\lor Order(S_2,2)\lor Order(S_3,2)$. $S_i$ here represent $i$ th vertex in $S$. 

D. $(Total(2,4)\land Order(A,3))\implies Total(3,7)$

E. $Size(4)\implies AtLeastTarget(4)$

### Problem 4

${A=true}$
1. $\mathrm{B}$
2. $\mathrm{C} \vee \mathrm{E}$
3. $\mathrm{B} \vee \mathrm{D}$.
4. $\neg \mathrm{B} \vee \neg \mathrm{C}$
5. $\neg \mathrm{B} \vee \mathrm{C} \vee \neg \mathrm{E}$​




${A=true,B=true}$
1. $\mathrm{C} \vee \mathrm{E}$
2. $ \neg \mathrm{C}$
3. $ \mathrm{C} \vee \neg \mathrm{E}$



${A=true,B=true,C=true}$
1. $ \neg \mathrm{C}$
2. $ \mathrm{C} \vee \neg \mathrm{E}$​
False



${A=true,B=true,C=false}$
1. $ \mathrm{E}$
2. $ \neg \mathrm{E}$
False



${A=False}$
1. $ \neg \mathrm{C} \vee \mathrm{D}$
2. $ \mathrm{B} \vee \mathrm{C}$
3. $ \neg B$
4. $\mathrm{B} \vee \mathrm{D}$.
5. $\neg \mathrm{B} \vee \neg \mathrm{C}$
6. $\neg \mathrm{B} \vee \mathrm{C} \vee \neg \mathrm{E}$​.



${A=false,B=false}$
1. $ \neg \mathrm{C} \vee \mathrm{D}$
2. $  \mathrm{C}$
3. $ \mathrm{D}$​



${A=false,B=false,C=true,D=true,E=true}$​

Solution Found

### Problem 5

A. $\exist x,(R(Gina,x)\land A(x,y)\land T(Hazel,x)\land T(David,y))$

B. $\exist f,\forall t, (F(Hazel,f)\land T(Hazel,t))\implies R(f,t)$

C. $\forall t,T(David,t)\implies \lnot M(t,Hazel)$

D. $\exist t,T(Gina,t)\land M(t,Hazel)\land M(t,David)$

E. $\forall f, F(David,f)\implies \exist t , T(David,t)\land M(t,f)$
