# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Here N is the number of accounts and K is the maximum length of an account.

# Time complexity: O(NKlogNK)

# In the worst case, all the emails will end up belonging to a single person. The total number of emails will be N*K, and we need to sort these emails. DFS traversal will take NK operations as no email will be traversed more than once.

# Space complexity: O(NK)O(NK)
# Building the adjacency list will take O(NK)O(NK) space. In the end, visited will contain all of the emails hence it will use O(NK)O(NK) space. Also, the call stack for DFS will use O(NK)O(NK) space in the worst case.



class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adj = defaultdict(list)
        # for i in range(len(accounts)):
        for i, account in enumerate(accounts):
            accountSize = len(account)
            
            # buildiing adjacency list
            # Adding edge between first email to all othr emails in the account
            # accountFirstEmail = account[1]
            for j in range(2, accountSize):
                adj[account[1]].append(account[j])
                adj[account[j]].append(account[1])
        
        def dfs(mergeAccount, email):
            # if email in visited:
            #     return False
            visited.add(email)
            mergeAccount.append(email)
            if email not in adj:
                return
            for nei in adj[email]:
                if nei not in visited:
                    dfs(mergeAccount, nei)
            # return True
        # Traverse over all the account to store components
        mergeAccounts = []
        for account in accounts:
            accountName = account[0]
            accountFirstEmail = account[1]
            if account[1] not in visited:
                mergeAccount = []
                # mergeAccount.append(accountname)
                dfs(mergeAccount, accountFirstEmail)
                mergeAccount = [accountName] + sorted(mergeAccount)
                mergeAccounts.append(mergeAccount)
        return mergeAccounts



# USING UNION FIND
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]