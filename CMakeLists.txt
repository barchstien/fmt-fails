cmake_minimum_required(VERSION 3.10.0)

project(test)
set(LIB_NAME ${PROJECT_NAME})
# enable conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# Per Target approach
conan_basic_setup(TARGETS)

# ---- TARGETS ----
# binary
add_executable(${LIB_NAME}-run
    main.cpp
)

#---- INCLUDE DIRECTORIES ----
target_include_directories(${LIB_NAME}-run PRIVATE 
    ${CONAN_INCLUDE_DIRS_FMT}
)

#---- Link ----
target_link_libraries(${LIB_NAME}-run CONAN_PKG::fmt)


#---- C++ 20 ----
# set standard to C++ 20
set_target_properties(${LIB_NAME}-run PROPERTIES CXX_STANDARD 20)

