build:
	g++ first_ros2_node.cpp \
	-I /opt/ros/foxy/include/ \
	-L /opt/ros/foxy/lib/ \
	-lrclcpp -lrcutils \
	-o first_node
	
# 顺便小鱼加个clean指令，用来删掉first_node
clean:
	rm first_node
