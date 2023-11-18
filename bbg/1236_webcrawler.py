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
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        #only have access to startURL
        #only can call htmlParser.getUrls("url")
        #return a list of all URls from that webpage

        host_url = startUrl.split("/")[2]

        visited = set()        

        def dfs(thisurl, htmlParser):

            nonlocal host_url

            visited.add(thisurl)

            for nextUrl in htmlParser.getUrls(thisurl):
                if  nextUrl.split("/")[2] == host_url and nextUrl not in visited:
                    dfs(nextUrl, htmlParser)


        dfs(startUrl, htmlParser)
        return visited