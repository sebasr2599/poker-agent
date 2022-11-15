from model import tree 
def main():
    ls = [1,10,1,11,1,13,1,12,1,1]
    tr = tree()
    print(tr.predict(ls))

if __name__ == "__main__":
    main()
