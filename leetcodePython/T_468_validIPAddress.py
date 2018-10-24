class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            if ':' in IP:
                return 'Neither'
            else:
                parts = IP.split('.')
                if len(parts)!=4:
                    return 'Neither'
                for part in parts:
                    if part=='' or (part[0]=='0' and len(part)>1):
                        return 'Neither'
                    for p in part:
                        if p not in '0987654321':
                            return 'Neither'
                    if int(part)>255:
                        return 'Neither'
                return 'IPv4'
        elif ':' in IP:
            parts = IP.split(':')
            if len(parts)!=8:
                return 'Neither'
            for part in parts:
                if len(part)>4 or len(part)==0:
                    return 'Neither'
                part = part.lower()
                for p in part:
                    if p not in '1234567890abcdef':
                        return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'