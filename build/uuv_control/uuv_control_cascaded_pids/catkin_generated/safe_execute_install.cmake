execute_process(COMMAND "/home/arslan/uuv_simulator/build/uuv_control/uuv_control_cascaded_pids/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/arslan/uuv_simulator/build/uuv_control/uuv_control_cascaded_pids/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
