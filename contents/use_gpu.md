# 使用图形硬件加速神经网络



## CUDA 和  cuDNN

CUDA 是英伟达（NVIDIA）公司推出的并行计算平台，通过其提供的 API，开发者可以在软件层面访问 NVIDA 的显卡并使用其虚拟指令集（virtual instruction set）和并行计算单元。目前主流的深度学习框架如 Tenserflow、PyTorch、Caffe2 等都封装了 CUDA 的 API 接口。

CUDA Deep Neural Network library （cuDNN）是基于 CUDA 的深度学习库，它提供了深度学习基本数学方法的 GPU 加速底层实现，如前向后向卷积、池化、标准化、激活函数等。

ILISA 服务器上已经安装了 CUDA 和 cuDNN：

> 当前 CUDA 安装版本：10.1.168
>
> 当前 cuDNN 安装版本：7.6



## 在 Tensorflow 上使用  CUDA

* Tensorflow Docs：GPU support [](https://www.tensorflow.org/install/gpu)
* Tensorflow 官方文档：GPU支持 [](https://www.tensorflow.org/install/gpu?hl=zh_cn)



## 在 PyTorch 使用  CUDA

* PyTorch Docs：CUDA semantics [](https://pytorch.org/docs/stable/notes/cuda.html)
* PyTorch 中文文档：CUDA 语义 [](https://pytorch-cn.readthedocs.io/zh/latest/notes/cuda/)



## 示例程序

这是一份在 PyTorch 上实现的用 MNIST 数据集训练 LeNet 卷积神经网络的程序，包含了未使用 GPU 加速的版本和使用 GPU 加速的版本。在 ILISA 服务器上完成 10 次训练迭代，不使用 GPU 加速需要 6 至 10 分钟，而使用 GPU 加速后仅需约 20 秒。

* [image_classification.py](./codes/image_classification.py)
* [image_classification_gpu.py](./codes/image_classification_gpu.py)