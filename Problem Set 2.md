## Problem Set 2

### Problem 1

#### A.

There neighbors with costs are:

{C,D,F}->Error(S)=22

{C,E,F}->Error(S)=16

{C,F,G}->Error(S)=11

{C,F,H}->Error(S)=9

{C}->Error(S)=1

{F}->Error(S)=10

So state {C} is the best neighbor.

In the next step, we will try to add another object to {C}, or delete C. Thus, we will stop the algorithm because state {C} is the local minimum.

#### B.

State Space: $2^N$. Because for each object there are two status: choose or don't choose

Maximal number of neighbors: $N$. Because for a not choosed object, we can choose next round. For a choosed object, we can remove next round. So there are $N$ possible neighbor.

## Problem 2

1. $\lnot A\lor \lnot B\lor \lnot C$
2. $ (\lnot C \lor \lnot D)\land (\lnot C \lor\lnot E)\land (D\lor E\lor C)$
3. $\lnot D \lor B$
4. $(\lnot D\lor \lnot E\lor \lnot B)\land(\lnot D\lor \lnot E\lor  A)$
5. $(\lnot D \lor E)\land(\lnot E \lor D)$



## Problem 3

S0:

- $\lnot A\lor \lnot B\lor \lnot C$
- $\lnot C \lor \lnot D$
- $\lnot C \lor\lnot E$
- $D\lor E\lor C$
- $\lnot D \lor B$
- $\lnot D\lor \lnot E\lor \lnot B$​
- $\lnot D\lor \lnot E\lor  A$
- $\lnot D \lor E$
- $\lnot E \lor D$

S1:{A=true}

- $\lnot B\lor \lnot C$​
- $\lnot C \lor \lnot D$
- $\lnot C \lor\lnot E$
- $D\lor E\lor C$
- $\lnot D \lor B$
- $\lnot D\lor \lnot E\lor \lnot B$
- Satisfied
- $\lnot D \lor E$
- $\lnot E \lor D$



S2:{A=true,B=true}

- $\lnot C$​
- $\lnot C \lor \lnot D$
- $\lnot C \lor\lnot E$
- $D\lor E\lor C$
- Satisfied
- $\lnot D\lor \lnot E$
- Satisfied
- $\lnot D \lor E$
- $\lnot E \lor D$


S3:{A=true,B=true,C=true}

- null
- $\lnot D$
- $\lnot E$
- Satisfied
- Satisfied
- $\lnot D\lor \lnot E$
- Satisfied
- $\lnot D \lor E$
- $\lnot E \lor D$

Failed, Roll back to S2 and set C=false

S3:{A=true,B=true,C=false}

- Satisfied
- Satisfied
- Satisfied
- $D\lor E$
- Satisfied
- $\lnot D\lor \lnot E$
- Satisfied
- $\lnot D \lor E$
- $\lnot E \lor D$

S4:{A=true,B=true,C=false,D=true}

- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- $\lnot E$
- Satisfied
- $E$
- Satisfied

Failed. Roll Back to S3 and select D=false.

Failed. Roll Back to S2 and select B=false.

S2:{A=true,B=false}

- Satisfied
- $\lnot C \lor \lnot D$
- $\lnot C \lor\lnot E$
- $D\lor E\lor C$
- $\lnot D \lor B$
- Satisfied
- Satisfied
- $\lnot D \lor E$
- $\lnot E \lor D$


S3:{A=true,B=false,C=true}

- Satisfied
- $\lnot D$
- $\lnot E$
- Satisfied
- $\lnot D$
- Satisfied
- Satisfied
- $\lnot D \lor E$
- $\lnot E \lor D$

S4:{A=true,B=false,C=true,D=false}

- Satisfied
- Satisfied
- $\lnot E$
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- $\lnot E $

S4:{A=true,B=false,C=true,D=false,E=false}

- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied
- Satisfied







So, A and C is true. BDE is false.