from random import randint

min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

if (max_number < min_number): 
  print('Invalid input - shutting down...')
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

# Python ver.3 으로 빌드된 간단한 어플리케이션 (웹개발용X)
# docker는 웹서버 전용이 아니기 때문에 이러한 어플리케이션도 동작 가능하다
# 연결 및 분리 모드와도 연관되어있다 -> 실제로 앱과 사용자가 서로 상호작용해야하기 때문!
# 이 예제를 백그라운드에서 실행하면 상호작용이 불가능해서 작동이 안됨