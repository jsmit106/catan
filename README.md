# Catan Board Layout Generator

Use the following command to generate a layout, replacing [seed] with a random integer:
```
clingo catan.lp --rand-freq=1 --seed=[seed]
```

This will generate an output similar to the following:
```
clingo version 5.4.1
Reading from catan.lp
Solving...
Answer: 1
board(5,1,blank,0) board(6,1,blank,0) board(7,1,blank,0) board(6,2,blank,0) ...
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 5.068s (Solving: 4.99s 1st Model: 4.99s Unsat: 0.00s)
CPU Time     : 5.027s
```

The line beginning with `board(5,1,blank,0)` is truncated and will contain all board placement information. These rules are space delimited and a basic regex parser could be written to read and format them. The board rules should be read as the following:
```
board(Row,Column,Resource,Value)
```
