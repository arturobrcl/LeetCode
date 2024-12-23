class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_list = list(pattern)
        s_list = s.split()
        s_dict = dict(zip(pattern_list, s_list))
        s_set = set(zip(pattern_list, s_list))
        s_dict_set = set(s_dict.values())
        if len(pattern_list) != len(s_list):
            return False
        return len(s_set) == len(set(s_list)) == len(set(pattern_list)) == len(s_dict_set)
