## Problem Set 3

## Problem 1:

1. $\lnot In(B)\or \lnot In(D)$ and $\lnot In(F)\or \lnot In(H)$​
2. $In(B)\iff Order(B,1)\lor Order(B,2)\lor Order(B,3)\lor Order(B,4)$ and $In(D)\iff Order(D,1)\lor Order(D,2)\lor Order(D,3)\lor Order(D,4)$
3. $Order(A,1)\lor Order(B,1)\lor Order(C,1)\lor Order(D,1)\lor Order(E,1)\lor Order(F,1)\lor Order(G,1)\lor Order(H,1)$ and $Order(A,2)\lor Order(B,2)\lor Order(C,2)\lor Order(D,2)\lor Order(E,2)\lor Order(F,2)\lor Order(G,2)\lor Order(H,2)$
4. ${\forall V\in G},{I\leq K}, V\neq A, Order(A,I)\implies \lnot Order(V,I)$ and ${\forall V\in G},{I\leq K}, V\neq B, Order(B,I)\implies \lnot Order(V,I)$
5. $\forall I\leq K,I\neq 1,V\in G, Order(V,1)\implies \lnot Order (V,I)$ and $\forall I\leq K,V\in G,I \neq2, Order(V,2)\implies \lnot Order (V,I)$

## Problem 2

#### Constrain 1: Every tasks is executed and with in time limit

We need to make sure every task is executed, so we need to have $\forall T, \exists P, \exists I\leq M \text{ such that } Exec(T,P,I) \text{ is true}$​.

Example: For $T=1$, there must exist a $P,I$ that $Exec(1,P,I)$ is true

#### Constrain 2:  If there is an arc from U to V then U is executed before V.

$\forall U,\forall V, edge(U,V)\implies \exist t_1 \exist t_2\exist p_1\exist p2 \text{ such that } Exec(U,p_1,t_1) \land Exec(V,p_2,t_2)\land( t1<t2)$

Example: For $U=A$,$V=D$, $edge(U,V)=true$, implies that exist a pairs of $t_1,t_2,p_1,p_2$ that $Exec(A,p_1,t_1) \land Exec(D,p_2,t_2)\land( t1<t2)$

#### Constrain 3: No two tasks running on same processor at same time

If $Exec(U,P,T)$ is true, then there are no $V$ such that $Exec(V,P,T)$ is true.

Example: if $Exec(A,1,1)$ is true, then $Exec(B,1,1)$, $Exec(C,1,1)$ etc are all false.

#### Constrain 4: No tasks been execute twice

If $Exec(U,P,T)$ is true, then there is no $(P',T')\neq (P,T)$ such that $Exec(T,P',T')$ is true.

Example: if $Exec(A,1,1)$, then $Exec(A,1,2)$ and $Exec(A,1,3)$ and $Exec(A,1,4)$ etc are all false.

## Problem 3

1. $\forall p,\forall q ,(F(p,q)\implies F(q,p))$​
2. $\forall p,\forall q ,(C(p,q)\implies \lnot C(q,p))$
3. $\exist f,(F(A,f)\land F(B,f))$
4. $\forall c_1, (C(c_1,A)\implies\forall c_2 C(c_2,B)\land \lnot F(c_1,c_2))$
5. $\exist p\forall c, (C(D,f)\land C(c,B)\implies F(f,c))$​
6. $\forall f, (F(f,D)\implies \exist c,C(c,f))$
7. $\forall f, (F(f,A)\implies \exist c,\forall gc,C(c,f)\land \lnot C(gc,c))$
8. $\forall c,(C(c,B)\implies \forall gc,\lnot C(gc,c))$