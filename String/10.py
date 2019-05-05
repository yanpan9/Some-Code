def simplify_p(p):
	if not p:
		return p
	else:
		star_end_flag = True if p[-1]=="*" else False
		p_split = p.split("*")
		new_p = list()
		p_iter, p_res = (p_split[:-1],p_split[-1:]) if star_end_flag else (p_split[:-2],p_split[-2:])
		for idx,elem in enumerate(p_iter):
			if len(elem)==1 and elem==p_split[idx+1]:
				continue
			else:
				new_p.append(elem)
		new_p.extend(p_res)
		return "*".join(new_p)

class Solution_Recursion:
    def isMatch(self, s: str, p: str) -> bool:
        any_char, prev_char = ".", "*"
        def dfs(s, p):
            if not p:
                return not s
            first_match = not len(s)==0 and (s[0]==p[0] or p[0]==any_char)
            if len(p)>=2 and p[1]==prev_char:
                return dfs(s,p[2:]) or (first_match and dfs(s[1:], p))
            else:
                return first_match and dfs(s[1:], p[1:])
        p = simplify_p(p)
        return dfs(s, p)

class Solution_DP:
    def isMatch(self, s: str, p: str) -> bool:
        dot, star = ".", "*"
        len_s, len_p = len(s), len(p)
        dp = [[False for j in range(len_p+1)] for i in range(len_s+1)]
        dp[0][0]=True
        for j in range(1, len_p):
            if p[j]==star and dp[0][j-1]:
                dp[0][j+1]=True
        for i in range(1,len_s+1):
            for j in range(1,len_p+1):
                if p[j-1] in {s[i-1], dot}:
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]==star:
                    if p[j-2] not in {s[i-1], "."}:
                        dp[i][j]=dp[i][j-2]
                    else:
                        dp[i][j]=(dp[i-1][j-1] or dp[i][j-2] or dp[i-1][j])
        return dp[-1][-1]