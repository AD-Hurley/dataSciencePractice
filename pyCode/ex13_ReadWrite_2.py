stockData={}
fileOut=open('Output.txt','w')
fileOut.write('CompanyName,PE Ratio,PB Ratio\n')
with open("stocks.csv","r") as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        stockName = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        bookValue = float(tokens[3])
        peRatio = round(price/eps,2)
        pbRatio = round(price/bookValue,2)
        fileOut.write(stockName+','+str(peRatio)+','+str(pbRatio)+'\n')
