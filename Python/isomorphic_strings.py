class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #s_dic = {letter:counter for (counter, letter) in enumerate(s)}
        #t_dic = {letter:counter for (counter, letter) in enumerate(t)}
        # return sorted(s_dic.values()) == sorted(t_dic.values())
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
