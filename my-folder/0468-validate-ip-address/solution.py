class Solution:
    def validIPAddress(self, queryIP: str) -> str:


        if "." in queryIP and ":" not in queryIP:
            ip = queryIP.split(".")

            if len(ip) != 4:
                return "Neither"
            else:
                for x in ip:
                    if not x.isdigit():
                        return "Neither"

                    if (len(x) > 1 and x.startswith("0")) or (not (0 <= int(x) and int(x) <= 255)):
                        return "Neither"

                return "IPv4"
        elif ":" in queryIP and "." not in queryIP:
            ip = queryIP.split(":")
                
            if len(ip) != 8:
                return "Neither"
            else:
                for x in ip:
                    if not (1 <= len(x) and len(x) <= 4):
                        return "Neither"

                    for char in x:
                        if char not in "0123456789abcdefABCDEF":
                            return "Neither"

                return "IPv6"
        else:
            return "Neither"

