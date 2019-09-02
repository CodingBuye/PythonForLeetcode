class Solution:
    def defangIPaddr(self, address):
        return "[.]".join(address.split("."))


if __name__ == "__main__":
    address = "1.1.1.1"
    print(Solution().defangIPaddr(address))
