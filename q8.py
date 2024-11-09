input1 = ["File_1", "File_2", "File_3", "Files_10", "File_Fi10"]
input2 = len(input1)

res = -1


for file in input1:
    val = file.removeprefix("File_")

    try:
        n = int(val)
        res = max(n, res)
    except:
        continue

print(res)
