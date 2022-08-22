client_list={1:'Naksh',2:'Rohan',3:'Harry'}
loc_list={1:'Diet',2:' Excersice'}
print(loc_list)
try:
    for key,value in client_list.items():
        print(key,value)
    name=int(input("what you want :"))


    print("1 for loc")
    print("2 for Retrive")
    op=int(input())

    if op==1:
        print("what is loc here\n")
        print("1 for Diet and 2 for Excersice")
        name1=int(input())

        print("write here:",loc_list[name1])
        f=open(client_list[name]+ '_' +loc_list[name1]+ '.txt' ,'a')
        mywrite=input()
        f.write(mywrite)

    if op==2:
        print("What is loc here:\n")
        print("1 for Diet and 2 for Excersice")
        name1=int(input())

        f=open(client_list[name]+ '_'+loc_list[name1]+'.txt','+rt')
        a=f.readlines()
        # for key,value in loc_list.items():
        #     a=f.readlines()
        #     print(a)
        for line in a:
              print(line,'\n')
        f.close()

except Exception as e:
    print("wrong input")


