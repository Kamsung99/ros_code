
# 2023/01/02~
* ros2 연습 git
- - -
# 2023_01_02
- - -
* 우분투 20.04 버전 Vmware 안에 설치

* ROS2 설치:
	* foxy : sudo apt install ros-foxy-desktop ros-foxy-rmw-fastrtps* ros-foxy-rmw-cyclonedds*

* Ros2가 정상작동함을 확인 (test,pub, testsub를 통하여)

* turtlesim_node 잘 구동됨을 확인,  teleop으로 움직임을 확인

* ros2 pkg create --build-type ament_python "packagename"으로 패키지 생성
	* ros2 pkg create --build-type ament_python "packagename"

* entry_points 에 ‘패키지명’.’파일명’:main 으로 만들며 ‘,’로 여러 개를 만들 수 있음
	* ex) 'move_turtle = move_turtle_pkg.move_turtle:main' -> move_turtlepkg라는 패키지에 setup.py에 있는 move_turtle를 실행
---
# 2023_01_03
---
* turtle1 토픽을 움직이는 file
	* move_turtle.py

* 터틀에 네임스페이스를 붙여서 생성
	* ros2 run turtlesim turtlesim_node --ros-args -r __ns:=/namespace
		* 네임스페이스로 namespace를 갖는 터틀창 생성
	* ros2 run turtlesim turtlesim_node --ros-args -r __ns:=/n1

* 터틀에 네임스페이스를 붙여서 모듈 실행
	* ros2 run move_turtle_pkg move_turtle --ros-args -r __ns:=/namespace
		* 네임스페이스로 namespace를 갖는 터틀창에 move_turtlepkg라는 패키지 속 setup.py에 있는 move_turtle를 실행
	* ros2 run move_turtle_pkg move_turtle --ros-args -r __ns:=/n1

* 해당 토픽 이름을 가지는 새로운 토픽을 발행함 (한 화면에 추가)
	* ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 7.0, theta: 1.5, name: '토픽이름'}"
		* 한 화면에 토픽이름으로 토픽이름을 가지는 turtle 토픽을 추가함
	* ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 7.0, theta: 1.5, name: 'turtle2'}"

* 해당 토픽의 색상을 변경
	* ros2 service call /토픽이름/set_pen turtlesim/srv/SetPen "{r: 100, g: 100, b: 100, width: 5}"
		* 해당 토픽 이름을 가지는 turtle 토픽의 펜 색상 변경
	* ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 100, g: 100, b: 100, width: 5}"

* + opencv2에서 이미지 로드, 회전, 색상 변경 등 진행
---
# 2023_01_04
---
* 서비스는 토픽처럼 주기적이 아닌 일회성으로 사용할때 사용한다.
* 서비스 코드 작성
	* ./test_num/test_service_client.py -> 클라이언트
	* ./test_num/test_service_ser1.py -> 서버
