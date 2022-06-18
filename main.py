from generator import Generator

if __name__ == '__main__':
    print("Please Type your Hardware Type:")
    print("     1. Desktop")
    print("     2. Laptop")
    print("     3. HEDT")
    print("     4. AMD YES!!!!!!")
    types = input("Type your choice: ")

    if types == "1":
        pass

    elif types == "2":
        print("Please Type your Processor Type:")
        types = '''
        1.Ivy Bridge(3th Gen)
        2.Haswell(4th Gen)
        3.Broadwell(5th Gen)
        4.Skylake(6th Gen)
        5.Kaby Lake(7th Gen)
        6.Coffee Lake and Whiskey Lake(8th Gen)
        7.Coffee Lake Plus and Comet Lake(9th Gen)
        8.Ice Lake(10th Gen)
        '''
        print(types)
        Generator('laptop', input("Type your choice: "))
