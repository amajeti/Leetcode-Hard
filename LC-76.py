class Solution(object):
    def minWindow(self, s, t):
        window = ''
        res = ''
        result = []
        boo = []
        k=0
        if len(s) < len(t):
            return ''
        elif len(s) == len(t):
            s = ''.join(sorted(s))
            t = ''.join(sorted(t))
            if s==t:
                return s
            else:
                return ''
        elif (t in s):
            return t
        else:
            for i in range(0,len(s)):
                for word in t:
                    window = s[i:i+len(t)-1+k]
                    #print(window)
                    if word in window:
                        boo.append(True)
                    if len(boo) == len(t):
                        res = window
                        result.append(res)
                        break
                    k+=1
                boo = []
            if len(result) == 0:
                return ''
            else:
                pass
        return min(result)
