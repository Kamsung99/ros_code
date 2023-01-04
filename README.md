- - -
# 2023_1_2
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
# 2023_1_3
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
# 2023_1_4
---
* 서비스 설명
* 서비스 코드 작성
* 인터페이스
* 에러 발생
	* Traceback (most recent call last):
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
