class Solution:
    def numUniqueEmails(self, emails):
        s = set()
        for email in emails:
            email_list = email.split("@")
            local_name = email_list[0].split("+")[0].replace(".", "")
            email = local_name+"@"+email_list[1]
            print(email)
            s.add(email)
        return len(s)


emails_list = ["test.email+alex@leetcode.com",
               "test.e.mail+bob.cathy@leetcode.com",
               "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails_list))
