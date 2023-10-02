if __name__ == '__main__':
    x = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name, score])

    x = [[n, s] for n, s in x if s > sorted(x, key = lambda x : x [1])[0][1]]

    x = [n for n, s in x if s == sorted(x, key = lambda x : x[1])[0][1]]

    for i in sorted(x):
        print(i)

    