class Codec:
    def base62encode(self, num):
        if num == 0:
            return "a"
        result = ""
        while num > 0:
            reminder = num % 62
            num = int(num / 62)
            result += self.alphatbet[reminder]
        return result

    def base62decode(self, string):
        result = 0
        for char in string:
            result += self.alphatbet.index(char)
        return result

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if not hasattr(self, 'alphatbet'):
            self.alphatbet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if not hasattr(self, 'db'):
            self.db = []
        if longUrl not in self.db:
            self.db.append(longUrl)
        return self.base62encode(self.db.index(longUrl))

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        index = self.base62decode(shortUrl)
        return self.db[index]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
def main():
    t = Codec()
    print(t.encode('http://www.ituring.com.cn/book/tupubarticle/21537'))
    print(t.decode(t.encode('http://www.ituring.com.cn/book/tupubarticle/215372')))


if __name__ == '__main__':
    main()
