class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=['']*numRows
        current_row=0
        down=False
        for c in s:
            rows[current_row]+=c
            if current_row==0 or current_row==numRows-1:
                down=not down
            current_row+=1 if down else -1;    
        return ''.join(rows)