class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        eset = set()
        for email in emails:
            parts = email.split('@')
            local = parts[0]
            email = "".join(local.split("+")[0].split(".")) + parts[1] 
            eset.add(email)
        return len(eset)       