import os

def main():
    file_pointer = open('./a.txt', 'r')
    line = None
    
    idx_line = 0
    while line != '':
        line = file_pointer.readline()
        if '1000/1000' and 'Epoch' in line :
            print(line)
        if '1000/1000' in line :
            print(line)
        
    file_pointer.close()
    
###################################################################################################################
# end
###################################################################################################################
if __name__=='__main__':
    main()