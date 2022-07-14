FROM python
# python 앱을 사용하기 위한 파이썬 base image
# 초기 빌드 시 파이썬 베이스 이미지를 다운로드 받아야하기 때문에 시간이 오래걸림

WORKDIR /app
# 컨테이너의 작업 디렉토리

COPY . /app

CMD ["python", "rng.py"]

# 포트 공개는 안함(포트 노출 X) : 네트워크 기반 어플리케이션이 아니기 때문
# 이 상태로 docker run ID 입력하면 오류가 발생함

#File "/app/rng.py", line 3, in <module>
#    min_number = int(input('Please enter the min number: '))
#EOFError: EOF when reading a line
# docker run을 사용하면 기본적으로 attached 모드에서 시작하지만 오류가 발생
# 실행중인 컨테이너와 컨테이너로 실행중인 어플리케이션은 상호 작용이 불가능함
# docker run을 사용하면 디폴트로 컨테이너에 연결됨 -> 컨테이너에 의해 출력된 결과를 받을 수 있음
# 컨테이너나 컨테이너로 실행되는 어플리케이션에는 입력하는 것이 불가능

# 옵션 1 : -i (인터렉티브 모드 실행 --interactive)
# Keep STDIN open even if not attached, 즉 컨테이너에 어떤 모드든 상관없이 입력이 가능하다
# -t 옵션(--tty)은 pseudo TTY 가 할당되는데, 이것은 터미널을 생성한다는 것을 의미함
# -i -t 옵션을 결합하면 무언가를 입력할 수 있게 됨!
# 컨테이너는 입력을 수신할 수 있게 되며 컨테이너에 의해 노출되는 터미널도 얻게된다.
# 컨테이너는 실제로 입력을 받는 장치가 됨
# -i -t or -it 형태로 결합
# 입력을 모두 받고 출력이 완료되면 컨테이너가 종료됨
# docker start를 이용하여 재실행하면 detached 모드 -> 통신 불가능

# docker start -a 옵션 -> foreground 실행
# 하지만 이상하게 작동 후 한번만 입력할 수 있게 됨
# docker start에도 -i 옵션 존재, -t 플래그는 필요없음
# 처음 -t 플래그로 컨테이너를 실행하고 docker start 명령을 사용하여 다시 컨테이너를 실행하면
# docker run 때 입력한 플래그 옵션을 기억하고 있기 때문(근데 왜 i는 또 입력할까..? 출력 결과를 수신하고 싶다는 것을 강조?)
# docker start -a -i를 통해 컨테이너를 재시작하면 정상적으로 숫자 입력과 출력이 가능