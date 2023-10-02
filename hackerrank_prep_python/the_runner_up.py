if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    points = list(arr)
    
    maior = max(points)
    
    runner_up = max([n for n in points if n != maior])

    print(runner_up)

   


