class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            new_row = [1]
            if triangle:
                last_row = triangle[-1]
                for j in range(len(last_row) - 1):
                    new_row.append(last_row[j] + last_row[j + 1])
                
                new_row.append(1)
            triangle.append(new_row)

        return triangle        

        