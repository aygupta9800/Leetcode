class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        soln1: cal depth def and then reach same level and then use 2 pointers
        soln2: simply keep a path set
        """
        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q and q not in path:
            q = q.parent
        return q if q is not None else None