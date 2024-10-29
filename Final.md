# Final Exam

## Part 1

### Problem 1

I'm going to use iterative deepening search (IDS). This is because when searching on a large board, the state space could be more than $2^{35}$ (Because if there are 35 holes, each holes can have a peg or don't have a peg). It will take a huge amount of memory if we want to store the all the state. Instead, if we use IDS, we only need to store all the state on a single path, which is far less than $2^{35}$​.

### Problem 2

A: $Put(3,2)\implies (Peg(2,2)\lor Peg(1,2)\lor Peg(5,2)\lor Peg(6,2))\land \lnot Peg(3,2)$

B: $Put(3,2)\implies Peg(3,3)$​

C: $\lnot Peg(6,4)\land Peg(6,5)\implies Jump(1,3,6,4)\lor Jump(4,5,6,4)\lor Put(6,4)$



### Problem 3

![IMG_43E013D03A97-1](/Users/zhengzihan/Downloads/IMG_43E013D03A97-1.jpeg)

The optimal strategy is: Use action A first, if its tail, you win directly. If it's head, use action B (cost 2) to win. The expected return is $\frac{1}{2}\times 8+\frac{1}{2}\times 6=7$





### Problem 4

![IMG_A9BD4A60ED17-1](/Users/zhengzihan/Downloads/IMG_A9BD4A60ED17-1.jpeg)

![CleanShot 2024-05-08 at 13.35.26@2x](/Users/zhengzihan/Library/Application Support/CleanShot/media/media_7I7z1O7lae/CleanShot 2024-05-08 at 13.35.26@2x.png)

The first one is going too slow(still at 1.9 after 5 steps) and the third one is going too fast(not stable). And the second case is decending in a good speed and gradually approch to convergence. I expect them to converge at -0.422.

### Problem 5

The learning rate of 1 will means model will only "consider" the current information. And use it to correct all previous data using current data. But it could sometimes cause overshoot.  When b approch infinity, it will no longer be a "soft" max but will become a "hard" max. In $P$, The option with highest  probability will got a probability that close to 1 and others will be close to 0.



### Problem 6

First, you should include all the feature in x. Also, you need to make sure $x$ and $z$(testing set) have different data. Because you want to do testing in data that is different from training data. Or you will have overfitting problem. $x$ dataset cannot be missing be cause its the "feature" data, without x, we have nothing to train on.  

### Problem 7

We refer cost c be lossely reffered as spring because it is similar with spring because it change parameters toward value that reduce loss. Global loss it defined as the aggregation of loss in every sample in the dataset. It is not accident to have same symbol because L both denote lliekly hood.And they both represent how good the model is. (prediction vs actual data).



### Problem 8

3 signals are spacial feature, local connectivity, share weight. local connectivity are connection between pixels and surrunding. Share weight meanse the weight used for processing input are same, the benefit is detecting same feature anywhere. And spacial feature means CNN can detect features from different part: higher layers can detect complex feature  and lower layer can detech low-level feature, this is also the benefit.



Padding add layers of zeros and stride means how far filter move each time. For no padding and normal stride, stride is 1 and padding is 0. For pooling layer, the stride is equal to the filter's size. For instance, for 3*3 filter, stride is 3.





### Problem 9

![IMG_FE6DE60294FD-1](/Users/zhengzihan/Downloads/IMG_FE6DE60294FD-1.jpeg)



The unit delay will take the input, and wait for a "cycle" and then output the data it takes as input. it shild the state forward in time. And it helps run to remember past data, This is why rnn need to have such architecture because it can remember the earilier information and memory is crucial for tasks like NLP because you need to know the previous text of a paragraph.