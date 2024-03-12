def crypto(file_name):
    with open(file_name,'r') as f:
        content = f.read()
        r_content = content.replace('secret','xxxxxx')
        print(r_content)
crypto("crypto.txt")

