# Homework 8: NLP, transformer model

## 1 Beam search

### 1

`
1: The reason why artificial intelligence is important is that ( -1.00) 
2: The reason why artificial intelligence is important is because (-1.32)
`

### 2

We need to choose the top k candidate from $k^2$ the possible path generated. For $k=2$, we need to choose 2 from 4 candidates.

`

Time Step 2:  

1: The reason why artificial intelligence is important is that it (-1.00, -0.98) 

2: The reason why artificial intelligence is important is that we (-1.00, -2.43) 

3: The reason why artificial intelligence is important is because it (-1.32, -1.00) 

4: The reason why artificial intelligence is important is because we (-1.32, -2.59)

`

We add sequences 1 and 3 because the chances are greatest.

### 3

```
\begin{tabular}{rllll}
\hline
   Time Step & Hypothesis 1   & Log Probability 1   & Hypothesis 2   & Log Probability 2   \\
\hline
           1 & that           & $-1.0$              & because        & $-1.32$             \\
           2 & it             & $-1.98$             & it             & $-2.32$             \\
           3 & is             & $-3.44$             & is             & $-3.72$             \\
           4 & the            & $-5.91$             & a              & $-5.96$             \\
           5 & only           & $-7.78$             & most           & $-8.18$             \\
           6 & way            & $-8.77$             & powerful       & $-10.2$             \\
           7 & to             & $-9.19$             & tool           & $-12.03$            \\
           8 & in             & $-13.24$            & for            & $-13.95$            \\
           9 & the            & $-14.27$            & our            & $-15.17$            \\
          10 & world          & $-15.13$            & daily          & $-17.33$            \\
          11 & .              & $-16.43$            & lives          & $-17.49$            \\
          12 & .              & $-16.43$            & .              & $-18.05$            \\
\hline
\end{tabular}
```



### 4

It's pretty good. At least correct in grammar.

### 5

```
\begin{tabular}{rll}
\hline
   Time Step & Hypothesis 1   & Log Probability 1   \\
\hline
           1 & that           & $-1.0$              \\
           2 & it             & $-1.98$             \\
           3 & is             & $-3.44$             \\
           4 & a              & $-5.81$             \\
           5 & way            & $-8.66$             \\
           6 & to             & $-9.29$             \\
           7 & make           & $-12.19$            \\
           8 & people         & $-14.41$            \\
           9 & more           & $-16.45$            \\
          10 & aware          & $-17.89$            \\
          11 & of             & $-18.09$            \\
          12 & their          & $-19.04$            \\
          13 & own            & $-20.63$            \\
          14 & capabilities   & $-23.41$            \\
          15 & .              & $-24.25$            \\
\hline
\end{tabular}
```

## 2 Word embedding

<img src="/Users/zhengzihan/Library/Application Support/CleanShot/media/media_D1tHvujxLd/CleanShot 2024-05-01 at 00.07.39@2x.png" alt="CleanShot 2024-05-01 at 00.07.39@2x" style="zoom: 25%;" />

<img src="/Users/zhengzihan/Library/Application Support/CleanShot/media/media_jhrwzcFOgL/CleanShot 2024-05-01 at 00.08.24@2x.png" alt="CleanShot 2024-05-01 at 00.08.24@2x" style="zoom:25%;" />

<img src="/Users/zhengzihan/Library/Application Support/CleanShot/media/media_WP5bS3wwRC/CleanShot 2024-05-01 at 00.08.58@2x.png" alt="CleanShot 2024-05-01 at 00.08.58@2x" style="zoom:25%;" />

## 3 Contextualised word representation

![CleanShot 2024-05-01 at 01.00.04@2x](/Users/zhengzihan/Library/Application Support/CleanShot/media/media_KPB66sSnCD/CleanShot 2024-05-01 at 01.00.04@2x.png)

![CleanShot 2024-05-01 at 01.00.31@2x](/Users/zhengzihan/Library/Application Support/CleanShot/media/media_DBsGz7rnxZ/CleanShot 2024-05-01 at 01.00.31@2x.png)

![CleanShot 2024-05-01 at 01.00.58@2x](/Users/zhengzihan/Library/Application Support/CleanShot/media/media_MUV7j67qJy/CleanShot 2024-05-01 at 01.00.58@2x.png)
