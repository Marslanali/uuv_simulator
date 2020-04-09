# Install script for directory: /home/arslanali/uuv_simulator/uuv_tutorials/uuv_tutorial_dp_controller

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/arslanali/uuv_simulator/build/uuv_tutorials/uuv_tutorial_dp_controller/catkin_generated/installspace/uuv_tutorial_dp_controller.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_tutorial_dp_controller/cmake" TYPE FILE FILES
    "/home/arslanali/uuv_simulator/build/uuv_tutorials/uuv_tutorial_dp_controller/catkin_generated/installspace/uuv_tutorial_dp_controllerConfig.cmake"
    "/home/arslanali/uuv_simulator/build/uuv_tutorials/uuv_tutorial_dp_controller/catkin_generated/installspace/uuv_tutorial_dp_controllerConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_tutorial_dp_controller" TYPE FILE FILES "/home/arslanali/uuv_simulator/uuv_tutorials/uuv_tutorial_dp_controller/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_tutorial_dp_controller" TYPE PROGRAM FILES "/home/arslanali/uuv_simulator/build/uuv_tutorials/uuv_tutorial_dp_controller/catkin_generated/installspace/tutorial_dp_controller.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_tutorial_dp_controller" TYPE DIRECTORY FILES "/home/arslanali/uuv_simulator/uuv_tutorials/uuv_tutorial_dp_controller/launch" REGEX "/[^/]*\\~$" EXCLUDE)
endif()

