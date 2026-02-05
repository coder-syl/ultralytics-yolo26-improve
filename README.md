# 安装依赖
```
pip install ultralytics

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --upgrade

pip install einops
pip install timm

conda create -n yolo26 python=3.11
conda activate yolo26

pip install basicsr
pip install einops
pip install timm
pip install mmengine
```

# 必读指南 📖 | YOLO26改进专栏简介

#### 📌 1. 模型改进无思路？<font color=#d73a49>200+实战方法</font>直接落地

针对<font color=#0366d6>YOLO模型改进</font>痛点，本专栏整理<font color=#d73a49>200+实战验证方法</font>，覆盖<font color=#6f42c1>卷积层</font>、<font color=#6f42c1>注意力机制</font>等<font color=#6f42c1>核心模块</font>。  每种方法含<font color=#005cc5>原理</font>、<font color=#005cc5>性能分析</font>、<font color=#005cc5>改进路径</font>及<font color=#005cc5>实操流程</font>，<font color=#22863a>代码可直接运行</font>，<font color=#d73a49>快速提升模型效果</font>，<font color=#d73a49>性价比超高</font>。

---

#### 🚀 2. 优质模块难匹配？<font color=#d73a49>顶会算法</font> + <font color=#0366d6>YOLO26专属适配</font>

改进方法源自<font color=#d73a49>CVPR</font>等<font color=#d73a49>顶会前沿算法</font>，结合<font color=#0366d6>YOLO26二次创新</font>。  模块<font color=#22863a>高创新</font>、<font color=#22863a>高适配</font>，可直接用于<font color=#6f42c1>检测</font>、<font color=#6f42c1>分割</font>等<font color=#6f42c1>多视觉任务</font>，满足<font color=#005cc5>科研</font>与<font color=#005cc5>项目</font>双重需求。

---

#### 🔗 3. 全版本兼容？<font color=#d73a49>一次学习</font><font color=#22863a>多端复用</font>

方案完美适配<font color=#0366d6>YOLO26全任务</font>，因<font color=#6f42c1>架构同源</font>，可无缝迁移至  <font color=#0366d6>YOLOv8</font>/<font color=#0366d6>v10</font>/<font color=#0366d6>v11</font> 。  <font color=#d73a49>一次学习</font><font color=#22863a>多版通用</font>，大幅降低<font color=#005cc5>学习</font>与<font color=#005cc5>时间成本</font>。

---

#### 💎 4. 持续更新保障？<font color=#d73a49>早订早享终身权益</font>

专栏<font color=#22863a>每周更新 3-5 篇实战案例</font>，<font color=#d73a49>97 分全网领跑</font>。  <font color=#6f42c1>紧跟 2025 最新动态</font>，<font color=#d73a49>内容增值即涨价</font>，<font color=#22863a>早订更划算</font>。  <font color=#d73a49>一次订阅终身可用</font>，<font color=#005cc5>私信留言需求可优先更新</font>。



# YOLO26的模型结构

