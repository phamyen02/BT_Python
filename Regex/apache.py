import sys
import re
def readfile_regex_image(filename):
    f =  open(filename, "r").read()
    content = f.read()
    jpgLineTextList = re.findall("GET (.*\.jpg)", content, re.MULTILINE)
    if(jpgLineTextList):
        domain = get_domain(filename)
        data = set(jpgLineTextList)
        inc = 1
        print ("Danh sách ảnh trong file: ")
        for path in data:
            print(f"{inc}. {domain}{path}")
            inc += 1
    else:
        print ("Không có link ảnh trong file")
def get_domain(filename):

    re_host = re.search("[\.](\w*(\.[a-z]{2,6}){1,2})$", filename)
    if re_host: domain = "http://"+re_host.groups()[0]
    else: domain = ""
    return domain
###
def main():
    if len(sys.argv) != 3:
        print('usage: ./apache.py {--filename} file')
        sys.exit(1)
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--filename':
        logs = readfile_regex_image(filename)
        print("\n".join(logs))
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()