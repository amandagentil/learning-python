def main():
    
    N = int(input())
    x = 1

    for _ in range(N) :
        print(str(x) + " " + str(x + 1) + " " + str(x+2) + " " + "PUM")
        x = x + 4


if __name__ == "__main__":
    main()