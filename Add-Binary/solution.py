class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        A, B = len(a) - 1, len(b) - 1
        binary = []

        while A >= 0 or B >= 0 or carry == 1:
            if A >= 0:
                carry += int(a[A])
                A -= 1
            
            if B >= 0:
                carry += int(b[B])
                B -= 1
            
            binary.append(str(carry % 2))
            carry = carry // 2
        
        return "".join(binary[::-1])
        
        