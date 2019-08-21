class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        ipList = list(address)
        #for ip in ipList:
            #newList.append('[.]') if ip == '.' else newList.append(ip)
        newList = ['[.]' if x == '.' else x for x in ipList]
        return(str(''.join(newList)))

s = Solution()
print(s.defangIPaddr('192.168.1.10'))