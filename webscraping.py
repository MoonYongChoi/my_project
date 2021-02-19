import requests
from bs4 import BeautifulSoup

def get_team_urls(url):
    # 리그별 url에 접근해서 팀 리스트 웹스크래핑 해오기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # 추가 코딩 필요

    # 아래 예제와 같이 리그별 팀 정보를 리스트로 얻어낸다
    teams_url = ['https://sports.daum.net/team/epl/1321/squad#1', 'https://sports.daum.net/team/epl/268/squad#1', 'https://sports.daum.net/team/epl/253/squad#1']
    return teams_url

def get_player_urls(url):
    # 팀 url에 접근해서 전체 선수 url을 웹스크래핑 해온다
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # 추가 코딩 필요

    # 아래 예제와 같이 팀별 선수 리스트를 얻어낸다
    player_url = ['https://sports.daum.net/player/epl/531533/news#1', 'https://sports.daum.net/player/epl/1624830/news#1', 'https://sports.daum.net/player/epl/902011/news#1']

    return player_url

def get_player_info(url):
    # 선수 url에 접근해서 웹스크래핑으로 선수 정보 가져온다
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # 추가 코딩 필요

    # 아래 예제와 같이 선수 상세 정보를 얻어낸다
    name = '드와이트 게일'
    position = '공격수'
    news = 'https://sports.v.daum.net/v/20210215131758656'
    print(name, position, news)

### 실행하기
league_urls = ['https://sports.daum.net/team/epl', 'https://sports.daum.net/team/bundesliga', 'https://sports.daum.net/team/primera']
for league in league_urls:
    team_urls = get_team_urls(league)
    for team in team_urls:
        player_urls = get_player_urls(team)
        for player in player_urls:
            get_player_info(player)