with open("test.txt", "r") as f:
    lines = f.read().splitlines()


class Search:
    def __init__(self, char_matrix):
        self.m = char_matrix
        self.w = len(char_matrix[0])
        self.h = len(char_matrix)

    def hz(self, i, j):
        if j + 4 > self.w:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i][j + 1] == "M"
            a = self.m[i][j + 2] == "A"
            s = self.m[i][j + 3] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def bh(self, i, j):
        if j - 3 < 0:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i][j - 1] == "M"
            a = self.m[i][j - 2] == "A"
            s = self.m[i][j - 3] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def v(self, i, j):
        if i + 4 > self.h:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i + 1][j] == "M"
            a = self.m[i + 2][j] == "A"
            s = self.m[i + 3][j] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def bv(self, i, j):
        if i - 3 < 0:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i - 1][j] == "M"
            a = self.m[i - 2][j] == "A"
            s = self.m[i - 3][j] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def dr(self, i, j):
        if i + 4 > self.h or j + 4 > self.w:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i + 1][j + 1] == "M"
            a = self.m[i + 2][j + 2] == "A"
            s = self.m[i + 3][j + 3] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def dl(self, i, j):
        if i + 4 > self.h or j - 3 < 0:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i + 1][j - 1] == "M"
            a = self.m[i + 2][j - 2] == "A"
            s = self.m[i + 3][j - 3] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def bdl(self, i, j):
        if i - 3 < 0 or j - 3 < 0:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i - 1][j - 1] == "M"
            a = self.m[i - 2][j - 2] == "A"
            s = self.m[i - 3][j - 3] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def bdr(self, i, j):
        if i - 3 < 0 or j + 4 > self.w:
            return False
        else:
            x = self.m[i][j] == "X"
            m = self.m[i - 1][j + 1] == "M"
            a = self.m[i - 2][j + 2] == "A"
            s = self.m[i - 3][j + 3] == "S"

            if x and m and a and s:
                return True
            else:
                return False

    def search(self):
        sum = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.hz(i, j):
                    sum += 1
                if self.bh(i, j):
                    sum += 1
                if self.v(i, j):
                    sum += 1
                if self.bv(i, j):
                    sum += 1
                if self.dl(i, j):
                    sum += 1
                if self.dr(i, j):
                    sum += 1
                if self.bdr(i, j):
                    sum += 1
                if self.bdl(i, j):
                    sum += 1

        return sum


class Search2:
    def __init__(self, char_matrix):
        self.m = char_matrix
        self.w = len(char_matrix[0])
        self.h = len(char_matrix)

    def dr(self, i, j):
        if i + 2 > self.h or j + 2 > self.w:
            return False
        if i - 1 < 0 or j - 1 < 0:
            return False
        else:
            x = self.m[i][j] == "A"

            if x:
                if self.m[i - 1][j - 1] == "M":
                    if self.m[i + 1][j + 1] == "S":
                        return True
                if self.m[i - 1][j - 1] == "S":
                    if self.m[i + 1][j + 1] == "M":
                        return True

        return False

    def dl(self, i, j):
        if i - 1 < 0 or j + 2 > self.w:
            return False
        if i + 2 > self.h or j - 1 < 0:
            return False
        else:
            x = self.m[i][j] == "A"
            if x:
                if self.m[i + 1][j - 1] == "M":
                    if self.m[i - 1][j + 1] == "S":
                        return True
                if self.m[i + 1][j - 1] == "S":
                    if self.m[i - 1][j + 1] == "M":
                        return True

        return False

    def search(self):
        sum = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.dl(i, j) and self.dr(i, j):
                    sum += 1

        return sum


char_matrix = lines

search = Search(char_matrix)
search2 = Search2(char_matrix)

print(f"The sum is {search.search()}")
print(f"The second search is {search2.search()}")

