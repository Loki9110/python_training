import csv
class l_item:
    def items(self):
        print("enter the type of item you want to buy:")
        c=input("1.monitors\t2.gpu\t3.keyboards")
        with open("items.csv","a",newline="") as file:
            a=csv.dictreader(file)
            if c=="monitors" or c =="1":
                for r in a:
                    if r =="monitors" or r=="1":
                        print(f'Item ::  {r['item']}   price :: {r['price']}  stock left :: {r['quan']}')
            elif r =="gpu" or r=="2":
                for r in a:
                    if row['cat'] == "gpu":
                        print(f'Item ::  {row['item']}   price :: {row['price']}  stock left :: {row['quan']}')
            elif c == "keyboards" or c == '3':
                for row in a:
                    if row['cat'] == "keyboards":
                        print(f'Item ::  {row['item']}   price :: {row['price']}  stock left :: {row['quan']}')
            else:
                print("enter valid option ")
                return 0


                    
