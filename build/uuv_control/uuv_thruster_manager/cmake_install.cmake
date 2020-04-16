# Install script for directory: /home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/arslanali/uuv_simulator/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_thruster_manager/srv" TYPE FILE FILES
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/srv/GetThrusterCurve.srv"
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/srv/ThrusterManagerInfo.srv"
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/srv/SetThrusterManagerConfig.srv"
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/srv/GetThrusterManagerConfig.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_thruster_manager/cmake" TYPE FILE FILES "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/installspace/uuv_thruster_manager-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/arslanali/uuv_simulator/devel/include/uuv_thruster_manager")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/arslanali/uuv_simulator/devel/share/roseus/ros/uuv_thruster_manager")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/arslanali/uuv_simulator/devel/share/common-lisp/ros/uuv_thruster_manager")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/arslanali/uuv_simulator/devel/share/gennodejs/ros/uuv_thruster_manager")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/arslanali/uuv_simulator/devel/lib/python2.7/dist-packages/uuv_thruster_manager")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/arslanali/uuv_simulator/devel/lib/python2.7/dist-packages/uuv_thruster_manager")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/installspace/uuv_thruster_manager.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_thruster_manager/cmake" TYPE FILE FILES "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/installspace/uuv_thruster_manager-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_thruster_manager/cmake" TYPE FILE FILES
    "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/installspace/uuv_thruster_managerConfig.cmake"
    "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/installspace/uuv_thruster_managerConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_thruster_manager" TYPE FILE FILES "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_thruster_manager" TYPE PROGRAM FILES "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager/catkin_generated/installspace/thruster_allocator.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_thruster_manager" TYPE DIRECTORY FILES
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/launch"
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/config"
    REGEX "/[^/]*\\~$" EXCLUDE)
endif()

