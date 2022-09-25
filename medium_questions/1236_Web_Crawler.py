# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def getHostName(self, url):
        removedHttp = url[7:]
        indSlash = len(removedHttp)
        for i, c in enumerate(removedHttp):
            if c == "/":
                indSlash = i
                break
        return removedHttp[:indSlash]
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        visited = {startUrl}
        domain = startUrl.split("http://")[1].split("/")[0]
        ans = [startUrl]
        queue = collections.deque([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                check = htmlParser.getUrls(url)
                for new_url in check:
                    if new_url in visited:
                        continue
                    if new_url.split("http://")[1].split("/")[0] != domain:
                        continue
                    ans.append(new_url)
                    visited.add(new_url)
                    queue.append(new_url)        
        return ans

        visited = set()
        result = [startUrl]
        def helper(su):
            print(su)
            if su in visited:
                return
            visited.add(su)
            urls = htmlParser.getUrls(su)
            for url in urls:
                if self.getHostName(url) == self.getHostName(startUrl) and url not in visited:
                    result.append(url)
                    helper(url)
        helper(startUrl)
        return result