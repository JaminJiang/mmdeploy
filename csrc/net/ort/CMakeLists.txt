# Copyright (c) OpenMMLab. All rights reserved.
cmake_minimum_required(VERSION 3.14)
project(mmdeploy_ort_net)

if ("cpu" IN_LIST MMDEPLOY_TARGET_DEVICES)
    include(${CMAKE_SOURCE_DIR}/cmake/MMDeploy.cmake)
    mmdeploy_add_module(${PROJECT_NAME} ort_net.cpp)
    target_include_directories(${PROJECT_NAME} PRIVATE ${ONNXRUNTIME_DIR}/include)
    target_link_directories(${PROJECT_NAME} PUBLIC ${ONNXRUNTIME_DIR}/lib)
    target_link_libraries(${PROJECT_NAME} PRIVATE mmdeploy_onnxruntime_ops_obj)
    add_library(mmdeploy::ort_net ALIAS ${PROJECT_NAME})
else ()
    message(ERROR "'ort_net' is NOT supported in target devices: ${MMDEPLOY_TARGET_DEVICES}")
endif ()
