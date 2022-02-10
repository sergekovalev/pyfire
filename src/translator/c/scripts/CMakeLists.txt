cmake_minimum_required(VERSION 3.1)

project (MAIN)

file(GLOB_RECURSE MAIN_SOURCES "src/*.c")
file(GLOB_RECURSE MAIN_HEADERS "headers/*.h")

set (MAIN_INCLUDE_DIRS "")
set (CMAKE_C_STANDARD 11)

foreach (_headerFile ${MAIN_HEADERS})
    get_filename_component(_dir ${_headerFile} PATH)
    list (APPEND MAIN_INCLUDE_DIRS ${_dir})
endforeach()
list(REMOVE_DUPLICATES MAIN_INCLUDE_DIRS)

add_executable (maind ${MAIN_SOURCES})
target_link_libraries(maind m)
target_include_directories(maind PRIVATE ${MAIN_INCLUDE_DIRS})
include_directories({{ INCLUDE_DIRECTORIES }}main)
message("ARGC = "${ARGC})