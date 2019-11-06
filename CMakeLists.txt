cmake_minimum_required(VERSION 3.12)
project(logf)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

add_library(logf INTERFACE)
target_include_directories(logf INTERFACE logf.h)

add_executable(logf-example
        main.cpp)
target_link_libraries(logf-example logf)