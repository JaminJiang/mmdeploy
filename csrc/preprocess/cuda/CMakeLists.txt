# Copyright (c) OpenMMLab. All rights reserved.
cmake_minimum_required(VERSION 3.14)
project(mmdeploy_cuda_transform_impl CUDA CXX)

if (${CMAKE_VERSION} VERSION_GREATER_EQUAL "3.18.0")
    # suppress 'CMAKE_CUDA_ARCHITECTURES' warning
    cmake_policy(SET CMP0104 OLD)
endif ()

find_package(pplcv REQUIRED)

include(${CMAKE_SOURCE_DIR}/cmake/MMDeploy.cmake)

set(SRCS
        crop_impl.cpp
        image2tensor_impl.cpp
        load_impl.cpp
        normalize_impl.cpp
        pad_impl.cpp
        resize_impl.cpp
        cast.cu
        crop.cu
        normalize.cu
        transpose.cu)
mmdeploy_add_module(${PROJECT_NAME} "${SRCS}")
target_link_libraries(${PROJECT_NAME} PRIVATE
        mmdeploy::transform ${PPLCV_LIBRARIES})
target_include_directories(${PROJECT_NAME}
        PUBLIC ${CUDA_TOOLKIT_ROOT_DIR}/include ${PPLCV_INCLUDE_DIRS})
add_library(mmdeploy::transform_impl::cuda ALIAS ${PROJECT_NAME})
