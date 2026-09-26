class Solution:
    def evaluate(self, s, knowledge):
        d = dict(knowledge)
        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i)
                key = s[i + 1:j]

                if key in d:
                    ans.append(d[key])
                else:
                    ans.append('?')

                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)