## 3.method
* 输入：单目图像序列 + 相机变换矩阵（由SLAM系统获得）
* 目标：**实时** 重建密集的三维场景
* S<sub>t</sub><sup>g</sup>：global TSDF volume，t表示当前时间步
### 3.1 关键帧选取
* 要提供足够的动作视差
* 同时要保持多视角共视？（ **multi-view co-visibility** ）
* 关键帧条件：相对的平移量大于t<sub>max</sub>，相对的旋转量大于R<sub>max</sub>（
    * a key frame if its relative translation is greater than tmax and the relative rotation angle is greater Rmax）
    * Q: 这里的t<sub>max</sub>和R<sub>max</sub>是在哪里定义的？
* 关键帧选择完毕后，会建立一个包含所有关键帧信息的立方体包围盒 **FBV**（在固定的最大深度d<sub>max</sub>下），在之后重建的过程中只考虑FBV中的区域
### 3.2 Joint Fragment Reconstruction and Fusion