
### English description
AWS lambda does not allow you to import many libraries directly, including scikit-learn.
One solution is to build the code that uses these libraries into a docker image. 
You must upload this to AWS ECS and load the image when creating a lambda function.
I referenced the following video, and the video order is p1,p2,p3,deploy.
https://youtube.com/playlist?list=PLXHC9Ygb_gU4COSnjLrqu2SUMuvACDHUh&si=B4mGJrL1DEmUf-ZS

### 한국어 설명
aws lambda에서는 scikit-learn를 포함하여 많은 라이브러리를 직접적으로 import 할 수 없습니다.  
해결 방법 중 하나는 이러한 라이브러리를 사용하는 코드를 docker 이미지로 만드는 것입니다. 
이를 aws ecs에 업로드하고 lambda 함수를 만들때 해당 이미지를 불러와야합니다. 
저는 다음 동영상을 참고했으며 동영상 순서는 p1,p2,p3,deploy입니다.
https://youtube.com/playlist?list=PLXHC9Ygb_gU4COSnjLrqu2SUMuvACDHUh&si=B4mGJrL1DEmUf-ZS
