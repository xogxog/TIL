
import requests
from pprint import pprint

class TMBDHelper :
    base_url = 'https://api.themoviedb.org/3'

    def __init__(self, api_key = None):
        self.api_key = api_key

    def get_request_url(self, method='/movie/popular',**kwargs ) : #과제 a,b,c가 movie/popular니까 default값으로 그냥 준다.
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url +method
        request_url += f'?api_key={self.api_key}'
        
        for k,v in kwargs.items():
            request_url += f'&{k}={v}'
        return request_url

    #제목으로 영화 검색 후, 검색결과에서 id를 찾아서 return 
    def get_moive_id(self,title) :
        request_url = self.get_request_url('/search/movie',query=title, region='KR', languate='ko')
        data = requests.get(request_url).json()
        pprint(data)

        results = data.get('results')
        if len(results) :
            movie_id = results[0]['id']
            return movie_id
        else :
            return None



# tmdb_helper = TMBDHelper('33e4ef19e015d915281ddd6881f93178')
# tmdb_helper.get_request_url(languate='ko', region='KR')
# print(tmdb_helper.get_moive_id('기생충'))