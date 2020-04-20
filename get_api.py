import requests
import random

'''
    * 참고 * 
    https://developers.nonghyup.com/
    https://github.com/NH-developers
    
    * 주의할 점 *
    IsTuno 
    - 핀테크서비스별 & 전송일자별 거래고유번호 채번 
    - 테스트과정에서는 API요청시 사용자가 항상 새로운 번호로 임의 채번해야함. (예 : 000000, 000001 …)
'''
# 예금주조회
ist_no = random.randint(1, 10000000) # 임의로 지정
iscd = 'YOUR ISCD VALUE'
access_token = 'YOUR TOKEN VALUE'
target_url = 'https://developers.nonghyup.com'
headers = {
  "Header": {
    "ApiNm": "", # 호출하는 API에 따라 달라짐
    "Tsymd": "", # 오늘 날짜 입력 'YYYYMMDD'
    "Trtm": "112428",
    "Iscd": iscd,
    "FintechApsno": "001",
    "ApiSvcCd": "DrawingTransferA",
    "IsTuno": str(ist_no),
    "AccessToken": access_token
  }
}

# 호출하는 API 따라 달라짐 
add_datas = {
    "Bncd": "011",
    "Acno": ""
}


def get_api_data(api_url, api_nm):
    url = target_url + api_url
    headers['Header']['ApiNm'] = api_nm
    headers.update(add_datas)
    response = requests.post(url, json=headers)
    print('response: ', response)
    data = response.json()
    print('data: ', data)


if __name__ == '__main__':
    # 예금주 조회 예시 
    api_url = '​/InquireDepositorAccountNumber.nh'
    api_nm = 'InquireDepositorAccountNumber'
    get_api_data(api_url, api_nm)
