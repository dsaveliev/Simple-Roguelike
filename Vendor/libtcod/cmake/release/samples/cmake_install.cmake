# Install script for directory: /home/dmitry/Work/Projects/Python/libtcod/samples

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "0")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF(EXISTS "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c")
    FILE(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c"
         RPATH "")
  ENDIF()
  list(APPEND CPACK_ABSOLUTE_DESTINATION_FILES
   "/home/dmitry/Work/Projects/Python/libtcod/samples_c")
FILE(INSTALL DESTINATION "/home/dmitry/Work/Projects/Python/libtcod" TYPE EXECUTABLE FILES "/home/dmitry/Work/Projects/Python/libtcod/cmake/release/samples/samples_c")
  IF(EXISTS "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c")
    FILE(RPATH_REMOVE
         FILE "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c")
    IF(CMAKE_INSTALL_DO_STRIP)
      EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_c")
    ENDIF(CMAKE_INSTALL_DO_STRIP)
  ENDIF()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF(EXISTS "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp")
    FILE(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp"
         RPATH "")
  ENDIF()
  list(APPEND CPACK_ABSOLUTE_DESTINATION_FILES
   "/home/dmitry/Work/Projects/Python/libtcod/samples_cpp")
FILE(INSTALL DESTINATION "/home/dmitry/Work/Projects/Python/libtcod" TYPE EXECUTABLE FILES "/home/dmitry/Work/Projects/Python/libtcod/cmake/release/samples/samples_cpp")
  IF(EXISTS "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp")
    FILE(RPATH_REMOVE
         FILE "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp")
    IF(CMAKE_INSTALL_DO_STRIP)
      EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/samples_cpp")
    ENDIF(CMAKE_INSTALL_DO_STRIP)
  ENDIF()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF(EXISTS "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin")
    FILE(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin"
         RPATH "")
  ENDIF()
  list(APPEND CPACK_ABSOLUTE_DESTINATION_FILES
   "/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin")
FILE(INSTALL DESTINATION "/home/dmitry/Work/Projects/Python/libtcod" TYPE EXECUTABLE FILES "/home/dmitry/Work/Projects/Python/libtcod/cmake/release/samples/hmtool.bin")
  IF(EXISTS "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin")
    FILE(RPATH_REMOVE
         FILE "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin")
    IF(CMAKE_INSTALL_DO_STRIP)
      EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/dmitry/Work/Projects/Python/libtcod/hmtool.bin")
    ENDIF(CMAKE_INSTALL_DO_STRIP)
  ENDIF()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

