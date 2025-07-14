class Codec:
    def __init__(self):
        self.codes={}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code=''
        while True:
            code=''.join(chr(randint(97,122)) for _ in range(6))
            if code not in self.codes:
                break
        self.codes[code]=longUrl
        return code

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codes.get(shortUrl,"")
        


# It generates a random 6-character code for each long URL and stores the mapping in a dictionary.
# The decode function retrieves the original URL using the shortened code.