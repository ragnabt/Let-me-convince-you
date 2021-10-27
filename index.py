def main():
    numbers = []
    with open("test.in", "r") as f:
        test_cases = f.readline()
        i = 0
        while i < int(test_cases):
            f.readline()
            line = f.readline().replace('\n', '')
            numbers.append(list(map(int, line.split(" "))))
            i += 1
    f.close()

    res = []
    for nums in numbers:
        i = 0
        yes = False
        qnty = len(nums)
        # print(qnty)
        while i <= len(nums) :
            summ = 0
            for n in nums[i:]:
                summ += n
                if summ == 0:
                    yes = True
                    break
            i += 1
        if yes:
            res.append('yes')
        elif not yes:
            res.append('no')

    textfile = open("test.out", "w")
    for element in res:
        textfile.write(element + "\n")
    textfile.close()
      

if __name__ == '__main__':
    main()