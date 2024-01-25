def handshakes(n):
    return n * (n - 1) // 2

if __name__ == "__main__":
    t = int(input().strip())  

    for _ in range(t):
        n = int(input().strip())  
        result = handshakes(n)
        print(result)
