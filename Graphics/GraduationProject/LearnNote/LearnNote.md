## Part1. Marching cubes
* 一种等值面提取算法，那么首先就要给出一个值K，值小于K的点在等值面内部；值大于K的点在等值面外部；
    * Question：怎么计算三维点的值？用函数表达式？~~不太现实~~
* 考虑每一个小正方体（体素），考虑每一个顶点在等值面内部还是外部，共有$2^8 = 256$种情况。 
* [Marching cubes算法理解](https://zhuanlan.zhihu.com/p/48022195)
## Part2. 如何判断三维点在一个模型内部
## Part3. MITK