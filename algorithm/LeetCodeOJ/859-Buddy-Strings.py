class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if A == B and len(set(list(A))) < len(A):
            return True
        
        if not A and not B:
            return False
        
        if len(A) != len(B):
            return False
        
        diff = []
        for i, c in enumerate(A):
            if B[i] != c:
                diff.append((i, c))
        
        print(diff)
        if len(diff) == 2:
            temp = list(B)
            print(temp)
            for i, c in diff:
                print(c)
                if c not in B:
                    print(123)
                    return False
                temp[i] = c
            print(temp)
            return ''.join(temp) == A
        
        return False