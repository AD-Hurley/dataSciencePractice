import statistics

stockHistory = {
    "info": [600,630,620],
    "ril": [1430,1490,1567],
    "mtl": [234,180,160]
}

def printStocks():
    for key, value in stockHistory.items():
        avg=statistics.mean(value)
        print(f"{key} ==> {value} avg: {round(avg,2)}")

def addToStocks():
    stock=input("Enter a stock name: ")
    if stock in stockHistory.keys():
        price=input("Enter a price: ")
        stockHistory[stock].append(float(price))
    else:
        price=input("Error: stock not found")

def main():
    usrInput=""
    while usrInput != "exit":
        usrInput=input("Choose and operation, <print>, <add>, or <exit>: ")
        if usrInput =="print":
            printStocks()
        elif usrInput =="add":
            addToStocks()
        elif usrInput == "exit":
            print("Goodbye")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()