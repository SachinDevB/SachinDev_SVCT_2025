def findPoint(px, py, qx, qy):
    
    dx = qx - px
    dy = qy - py
    
    rx = qx + dx
    ry = qy + dy
    
    
    return rx, ry

 
n = int(input())

 
for _ in range(n):
    
    px, py, qx, qy = map(int, input().split())
    
    
    result = findPoint(px, py, qx, qy)
    print(result[0], result[1])