需要可编辑的原型图，请私信联系！

 ![在这里插入图片描述](https://banxia-frontend.oss-cn-beijing.aliyuncs.com/img74f69c319ca24b3da6fa8b7ba1b919ac.png)

# YOLO26改进目录一览（持续更新中ing📃）

💡 **购买专栏后，即可私信我，获取完整程序文件以及一键运行的环境**  🛠️ 所有代码支持<span style="color:#22863a">直接集成到你的项目中运行与训练</span>，无需繁琐配置。 支持按需<span style="color:#005cc5">自由组合模块</span>，快速构建适配你数据集的改进方案，实现<span style="color:#d73a49">实战有效涨点</span>。

  

> **专栏购买链接 ： [YOLO26改进专栏](https://blog.csdn.net/yolochangeworld/category_13061428.html)**



# <div align="center">✨基础知识 ✨</div>

[YOLO26 正式发布源代码！极致速度优化方案， 面向工业级落地的目标检测模型！](https://blog.csdn.net/yolochangeworld/article/details/156984905)



# <div align="center">🚁注意力机制 🚁</div> 

- [YOLO26改进 - 注意力机制 | 二阶通道注意力SOCA 通过协方差建模与自适应重缩放实现判别性特征增强](https://blog.csdn.net/yolochangeworld/article/details/157103429)
- [YOLO26改进 - 注意力机制 | SCSA注意力通过双重注意力机制增强局部-全局特征交互](https://blog.csdn.net/yolochangeworld/article/details/157103293)
- [YOLO26改进 - 注意力机制 | 轴向注意力Axial Attention（Axial Attention）优化高分辨率特征提取](https://blog.csdn.net/yolochangeworld/article/details/157102558)
- [YOLO26改进 - 注意力机制 | HaloNet 局部自注意力 (Local Self-Attention) 以分块交互策略实现高效全局上下文建模](https://blog.csdn.net/yolochangeworld/article/details/157102437)
- [YOLO26改进 - 注意力机制 | 空间增强注意力SEAM（Spatially Enhanced Attention Module）提升遮挡场景检测鲁棒性](https://blog.csdn.net/yolochangeworld/article/details/157102154)
- [YOLO26改进 - 注意力机制 | ACmix自注意力与卷积混合模型：轻量级设计融合双机制优势，实现高效特征提取与推理加速](https://blog.csdn.net/yolochangeworld/article/details/157071031)
- [YOLO26改进 - 注意力机制 | CAFM (Convolutional Block Attention Module) 卷积块注意力模块：轻量级设计优化特征提取流程，提升小目标感知](https://blog.csdn.net/yolochangeworld/article/details/157070779)
- [YOLO26改进 - 注意力机制 | DCAFE双坐标注意力：并行坐标注意力 + 双池化融合](https://blog.csdn.net/yolochangeworld/article/details/157070501)
- [YOLO26改进 - 注意力机制  MCAttn 蒙特卡洛注意力：全局上下文与局部细节协同建模，破解微小目标特征表达难题](https://blog.csdn.net/yolochangeworld/article/details/157070359)
- [YOLO26改进 - 注意力机制 | DiffAttention差分注意力：轻量级差分计算实现高效特征降噪，提升模型抗干扰能力 | TMLR  2025](https://blog.csdn.net/yolochangeworld/article/details/157070310)
- [YOLO26改进 - 注意力机制 | Mask Attention掩码注意力，可学习掩码矩阵破解低分辨率特征提取难题 |  2025 预印](https://blog.csdn.net/yolochangeworld/article/details/157070197)
- [YOLO26改进 - 注意力机制 |  IIA信息整合注意力（Information Integration Attention ）：精准保留空间位置信息，平衡精度与计算成本 | TGRS2025](https://blog.csdn.net/yolochangeworld/article/details/157070128)
- [YOLO26改进 - 注意力机制 | LRSA局部区域自注意力( Local-Region Self-Attention）: 轻量级局部上下文建模弥补长程依赖细节不足 | CVPR2025](https://blog.csdn.net/yolochangeworld/article/details/157070069)
- 



#  <div align="center">✅ 特征融合 ✅</div>

1. [YOLO26改进 - 特征融合 | 重参数化CSPELAN模块（Reparameterized CSPELAN Module）通过结构重参数化实现高效特征提取](https://blog.csdn.net/yolochangeworld/article/details/157362806)
2. [YOLO26改进 - 特征融合 | 融合Hyper-YOLO混合聚合网络MANet（Mixed Aggregation Network）通过多路径设计实现高效特征学习与模型适应性提升](https://blog.csdn.net/yolochangeworld/article/details/157362671)
3. [YOLO26改进 - 特征融合 | EFC增强层间特征相关性，通过多尺度特征交互减少冗余信息丢失即插即用](https://blog.csdn.net/yolochangeworld/article/details/157362549)
4. 



# <div align="center">🚀Mamba 系列🚀</div>







# <div align="center">🚀Conv 🚀</div>

1. [YOLO26改进 - 卷积Conv | AKConv可变核卷积：任意参数与采样形状赋能特征提取，提升检测精度](https://blog.csdn.net/yolochangeworld/article/details/157362498)
2. [YOLO26改进 - 卷积Conv | DynamicConv动态卷积赋能YOLO，实现高效参数利用](https://blog.csdn.net/yolochangeworld/article/details/157362418)
3. [YOLO26改进 - 卷积Conv | ODConv全维度动态卷积：四维注意力机制赋能特征提取，增强多尺度感知](https://blog.csdn.net/yolochangeworld/article/details/157362373)
4. [YOLO26改进 - 卷积Conv |  SAConv可切换空洞卷积：自适应融合多尺度特征，优化小目标与遮挡目标感知](https://blog.csdn.net/yolochangeworld/article/details/157362319)
5. [YOLO26改进 - 卷积Conv |  DualConv( Dual Convolutional)：用于轻量级深度神经网络的双卷积核](https://blog.csdn.net/yolochangeworld/article/details/157361967)
6. [YOLO26改进 - 卷积Conv |  SPConv：基于分割的卷积巧解特征冗余，实现高效特征提取](https://blog.csdn.net/yolochangeworld/article/details/157361856)
7. [YOLO26改进 - 卷积Conv |  SCConv空间和通道重建卷积：轻量化设计助力复杂场景与小目标检测](https://blog.csdn.net/yolochangeworld/article/details/157361786)
8. [YOLO26改进 - 卷积Conv | SPD-Conv空间深度转换卷积优化空间信息编码，攻克小目标检测难题](https://blog.csdn.net/yolochangeworld/article/details/157361692)
9. [YOLO26改进 - 卷积Conv | RFAConv：感受野注意力卷积动态调整感受野，提升小目标检出精度 ](https://blog.csdn.net/yolochangeworld/article/details/157361508)
10. [YOLO26改进 - 卷积Conv |   即插即用轻量化突破：OREPA在线卷积重参数化，通过动态结构演化实现高效特征提取与自适应优化](https://blog.csdn.net/yolochangeworld/article/details/157332676)
11. [YOLO26改进 - 卷积Conv |   增强感受野与多尺度特征捕获：引入RFB感受野块（Receptive Field Block）多分支卷积结构](https://blog.csdn.net/yolochangeworld/article/details/157332563)
12. [YOLO26改进 - 卷积Conv |  融合Diverse Branch Block (DBB) 多样分支块的多尺度卷积路径，丰富特征空间实现即插即用性能增益](https://blog.csdn.net/yolochangeworld/article/details/157332447)
13. [YOLO26改进 - 卷积Conv |  RefConv重新参数化重聚焦卷积：突破传统卷积瓶颈，有效减少通道冗余](https://blog.csdn.net/yolochangeworld/article/details/157065280)
14. [YOLO26改进 - 卷积Conv |  引入线性可变形卷积LDConv（Linear Deformable Convolution）增强不规则目标特征捕获能力](https://blog.csdn.net/yolochangeworld/article/details/157065167)
15. [YOLO26改进 - 卷积Conv | 注入多阶门控聚合机制：Multi-Order Gated Aggregation 突破表示瓶颈，增强复杂场景目标感知能力](https://blog.csdn.net/yolochangeworld/article/details/157064455)
16. [YOLO26改进 - 卷积Conv | 融合MogaNet中的ChannelAggregationFFN（通道聚合前馈网络），优化通道维度的特征](https://blog.csdn.net/yolochangeworld/article/details/157064094)
17. [YOLO26改进 - 卷积Conv |   融合多阶门控聚合网络MogaNet与 CA block，提升复杂场景与小目标检测鲁棒性](https://blog.csdn.net/yolochangeworld/article/details/157063994)
18. [YOLO26改进 - 卷积Conv |  LAE: 轻量级自适应提取卷积，从多尺度特征图中获得更多的上下文信息和高分辨率细节](https://blog.csdn.net/yolochangeworld/article/details/157063894)
19. [YOLO26改进 - 卷积Conv |  PConv(Pinwheel-shaped Conv): 风车状卷积用于红外小目标检测 | AAAI 2025](https://blog.csdn.net/yolochangeworld/article/details/157063741)
20. [YOLO26改进 - 卷积Conv |  GCNet之金箍棒块GCBlock ： 重参数化捕获全局依赖 |  CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157063616)
21. [YOLO26改进 - 卷积Conv | 加权卷积wConv2D：无损替换标准卷积，增强空间建模与特征提取质量 | arXiv 2025](https://blog.csdn.net/yolochangeworld/article/details/157063331)
22. [YOLO26改进 - 卷积Conv |   MKDC 多核深度卷积块：多分支架构协同捕获局部细节与全局语义，提升特征判别力 | ICCV 2025](https://blog.csdn.net/yolochangeworld/article/details/157063135)
23. [YOLO26改进 - 卷积Conv | PATConv（Partial Attention Convolution）部分注意力卷积，在减少计算量的同时融合卷积与注意力的优势 | AAAI 2026](https://blog.csdn.net/yolochangeworld/article/details/157062717)





# <div align="center">⛵C3k2融合⛵</div>

1. [YOLO26改进 - C3k2 | C3k2融合SFS-Conv空间 - 频率选择卷积，在单卷积层中提取空间和频率维度特征，降低通道冗余](https://blog.csdn.net/yolochangeworld/article/details/157331792)
2. [YOLO26改进 - C3k2 | C3k2融合FDConv频率动态卷积：空间-频域协同调制增强细节捕获，提升小目标与边界模糊目标检出 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157331683)
3. [YOLO26改进 - C3k2 | C3k2 融合 ARConv 自适应矩形卷积：动态调整卷积核形状与采样点 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157331482)
4. [YOLO26改进 - C3k2 | C3k2 融合 LSConv (Large-Small Conv）:融合大核感知与小核聚合，提升小目标特征判别力 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157331273)
5. [YOLO26改进 - C3k2 | C3k2融合 EVA Block高效视觉注意力块：融合多尺度特征自适应融合与通道级特征精炼 | ICIP 2025](https://blog.csdn.net/yolochangeworld/article/details/157324124)
6. [YOLO26改进 - C3k2 | C3k2融Decoder Block解码器块 ，去模糊和提升图像清晰度 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157324300)
7. [YOLO26改进 - C3k2 26| C3k2融合Mona多认知视觉适配器(CVPR 2025)：打破全参数微调的性能枷锁：即插即用的提点神器](https://blog.csdn.net/yolochangeworld/article/details/157324395)
8. [YOLO26改进 - C3k2 | C3k2融合HMHA分层多头注意力机制：优化模型在复杂场景下的目标感知能力 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157324728)
9. [YOLO26改进 - C3k2 | C3k2融合CBSA 收缩 - 广播自注意力:轻量级设计实现高效特征压缩，优化处理效率 | NeurIPS 2025](https://blog.csdn.net/yolochangeworld/article/details/157324807)
10. [YOLO26改进 - C3k2 | C3k2融合 IIA信息整合注意力（Information Integration Attention ）平衡精度与计算成本 | TGRS2025](https://blog.csdn.net/yolochangeworld/article/details/157324877)
11. [YOLO26改进 - C3k2 | C3k2融合LWGA轻量分组注意力（Light-Weight Grouped Attention）：四路径并行架构破解通道冗余难题  | AAAI 2026](https://blog.csdn.net/yolochangeworld/article/details/157324969)
12. 

# <div align="center">🚤 C2PSA🚤</div>

1. [YOLO26改进 - C2PSA | C2PSA融合MSLA多尺度线性注意力：并行多分支架构融合上下文语义，提升特征判别力 | Arxiv2025](https://blog.csdn.net/yolochangeworld/article/details/157144519)
2. [YOLO26改进 - C2PSA | C2PSA融合DML动态混合层（Dynamic Mixing Layer）轻量级设计优化局部细节捕获与通道适应性，提升超分辨率重建质量](https://blog.csdn.net/yolochangeworld/article/details/157145316)
3. [YOLO26改进 - C2PSA | C2PSA融合EDFFN高效判别频域前馈网络(CVPR 2025)：频域筛选机制增强细节感知，优化复杂场景目标检测](https://blog.csdn.net/yolochangeworld/article/details/157262012)
4. [YOLO26改进 - C2PSA | C2PSA融合Mona多认知视觉适配器：打破全参数微调的性能枷锁：即插即用的提点神器 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157262360)
5. [YOLO26改进 - C2PSA | C2PSA融合CPIASA跨范式交互与对齐自注意力机制 : 交互对齐机制，提升小目标与遮挡目标判别力 | ACM MM2025](https://blog.csdn.net/yolochangeworld/article/details/157262469)
6. [YOLO26改进 - C2PSA | C2PSA融合DiffAttention差分注意力：轻量级差分计算实现高效特征降噪，提升模型抗干扰能力](https://blog.csdn.net/yolochangeworld/article/details/157262673)
7. [YOLO26改进 - C2PSA | C2PSA融合Mask Attention掩码注意力，可学习掩码矩阵破解低分辨率特征提取难题 |  2025 预印](https://blog.csdn.net/yolochangeworld/article/details/157262798)
8. [YOLO26改进 - C2PSA | C2PSA融合TSSA(Token Statistics Self-Attention)令牌统计自注意力，优化遮挡目标感知](https://blog.csdn.net/yolochangeworld/article/details/157262895)
9. 





# <div align="center">🧨SPPF改进 🧨</div>

1. [YOLO26改进 - SPPF模块 | SPPELAN  空间金字塔池化与增强局部注意力：替代SPPF增强多尺度上下文捕获，提升检测精度](https://blog.csdn.net/yolochangeworld/article/details/157263123)
2. [YOLO26改进 - SPPF模块 |  替代SPPF, Mona多认知视觉适配器：打破全参数微调的性能枷锁：即插即用的提点神器 | CVPR 2025](https://blog.csdn.net/yolochangeworld/article/details/157263021)
3. [YOLO26改进 - SPPF模块 | 发论文神器！LSKA注意力改进SPPF,增强多尺度特征提取能力，高效涨点！！！](https://blog.csdn.net/yolochangeworld/article/details/157332143)
4. [YOLO26改进 - SPPF模块 |  替代SPPF，FFocal Modulation焦点调制：即插即用轻量设计优化全局语义捕获](https://blog.csdn.net/yolochangeworld/article/details/157332075)
5. [YOLO26改进 - SPPF模块 | AIFI基于注意力的尺度内特征交互：替代SPPF构建高效混合编码器，提升模型综合效能](https://blog.csdn.net/yolochangeworld/article/details/157331999)
6. 





# <div align="center">🛩️即插即用模块 🛩️</div>





# <div align="center">🪂主干改进 🪂</div>







#  <div align="center">🚀 采样 🚀</div>

1. [YOLO26改进 - 采样 | 小目标分割救星：HWD 降采样少丢细节提精度](https://blog.csdn.net/yolochangeworld/article/details/157363698)
2. [YOLO26改进 - 采样 | mAP 升 2%-7%：DRFD&SRFD 分阶下采样，强化特征稳健性](https://blog.csdn.net/yolochangeworld/article/details/157363786)
3. [YOLO26改进 - 采样 | ICCV 顶会技术：WaveletPool 小波池化强化采样，保留小目标细节](https://blog.csdn.net/yolochangeworld/article/details/157364365)
4. [YOLO26改进 - 下采样 | 轻量化突破：ADown 下采样让 YOLO26 参量减、精度升](https://blog.csdn.net/yolochangeworld/article/details/157364438)
5. [YOLO26改进 -下采样 | 特征融合 NECK 优化，CARAFE 轻量算子让 YOLO26 细节检测飙升](https://blog.csdn.net/yolochangeworld/article/details/157364508)
6. [YOLO26改进-上采样 | EUCB高效上卷积块，实现特征图尺度匹配和高效上采样](https://blog.csdn.net/yolochangeworld/article/details/157364563)
7. 





# <div align="center">✈️  检测头 ✈️</div>

