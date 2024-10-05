import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        match_ipv4 = r'^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'

        match_ipv6 = r'^([0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}$'
  
        
        if re.match(match_ipv4, queryIP):
            return 'IPv4'
        
        elif re.match(match_ipv6, queryIP):
            return 'IPv6'
        
        else:
            return 'Neither'