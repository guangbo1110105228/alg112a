不算原創，根據要求完成拆解的8 puzzle game，並將4隻程式整併為8 puzzle game


第一題:
如果n是奇數，且無序數字（在狀態表示中）的數量是偶數，則問題可解
無序數字的數量是透過計算數字對 (i, j) 來測量，其中 1 ≤ i < j ≤ N-1 但postion(i) > position(j)
無序數字 = i < j 且 position(i) > position(j)

Input:    
3
[7 2 4 5 0 6 8 3 1]
[1 6 7 3 5 2 4 8 0]
[8 1 7 3 6 5 2 0 4]

Output:
YES
NO
YES

第二題:
將0(空格)依照上下左右順序移動，若0在最上即不能往上，因此第一行output為0向下的結果，第二行output為0向左的結果,第三行output為0向右的結果
若0在最下，則ouput上左右，最左(上下右)，最右(上下左)

Input:  
3
[0 1 2 3 4 5 6 7 8]
[1 2 3 4 0 5 6 7 8]
[5 3 4 2 8 1 7 0 6]

Output:
2
move 0 to down
[3 1 2 0 4 5 6 7 8]
move 0 to right
[1 0 2 3 4 5 6 7 8]

4
move 0 to up
[1 0 3 4 2 5 6 7 8]
move 0 to down
[1 2 3 4 7 5 6 0 8]
move 0 to left
[1 2 3 0 4 5 6 7 8]
move 0 to right
[1 2 3 4 5 0 6 7 8]

3
move 0 to up
[5 3 4 2 0 1 7 8 6]
move 0 to left
[5 3 4 2 8 1 0 7 6]
move 0 to right
[5 3 4 2 8 1 7 6 0]

第三題:
將0-8不重複隨機輸入array[9]裡，根據曼哈頓距離計算最後完成到[0 1 2 3 4 5 6 7 8]的距離
例如在平面上，坐標（x1, y1）的點P1與坐標（x2, y2）的點P2的曼哈頓距離為： d(x,y) = |x1 -x2| + |y1 - y2|
ps 0(空格)的distance不用計算

Input:  
3
[0 1 2 3 4 5 6 7 8]
[1 2 3 4 5 6 7 8 0]
[2 7 0 1 5 8 3 4 6]

Output:
0
12
12

第四題:
queue 先進先出
stack 先進後出

先輸入一個字串in還是out，如果輸入in的話讓使用者輸入0-8不重複隨機輸入array[9]裡，並輸入g、h的值，f = (g + h)
f最小的話，則對照的array排序為第一位
若f值相同的話，則依照queue(先進先出)的規則排序

假設[0 1 2 3 4 5 6 7 8](1,12)，f = 1 + 12 = 13
假設[0 2 3 4 5 6 7 8 1](1,13)，f = 1 + 13 = 14

ex:f = 12 跟 f = 13的狀況下， [0 1 2 3 4 5 6 7 8]會排在 [0 2 3 4 5 6 7 8 1]的前面

if(輸入 = in) 
輸出 "insert ok"

if(輸入 = out) 
移除最上層array資料，並將被移出的資料print出
當所有array都已經被移出則輸出 "queue is empty"


Input:
in
[0 1 2 3 4 5 6 7 8](1,12)
in
[0 2 3 4 5 6 7 8 1](1,13)
out
out
out

Output:
insert ok
[0 1 2 3 4 5 6 7 8]
insert ok
[0 2 3 4 5 6 7 8 1]
queue is empty
