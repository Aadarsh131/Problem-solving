> ### Question:  
> Find the total area of two rectangles in 2d plane. The rectangles may overlap.
> Given is x1,y1, x2,y2 as the bottom-left (x1,y1) and top-right(x2,y2) coord of 1st rectangle and x3,y3, x4,y4 for 2nd rectangle similarily. 
> Find the total area of two rectangles after substracting the overlapped area if any.
>
> **<u>Test case</u>**:  
> **Sample Input**:  
> 1 1 3 4  
> 2 3 6 7  
> (first line: x1,y1, x2,y2; second line: x3, y3, x4, y4)  
> **Sample Output**:  
> 21

### Solution:
> Approach 1 (easy):
```cpp
int main(){
    int x1,x2, y1, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    int x3,x4, y3, y4;
    cin >> x3 >> y3 >> x4 >> y4;

    int Area1 = (x2-x1)*(y2-y1);
    int Area2 = (x4-x3)*(y4-y3);

    //check if rectangles overlap
    int a = (x4-x1);
    int b = abs(x2-x1)+abs(x4-x3);  

    int c = abs(y4-y1);
    int d = abs(y2-y1)+abs(y4-y3);
    if(b > a && d > c){
        //overlap occured
        int X=b-a;
        int Y=d-c;
        int overlapArea=X*Y;
        cout << Area1+Area2-overlapArea << endl;
    }
    else{
        //no overlap
        cout << Area1+Area2 << endl;
    }
}
```

> Approach 2:
```cpp
int main(){
    int x1,x2, y1, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    int x3,x4, y3, y4;
    cin >> x3 >> y3 >> x4 >> y4;

    int Area1 = (x2-x1)*(y2-y1);
    int Area2 = (x4-x3)*(y4-y3);

    int left = max(x1,x3);
    int right = min(x2,x4);
    int bottom= max(y1,y3);
    int top = min(y2,y4);
    int AreaIntersection=0;
    if(left < right && bottom < top) {
        AreaIntersection = (right - left) * ( top - bottom);
    }

    int ans = Area1 + Area2 - AreaIntersection;
    cout << ans << endl;
}
```
