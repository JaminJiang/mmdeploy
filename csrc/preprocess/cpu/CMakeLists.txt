# Copyright (c) OpenMMLab. All rights reserved.
cmake_minimum_required(VERSION 3.14)
project(mmdeploy_cpu_transform_impl)

include(${CMAKE_SOURCE_DIR}/cmake/opencv.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/MMDeploy.cmake)

set(SRCS
        collect_impl.cpp
        crop_impl.cpp
        image2tensor_impl.cpp
        load_impl.cpp
        normalize_impl.cpp
        pad_impl.cpp
        resize_impl.cpp)
mmdeploy_add_module(${PROJECT_NAME} "${SRCS}")
target_link_libraries(${PROJECT_NAME}
        PRIVATE mmdeploy::transform
        mmdeploy_opencv_utils)
add_library(mmdeploy::transform_impl::cpu ALIAS ${PROJECT_NAME})
