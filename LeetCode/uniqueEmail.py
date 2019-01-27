#unique email
class Solution:
    def numUniqueEmails(self, emails):

        unique = []
        for email in emails:
            local, domain = email[:email.index('@')], email[email.index('@'):]
            chars = [c for c in local]
            local = str(list(filter(lambda c: (c != '.'), chars)))
            if '+' in local:
                local = local[:local.index('+')]
            email = local + domain
            if email not in unique:
                unique.append(email)
        print(unique)
        return len(unique)
            
s = Solution()
l = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(s.numUniqueEmails(l))
