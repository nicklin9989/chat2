
def read_file(filename):
    lines = []
    with open(filename,'r',encoding = 'utf-8-sig') as f:
        for r in f:
            lines.append(r.strip())
        return lines


def convert(lines):
    new = []
    person = None
    for r in lines:
        if r == 'Allen':
            person = 'Allen'
            continue
        elif r == 'Tom':
            person = 'Tom'
            continue
        if person :
            pass

        new.append(person + ':' + r)
    return new

def write_file(filename,lines):
    with open(filename,'w') as f:
        for r in lines:
            f.write(r + '\n')



def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt',lines)
main()