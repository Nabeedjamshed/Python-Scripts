def sample(file_name):
    with open(file_name,'r') as f:
        words = f.read().split()
        counts = [0,0,0,0]
        for i in words:
            length = len(i)
            if length <= 4:
                counts[length - 1] += 1
    return (f"Words of length 1 "
            f": {counts[0]}\nWords of length 2 "
            f": {counts[1]}\nWords of length 3 "
            f": {counts[2]}\nWords of length 4 "
            f": {counts[3]}\n")
print(sample('sample.txt'))



