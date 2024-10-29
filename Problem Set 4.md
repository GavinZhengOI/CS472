# Problem Set 4

### Problem 1: 3 points

Rules:

1. $J(h a, h b, h c, t x) \wedge S(t x, t y) \Rightarrow P(h c, t y)$
2. $J(h a, h b, h c, t x) \wedge S(t x, t y) \Rightarrow E(h a, t y)$
3. $J(h a, h b, h c, t x) \wedge S(t x, t y) \Rightarrow E(h b, t y)$
4. $J(h a, h b, h c, t x) \wedge U(h d, h a) \wedge U(h d, h b) \wedge U(h d, h c) \wedge P(h d, t x) \wedge S(t x, t y) \Rightarrow P(h d, t y)$
5. $J(h a, h b, h c, t x) \wedge U(h d, h a) \wedge U(h d, h b) \wedge U(h d, h c) \wedge E(h d, t x) \wedge S(t x, t y) \Rightarrow E(h d, t y)$​
6. $\mathrm{U}(\mathrm{ha}, \mathrm{hb}) \Rightarrow \mathrm{U}(\mathrm{hb}, \mathrm{ha})$



Inference:

Combining rule 1 with fact (11,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1\}$​ infer (21)  $\mathrm{P}(\mathrm{H} 1, \mathrm{~T} 2)$​

Combining rule 1 with fact (11,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1\}$ infer (22)  $\mathrm{E}(\mathrm{H} 2, \mathrm{~T} 2)$

Combining rule 1 with fact (11,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1\}$ infer (23)  $\mathrm{E}(\mathrm{H} 3, \mathrm{~T} 2)$

Combining rule 4,6 with fact (10,11,15,17,18,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1,\mathrm{hd} \rightarrow H4\}$ infer (24) $\mathrm{P}(\mathrm{H} 4, \mathrm{~T} 2)$



Combining rule 1 with fact (12,20) with subsitution $\{\mathrm{tx} \rightarrow T2, \mathrm{ty} \rightarrow T3,\mathrm{ha} \rightarrow H4,\mathrm{hb} \rightarrow H1,\mathrm{hc} \rightarrow H2\}$ infer (25)  $\mathrm{P}(\mathrm{H} 2, \mathrm{~T} 3)$

Combining rule 1 with fact (12,20) with subsitution $\{\mathrm{tx} \rightarrow T2, \mathrm{ty} \rightarrow T3,\mathrm{ha} \rightarrow H4,\mathrm{hb} \rightarrow H1,\mathrm{hc} \rightarrow H2\}$ infer (26)  $\mathrm{E}(\mathrm{H} 1, \mathrm{~T} 3)$

Combining rule 1 with fact (12,20) with subsitution $\{\mathrm{tx} \rightarrow T2, \mathrm{ty} \rightarrow T3,\mathrm{ha} \rightarrow H4,\mathrm{hb} \rightarrow H1,\mathrm{hc} \rightarrow H2\}$ infer (27)  $\mathrm{E}(\mathrm{H} 4, \mathrm{~T} 3)$​

Combining rule 5,6 with fact (12,14,16,18,20,23) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1,\mathrm{hd} \rightarrow H4\}$ infer (28) $\mathrm{E}(\mathrm{H} 3, \mathrm{~T} 3)$



### Problem 2: 3 points

 New predicates:

- $$P(h,c, t)$$​ Hole h has a peg(c color) in it at time t.

New Axioms:

1. $J(h a, h b, h c, t x) \wedge S(t x, t y) \wedge P(ha,ca,tx)\Rightarrow P(h c,ca, t y)$
2. $J(h a, h b, h c, t x) \wedge S(t x, t y) \Rightarrow E(h a, t y)$
3. $J(h a, h b, h c, t x) \wedge S(t x, t y) \Rightarrow E(h b, t y)$
4. $J(h a, h b, h c, t x) \wedge U(h d, h a) \wedge U(h d, h b) \wedge U(h d, h c) \wedge P(h d,cd, t x) \wedge S(t x, t y) \Rightarrow P(h d,cd, t y)$
5. $J(h a, h b, h c, t x) \wedge U(h d, h a) \wedge U(h d, h b) \wedge U(h d, h c) \wedge E(h d, t x) \wedge S(t x, t y) \Rightarrow E(h d, t y)$
6. $\mathrm{U}(\mathrm{ha}, \mathrm{hb}) \Rightarrow \mathrm{U}(\mathrm{hb}, \mathrm{ha})$



New Starting state:

