
def read_file(filename):
    lines = []
    with open(filename,'r',encoding = 'utf-8-sig') as f:
        for r in f:
            lines.append(r.strip())
        return lines


def convert(lines):
    new = []
    person = None
    Allen_word_count = 0
    Viki_word_count = 0
    Allen_sticker_count = 0
    Viki_sticker_count = 0
    Allen_image_count = 0
    Viki_image_count = 0
    for r in lines:
        s = r.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                 Allen_image_count += 1
            else:   
                for m in s[2:]:
                    Allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] =='貼圖':
                Viki_sticker_count += 1
            elif s[2] == '圖片':
                 Viki_image_count += 1
            else:
                for m in s[2:]:
                    Viki_word_count += len(m)     
    print('allen說了',Allen_word_count,'傳了',Allen_sticker_count)
    print('Viki說了',Viki_word_count,'傳了',Viki_sticker_count)
    print('Allen傳了',Allen_sticker_count,'個圖片')
    print('Allen傳了',Allen_sticker_count,'個圖片')
    return new

def write_file(filename,lines):
    with open(filename,'w') as f:
        for r in lines:
            f.write(r + '\n')



def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt',lines)
main()