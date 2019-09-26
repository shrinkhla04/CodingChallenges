#https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count_dict = {}
        for i in cpdomains:
            count, domain = i.split()
            count = int(count)
            subdomains = domain.split('.')
            for j in range(len(subdomains)):
                t = ".".join(subdomains[j:])
                domain_count_dict[t] = domain_count_dict[t] + count if t in domain_count_dict else count
        return [str(count) + " " + domain for domain, count in domain_count_dict.items()]
#O(N) time where N is the length of cpdomains and assuming cpdomains[i] is of fixed length
#O(N) space for hash_table