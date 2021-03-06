import json
import requests

### access token, refresh token
# url = "https://kauth.kakao.com/oauth/token"
#
# data = {
#     "grant_type": "authorization_code",
#     "client_id": "7129688c8d4dc5fb8bd17daf88ddef94",
#     "redirect_uri": "https://localhost.com",
#     "code": "6palcJfbpU_mSRr3HoSEGReqNcL1_zP_pmUlVXiBjkkJYMZhI2MQQ--DLUumOFTpAgGc8worDSAAAAF3JCrz_g"
#
# }
# response = requests.post(url, data=data)
#
# tokens = response.json()
#
# print(tokens)

### refresh token
# url = "https://kauth.kakao.com/oauth/token"
# data = {
#     "grant_type" : "refresh_token",
#     "client_id"  : "7129688c8d4dc5fb8bd17daf88ddef94",
#     "refresh_token" : "u2ZaMPKkcLCtvQBl6VxDI8XVPAcfVyEJOXREGQorDNIAAAF3H9-x_w"
# }
# response = requests.post(url, data=data)
#
# print(response.json())


### 나에게 메시지 보내기
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + 'gR6IsMWiF2KdP4Ig0iqQBseTDULbH98Rd2C0gAopdSkAAAF3JC3FjA'
}

# 일반메시지
# data = {
#     "template_object" : json.dumps({ "object_type" : "text",
#                                      "text" : "Hello, world!",
#                                      "link" : {
#                                                  "web_url" : "www.naver.com"
#                                               }
#     })
# }

# 리스트 메시지
template = {
    "object_type": "list",
    "header_title": "초밥 사진",
    "header_link": {
        "web_url": "www.naver.com",
        "mobile_web_url": "www.naver.com"
    },
    "contents": [
        {
            "title": "1. 광어초밥",
            "description": "광어는 맛있다",
            "image_url": "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width": 50, "image_height": 50,
            "link": {
                "web_url": "www.naver.com",
                "mobile_web_url": "www.naver.com"
            }
        },
        {
            "title": "2. 참치초밥",
            "description": "참치는 맛있다",
            "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width": 50, "image_height": 50,
            "link": {
                "web_url": "www.naver.com",
                "mobile_web_url": "www.naver.com"
            }
        }

    ],
    "buttons": [
        {
            "title": "웹으로 이동",
            "link": {
                "web_url": "www.naver.com",
                "mobile_web_url": "www.naver.com"
            }
        }
    ]

}

data = {
    "template_object": json.dumps(template)
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
