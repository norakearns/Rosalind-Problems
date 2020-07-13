seq = 'ABCDE'
num = 4

sequp: ''
i = 0
for i in range(len(seq)):
    j = 0
    for j in range(len(seq)):
        k = 0
        for k in range(len(seq)):
            m = 0
            for m in range(len(seq)):
                sequp = str(seq[i]+seq[j]+seq[k]+seq[m])
                print(sequp)