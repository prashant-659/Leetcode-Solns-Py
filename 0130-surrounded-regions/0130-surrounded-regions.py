class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R=len(board)
        C=len(board[0])
        visit=set()


        # To capture unurrounded regsions (O->T)
        #To capture surrounded regions (O-> X)
        #To uncapture undrrouned regions (T->0)





        def capture(r,c):
            if (r<0 or r==R or
               c<0 or c==C or 
               board[r][c]!='O'):
               return
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        




        for r in range(R):
            for c in range(C):
                if (board[r][c]=='O' and 
                r in [0,R-1] or c in [0,C-1]):
                    capture(r,c)

        for r in range(R):
            for c in range(C):
                if board[r][c]=='O':
                    board[r][c]="X"
        
        for r in range(R):
            for c in range(C):
                if board[r][c]=='T':
                    board[r][c]='O'
        

        