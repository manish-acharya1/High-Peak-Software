fh = open( "./input.txt" )
m, ind, goodies= int( fh.readline()[:-1][-1] ) - 1, 0, {}
fh.readline();fh.readline();fh.readline()
for each in fh:
    each.strip()
    item_price = each.split(":")
    goodies[ item_price[0] ] = int(item_price[1].strip())
goodies = {k: v for k, v in sorted(goodies.items(), key=lambda item: item[1])}
pl = list(goodies.values())
for i in range( 0, len(pl)-m ):
    if pl[i+m]-pl[i] < pl[ind+m]-pl[ind]: ind = i
fh = open("out.txt","w")
fh.write( "The goodies selected for distribution are:\n\n" )
for key in list(goodies.keys())[ind:ind+m+1]:
    fh.write( "{0} : {1}\n".format(key,goodies[key]))
fh.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(pl[ind+m]-pl[ind]))