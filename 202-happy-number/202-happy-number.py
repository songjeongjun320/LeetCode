class Solution(object):
    def isHappy(self, n):
        first_input = n
        switch = True
        check_list = []

        # LeetCode에서 '/'가 안되는 문제

        while True:
            # Check that this # was occured before
            for _ in range(len(check_list)):
                if check_list[_] == n:
                    switch = False
                    return False
                    break
                else:
                    check_list.append(n)

            if n == 1 or switch == False:
                break 

            check_list.append(n)
            count = 1
            tmp = n
            updated_input = 0   

            while True:
                if tmp/10 < 1:
                    break
                else:
                    count += 1
                    tmp = tmp/10

            for _ in range(count,0,-1):
                a,b = divmod(n, 10**(_ - 1))
                updated_input += a*a
                n -= a * 10 ** (_ - 1)

            n = updated_input
        if n == 1:
            return True