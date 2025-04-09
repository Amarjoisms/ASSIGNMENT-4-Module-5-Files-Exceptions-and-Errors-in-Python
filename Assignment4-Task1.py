try:
    file = open('sample.txt','r')
    read_line1 = file.readline()[:22]
    read_line2 = file.readline()[:27]
    print("Line1: "+read_line1)
    print("Line2: "+read_line2)
    file.close()
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found")
