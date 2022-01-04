class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        ))(()
        open =2
        close =3
        count = 2+1 = 3
        openClose =1
        
        """
        first_pass_chars = []
        # count = 0
        openClose = 0 #Balance of open bracket which are yet to be closed
        openBr = 0
        #first pass remove invalid ) char
        for i, c in enumerate(s):
            if c == ")":
                if openClose == 0:
                    # count += 1
                    continue #not add the c in output
                openClose -= 1
            elif c == "(":
                openBr += 1
                openClose += 1
                
            first_pass_chars.append(c)
        # count += openClose
        open_to_keep = openBr - openClose 
        # print(open_to_keep)
        res = []
        # 2nd pass remove open bracket = balance from the end
        for c in first_pass_chars:
            if c == "(" :
                if open_to_keep <= 0:
                    continue
                open_to_keep -= 1
            res.append(c)
        return "".join(res)

            