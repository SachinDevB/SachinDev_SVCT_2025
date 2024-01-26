def connectingTowns(n, routes):
   
    total_routes = 1
    
  
    for r in routes:
        total_routes = (total_routes * r) % 1234567
    
    return total_routes

 
t = int(input())

 
for _ in range(t):
     
    n = int(input())
    
    
    routes = list(map(int, input().split()))
    
     
    result = connectingTowns(n, routes)
    print(result)