* 인터페이스
* 경고 발생 -> 그러나 코드 실행은 잘됨?
	~~~
	Traceback (most recent call last):
		File "<string>", line 1, in <module>
		File "/usr/lib/python3.8/distutils/core.py", line 215, in run_setup
			exec(f.read(), g)
		File "<string>", line 28, in <module>
	NameError: name 'e' is not defined
	[1.604s] ERROR:colcon.colcon_core.package_identification:Exception in package identification extension 'python_setup_py' in 'backup': Command '['/usr/bin/python3', '-c', "import sys;from setuptools.extern.packaging.specifiers import SpecifierSet;from distutils.core import run_setup;dist = run_setup(    'setup.py', script_args=('--dry-run',), stop_after='config');skip_keys = ('cmdclass', 'distclass', 'ext_modules', 'metadata');data = {    key: value for key, value in dist.__dict__.items()     if (        not key.startswith('_') and         not callable(value) and         key not in skip_keys and         key not in dist.display_option_names    )};data['metadata'] = {    k: v for k, v in dist.metadata.__dict__.items()     if k not in ('license_files', 'provides_extras')};sys.stdout.buffer.write(repr(data).encode('utf-8'))"]' returned non-zero exit status 1.
	Traceback (most recent call last):
		File "/usr/lib/python3/dist-packages/colcon_core/package_identification/__init__.py", line 142, in _identify
			retval = extension.identify(_reused_descriptor_instance)
		File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 48, in identify
			config = get_setup_information(setup_py)
		File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 241, in get_setup_information
			_setup_information_cache[hashable_env] = _get_setup_information(
		File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 281, in _get_setup_information
			result = subprocess.run(
		File "/usr/lib/python3.8/subprocess.py", line 516, in run
			raise CalledProcessError(retcode, process.args,
	subprocess.CalledProcessError: Command '['/usr/bin/python3', '-c', "import sys;from setuptools.extern.packaging.specifiers import SpecifierSet;from distutils.core import run_setup;dist = run_setup(    'setup.py', script_args=('--dry-run',), stop_after='config');skip_keys = ('cmdclass', 'distclass', 'ext_modules', 'metadata');data = {    key: value for key, value in dist.__dict__.items()     if (        not key.startswith('_') and         not callable(value) and         key not in skip_keys and         key not in dist.display_option_names    )};data['metadata'] = {    k: v for k, v in dist.metadata.__dict__.items()     if k not in ('license_files', 'provides_extras')};sys.stdout.buffer.write(repr(data).encode('utf-8'))"]' returned non-zero exit status 1.
	~~~
---
# 2023_01_05
---
* 파라미터
	* Node 안에서 사용하는 변수같은 것
	* 서비스와 유사
		* 노드 내 매개변수를 서비스 데이터 통신 방법을 사용하여 노드 내부 또는 외부에서 쉽게 지정(Set) 하거나 변경할 수 있고, 쉽게 가져(Get)와서 사용
		* 그와 다르게 서비스는 서비스가 서비스 요청과 응답이라는 RPC(remote procedure call)가 목적
---
# 2023_01_06
---
* ssh 접속하여 ros topic 전달 확인
* sudo apt install ros-foxy-image-transport* 로 이미지, 영상을 볼 수 있음
	* 기존 PC에서 작업
*	카메라 작착 및 카메라 테스트
	*	turtlebot에서 작업.
		*	git clone https://github.com/christianrauch/raspicam2_node.git
			*	패키지 충돌로 인해 아래 3코드를 사용해야 함
			*	sudo apt autoremove --purge libgles2-mesa-dev mesa-common-dev 충돌하는 비디오제거
			*	sudo add-apt-repository ppa:ubuntu-pi-flavour-makers/ppa 파이캠 필요한 라이브러리
			*	sudo apt install libraspberrypi-bin libraspberrypi-dev 파이캠 필요한 라이브러리
			*	sudo usermod -a -G video ubuntu 카메라 유저권한 접근성 등록.
			* sudo apt-get install v4l-utils
			*	v4l2-ctl --list-devices 카메라 잡히는지 확인, 안될경우 밑의 코드를 연이어 실행
			*	df -h #Find your device numbert 디바이스 확인. 장치마다 p1, p2, p3등 다름
			* wget https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20160527_all.deb -P /tmp 라스피컨피그 설치
			*	sudo apt-get install libnewt0.52 whiptail parted triggerhappy lua5.1 alsa-utils -y 라스피컨피크 설치
			* sudo apt-get install -fy
			*	sudo dpkg -i /tmp/raspi-config_20160527_all.deb
			* cd /boot/firmware
			*	sudo vi config.txt 로 이동하여 밑의 줄을 추가
				* start_x=1
				*	gpu_mem = 128
			* sudo reboot 로 다시 시작하여 마침
---
# 2023_01_09
---
* tp_link 802ac - USB wifi driver 설치 -> 체감 x
	~~~
	sudo apt purge rtl8812au-dkms
	sudo apt install git
	git clone https://github.com/gnab/rtl8812au.git
	sudo cp -r rtl8812au  /usr/src/rtl8812au-4.2.2
	sudo dkms add -m rtl8812au -v 4.2.2
	sudo dkms build -m rtl8812au -v 4.2.2
	sudo dkms install -m rtl8812au -v 4.2.2
	~~~
* 원활한 통신 환경을 위해서 좋은 wifi 모듈이 필요
* 리눅스 듀얼 부팅으로 노트북 와이파이 사용 고려
* wifi 접속 불안정 문제 발생
	* 그래서 터틀봇과 가상머신 우분투와의 원격 접속이 불안정함
	* 단순히 사용자가 많아서 그러는것으로 유추.. 핫스팟등 다른 wifi를 갖출 필요가 있음
* raspicam2-node에서 발행하는 Topic 이 너무 느림. 평균 0.15 Hz -> 카메라 사용에 문제 발생
---
# 2023_01_13
---
* SALM으로 지도 생성후 저장시, timeout에러 발생
	* error code (test 라는 이름으로 지도를 저장)
		`ros2 run nav2_map_server map_saver_cli -f ~/test`
	* 해결 코드 (timeout 설정으로 저장)
		`ros2 run nav2_map_server map_saver_cli -f ~/test --ros-args -p save_map_timeout:=10000`

* 네비게이션 로봇 크기와 inflation 변경 하는 방법 -> 너무 크게 설정 되어있으면 navigation이 움직이지 못하는 현상 발생
	* /opt/ros/foxy/share/nav2_bringup/params/nav2_params.yaml 수정
		* local_costmap: local_costmap: ros_parameters: robot_radius 0.11변경
		* local_costmap: local_costmap: ros_parameters: inflation_layer: cost_scaling_factor: 0.3변경
		* local_costmap: local_costmap: ros_parameters: inflation_layer: inflation_radius: 0.055 변경
		* global_costmap: global_costmap: ros_parameters: robot_radius 0.11변경
		* global_costmap: global_costmap: ros_parameters: inflation_layer: cost_scaling_factor: 0.3변경
		* global_costmap: global_costmap: ros_parameters: inflation_layer: inflation_radius: 0.055 변경
	* 네비게이션 관련 변경한 내용이 있으면 turtlebot3_navi 에 있는 param 건들지 말고 여기거를 건드려야 적용됨!

* 프로젝트 발표를 하였음