7. $\mathrm{E}(\mathrm{H} 1, \mathrm{~T} 1)$
8. $\mathrm{P}(\mathrm{H} 2,PR, \mathrm{~T} 1)$
9. $P(\mathrm{H} 3,PW, \mathrm{~T} 1)$
10. $\mathrm{P}(\mathrm{H} 4,PB, \mathrm{~T} 1)$

New Inference:

Combining rule 1 with fact (11,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1,\mathrm{ca} \rightarrow PW\}$ infer (21)  $\mathrm{P}(\mathrm{H} 1,PW, \mathrm{~T} 2)$

Combining rule 1 with fact (11,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1,\mathrm{ca} \rightarrow PW\}$ infer (22)  $\mathrm{E}(\mathrm{H} 2, \mathrm{~T} 2)$

Combining rule 1 with fact (11,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1, \mathrm{ca} \rightarrow PW\}$ infer (23)  $\mathrm{E}(\mathrm{H} 3, \mathrm{~T} 2)$

Combining rule 4,6 with fact (10,11,15,17,18,19) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1,\mathrm{hd} \rightarrow H4,\mathrm{cd} \rightarrow PB\}$ infer (24) $\mathrm{P}(\mathrm{H} 4,\mathrm{PB} \mathrm{~T} 2)$



Combining rule 1 with fact (12,20) with subsitution $\{\mathrm{tx} \rightarrow T2, \mathrm{ty} \rightarrow T3,\mathrm{ha} \rightarrow H4,\mathrm{hb} \rightarrow H1,\mathrm{hc} \rightarrow H2, \mathrm{ca} \rightarrow PB\}$ infer (25)  $\mathrm{P}(\mathrm{H} 2,PB, \mathrm{~T} 3)$

Combining rule 1 with fact (12,20) with subsitution $\{\mathrm{tx} \rightarrow T2, \mathrm{ty} \rightarrow T3,\mathrm{ha} \rightarrow H4,\mathrm{hb} \rightarrow H1,\mathrm{hc} \rightarrow H2,, \mathrm{ca} \rightarrow PB\}$ infer (26)  $\mathrm{E}(\mathrm{H} 1, \mathrm{~T} 3)$

Combining rule 1 with fact (12,20) with subsitution $\{\mathrm{tx} \rightarrow T2, \mathrm{ty} \rightarrow T3,\mathrm{ha} \rightarrow H4,\mathrm{hb} \rightarrow H1,\mathrm{hc} \rightarrow H2, \mathrm{ca} \rightarrow PB\}$ infer (27)  $\mathrm{E}(\mathrm{H} 4, \mathrm{~T} 3)$

Combining rule 5,6 with fact (12,14,16,18,20,23) with subsitution $\{\mathrm{tx} \rightarrow T1, \mathrm{ty} \rightarrow T2,\mathrm{ha} \rightarrow H3,\mathrm{hb} \rightarrow H2,\mathrm{hc} \rightarrow H1,\mathrm{hd} \rightarrow H4\}$ infer (28) $\mathrm{E}(\mathrm{H} 3, \mathrm{~T} 3)$





### Problem 3: 4 points

A: It's $1/5*0.1+2/5*0.3+2/5*0.8=0.46$​

B: $1/5*0.1*0.1+2/5*0.3*0.3+2/5*0.8*0.8=0.294$​

C: $2(1/5*(2/4)*0.1*0.3+1/5*(2/4)*0.1*0.8+2/5*(2/4)*0.3*0.8+1/5*(1/4)*0.3*0.3+1/5*(1/4)*0.8*0.8)$=0.13

D: 0.46*0.46=0.21

E: P(Cat1|head)=$(1/5)*0.1$=0.02 P(Cat2|head)=$(2/5)*0.3$=0.12 P(Cat3|head)=(2/5)*0.8=0.32 so that when when we get one head up, P(Cat1)=0.02/0.46= 0.0434 $P(Cat2)=0.12/0.46=0.2608$

F: P(Cat1|tails)=$1/5*0.9=0.18$  P(Cat2|tails)=$2/5*0.7=0.28$   P(Cat3|tails)=$2/5*0.2=0.08$  So when it comes up tails, P(Cat1)=0.18/(0.18+0.28+0.08)=1/3  P(Cat2)=0.518518, P(Cat3)=0.148148

G: Same as A, it's 0.46

H: P(Cat1|up1|up2)=$1/5*0.1*0.1=0.002$  P(Cat2|up1|up2)=$2/5*0.3*0.3=0.036$   P(Cat3|up1|up2)=$2/5*0.8*0.8=0.256$   So that when we got two heads up, P(Cat1)=0.002/(0.002+0.036+0.256)=0.0068, P(Cat2)=0.1224, P(Cat3)=0.87