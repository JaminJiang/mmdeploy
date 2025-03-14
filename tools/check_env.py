# Copyright (c) OpenMMLab. All rights reserved.

from mmcv.utils import collect_env as collect_base_env
from mmcv.utils import get_git_hash

import mmdeploy
from mmdeploy.utils import get_root_logger


def collect_env():
    """Collect the information of the running environments."""
    env_info = collect_base_env()
    env_info['MMDeployment'] = f'{mmdeploy.__version__}+{get_git_hash()[:7]}'

    return env_info


def check_backend():
    try:
        import onnxruntime as ort
    except ImportError:
        ort_version = None
    else:
        ort_version = ort.__version__
    import mmdeploy.apis.onnxruntime as ort_apis
    logger = get_root_logger()
    logger.info(f'onnxruntime: {ort_version} ops_is_avaliable : '
                f'{ort_apis.is_available()}')

    try:
        import tensorrt as trt
    except ImportError:
        trt_version = None
    else:
        trt_version = trt.__version__
    import mmdeploy.apis.tensorrt as trt_apis
    logger.info(
        f'tensorrt: {trt_version} ops_is_avaliable : {trt_apis.is_available()}'
    )

    try:
        import ncnn
    except ImportError:
        ncnn_version = None
    else:
        ncnn_version = ncnn.__version__
    import mmdeploy.apis.ncnn as ncnn_apis
    logger.info(
        f'ncnn: {ncnn_version} ops_is_avaliable : {ncnn_apis.is_available()}')

    import mmdeploy.apis.pplnn as pplnn_apis
    logger.info(f'pplnn_is_avaliable: {pplnn_apis.is_available()}')

    import mmdeploy.apis.openvino as openvino_apis
    logger.info(f'openvino_is_avaliable: {openvino_apis.is_available()}')


def check_codebase():
    try:
        import mmcls
    except ImportError:
        mmcls_version = None
    else:
        mmcls_version = mmcls.__version__
    logger.info(f'mmcls: {mmcls_version}')

    try:
        import mmdet
    except ImportError:
        mmdet_version = None
    else:
        mmdet_version = mmdet.__version__
    logger.info(f'mmdet: {mmdet_version}')

    try:
        import mmedit
    except ImportError:
        mmedit_version = None
    else:
        mmedit_version = mmedit.__version__
    logger.info(f'mmedit: {mmedit_version}')

    try:
        import mmocr
    except ImportError:
        mmocr_version = None
    else:
        mmocr_version = mmocr.__version__
    logger.info(f'mmocr: {mmocr_version}')

    try:
        import mmseg
    except ImportError:
        mmseg_version = None
    else:
        mmseg_version = mmseg.__version__
    logger.info(f'mmseg: {mmseg_version}')


if __name__ == '__main__':
    logger = get_root_logger()
    logger.info('\n')
    logger.info('**********Environmental information**********')
    for name, val in collect_env().items():
        logger.info('{}: {}'.format(name, val))
    logger.info('\n')
    logger.info('**********Backend information**********')
    check_backend()
    logger.info('\n')
    logger.info('**********Codebase information**********')
    check_codebase()
