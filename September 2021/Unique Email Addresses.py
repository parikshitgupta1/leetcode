class Solution:
    """
    @param emails: 
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        # write your code here
        different = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = "".join(local_name.split('+')[0].split('.'))
            email = local_name + '@' + domain_name
            different.add(email)
        return len(different)
