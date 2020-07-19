def main():
    
    lista = []
    i = int(0)
    n = int(input())
    for i in range(0, 10):
        lista.append(n)
        print("N["+str(i)+"] = " + str(lista[i]))
        n = n * 2
    

if __name__ == "__main__":
    main()