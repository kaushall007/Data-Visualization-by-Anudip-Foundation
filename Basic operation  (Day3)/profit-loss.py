cp = float(input("enter cost price(Rs):"))
sp = float(input("enter selling price (Rs):"))
if (cp or sp) >= 0:
    if cp > sp:
        print("Loss of",(cp-sp),"Rs")
    elif sp > cp:
        print("Profit of",(sp-cp),"Rs")
    else:
        print("no profit no loss")
else:
    print("Invalid! cost")
    
