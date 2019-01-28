class Solution:
    def cacheDomain(self, domain, num):
        if self.domaindict.get(domain):
            self.domaindict[domain] += int(num)
        else:
            self.domaindict[domain] = int(num)

    def subdomainVisitsHelper(self, cpdomain):
        num = cpdomain.split(' ')[0]
        domain = cpdomain.split(' ')[1]
        if len(domain.split('.')) == 1:
            self.cacheDomain(domain, num)
            return [num + " " + domain]
        domain = cpdomain.split(' ')[1]
        self.cacheDomain(domain, num)
        self.subdomainVisitsHelper(num + " " + ".".join(domain.split('.')[1:]))

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        self.domaindict = {}
        results = []
        for i in cpdomains:
            self.subdomainVisitsHelper(i)
        results = [str(v) + " " + k for k, v in self.domaindict.items()]
        return results


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().subdomainVisits)
    i2 = ["9001 discuss.leetcode.com"]
    r2 = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    t.equal(
        sorted(r2, key=lambda x: int(x.split(" ")[0])),
        sorted(i2, key=lambda x: int(x.split(" ")[0])))
