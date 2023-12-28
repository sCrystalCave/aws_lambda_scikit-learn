![image](https://github.com/sCrystalCave/aws_lambda_scikit-learn/assets/124455998/bf46fe96-34e6-4af9-8460-077fea2e7c16)

### English description
AWS lambda does not allow you to import many libraries directly, including scikit-learn.
One solution is to build the code that uses these libraries into a docker image. 
You must upload this to AWS ECR and load the image when creating a lambda function.
I referenced the following video, and the video order is p1,p2,p3,deploy.
#### https://youtube.com/playlist?list=PLXHC9Ygb_gU4COSnjLrqu2SUMuvACDHUh&si=B4mGJrL1DEmUf-ZS

### 한국어 설명
aws lambda에서는 scikit-learn를 포함하여 많은 라이브러리를 직접적으로 import 할 수 없습니다.  
해결 방법 중 하나는 이러한 라이브러리를 사용하는 코드를 docker 이미지로 만드는 것입니다. 
이를 aws ecr에 업로드하고 lambda 함수를 만들때 해당 이미지를 불러와야합니다. 
저는 다음 동영상을 참고했으며 동영상 순서는 p1,p2,p3,deploy입니다.
#### https://youtube.com/playlist?list=PLXHC9Ygb_gU4COSnjLrqu2SUMuvACDHUh&si=B4mGJrL1DEmUf-ZS

### local test
<pre><code>
py -3.8 -m venv venv

source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

pip install -r requirements.txt

python test.py 
</code></pre>

### after deploy, write a new lambda function
<pre><code>
import json
import http.client  #request x

def send_request_and_store_data():
    # created Lambda function URL 
    host = ' ' # ex. 'dddskelskelsegega.lambda-url.ap-northeast-2.on.aws'
    path = '/?tick=1'

    # HTTP 연결 생성 및 요청
    connection = http.client.HTTPSConnection(host)
    connection.request("GET", path)

    # 응답 받기
    response = connection.getresponse()
    if response.status == 200:
        # 응답 데이터 읽기 및 파싱
        data = json.loads(response.read())
        print(data)

    else:
        print(f"Request failed with status code: {response.status}")

    # 연결 닫기
    connection.close()
  
def lambda_handler(event, context):

    send_request_and_store_data()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Published to topic and data stored in DynamoDB')
    }
</code></pre>
##
