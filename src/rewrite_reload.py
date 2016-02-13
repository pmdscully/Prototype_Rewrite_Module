import time
import rewrite_reload2

def write_to_file(l, filename):
        f 		= open(filename,'w')
        for s in l:
                f.write( str(s) +"\n")
        f.close()


def read_file_to_list(filename):
    with open(filename, 'r') as f:
        data = f.read()
    l = data.splitlines()
    return l
	
def display(l):
    c=0
    for i in l:
        print(str(c)+":\t"+str(i))
        c+=1

def update_code( index, filename ):
    l = read_file_to_list(filename)
    l = l[:index] + ['        print("I added a line.")'] + l[index:]
    write_to_file(l, filename)
    return l


if __name__ == "__main__":
    while True:
        l = update_code(2, 'rewrite_reload2.py')
        #display(l)
        rewrite_reload2.editable_function()
        time.sleep(1)
        reload(rewrite_reload2)
