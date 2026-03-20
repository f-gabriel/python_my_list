from my_list import My_List

def main():
    c_list = My_List()
    for i in range(5):
        c_list.add(i)

    
    print(c_list)
    print(c_list[2])

if __name__ == '__main__':
    main()


