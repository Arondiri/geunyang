def safe_pawns(pawns: set) -> int:
  pawns = list(pawns)
    A = ['a','b','c','d','e','f','g','h']
    ranks = []
    files = []
    d = 0
    if len(pawns) == 0 or len(pawns) == 1:
        return d
    else:
        for i in range(len(pawns)):
            ranks.append(pawns[i][0])
            files.append(int(pawns[i][1]))
            for j in range(1,7):
                if ranks[i] == A[0]:
                    if files[i] > 1 and (A[1]+str(files[i]-1) in pawns):
                        d += 1
                        break
                elif ranks[i] == A[7]:
                    if files[i] > 1 and (A[6]+str(files[i]-1) in pawns):
                        d += 1
                        break
                elif ranks[i] == A[j]:
                    if files[i] > 1 and (A[j-1]+str(files[i]-1) in pawns or A[j+1]+str(files[i]-1) in pawns):
                        d += 1
                        break
        return d
