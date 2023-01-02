- - -
# 2023_1_2
- - -
* 우분투 20.04 버전 Vmware 안에 설치
* ROS2 설치:
	* foxy : sudo apt install ros-foxy-desktop ros-foxy-rmw-fastrtps* ros-foxy-rmw-cyclonedds*
* Ros2가 정상작동함을 확인 (test,pub, testsub를 통하여)
* turtlesim_node 잘 구동됨을 확인,  teleop으로 움직임을 확인
* ros2 pkg create --build-type ament_python "packagename"으로 패키지 생성
* entry_points 에 ‘패키지명’.’파일명’:main 으로 만들며 ‘,’로 여러 개를 만들 수 있음
