# llamafia.github

LLaMafia 是一个中文前沿 AI / LLM 开源讨论空间。LLaMa 指 [LLaMA 模型](https://en.wikipedia.org/wiki/LLaMA)， Mafia 指[极客群体](https://en.wikipedia.org/wiki/PayPal_Mafia)，合起来叫 LLaMafia

LLaMafia 关注最扎实的工程和最前沿的科学，所有讨论基于第一性科学原理和第一手工程经验，鼓励 critical thinking, promote insightful work

在当下的时代，人们研究 AI 原因有很多，可以是追求产品价值，投资机会，学术资源，社会影响力

LLaMafia 研究 AI，是因为纯粹的热爱

## Tech Log

[20231210](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231210.md)

* MOE Evaluation时的capacity
* 模型外推
* LLM self-generating training data
* Loss形状与训练数据的顺序的关系
* Mixtral讨论
* 论文分析：1.运用在医药领域，构建提示让通用模型战胜专用模型的方法。2. RLCD，用positive/negative prompts生成data，这样data自动有pos/neg labels，然后train reward models。3.天工开源150B中文预训练语料。4. Medical LLM的survey report
* 讨论：1.grad norm的解释。2.文字顺序不影响gpt理解。3. 4090 做多机多卡 pretrain。4. mamba（线性复杂度序列模型）讨论。5. apple 发的新机器学习框架测试。6. window attention，rnn实用性。7. alignment阶段模型学习了什么

[20231203](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231203.md)

* 数字切开验证&&数字计算
* Instruction following 能力
* 论文分析：1.《我在Performer中发现了Transformer-VQ的踪影》2.Multimodal understanding benchmark!
* 讨论：1.LLama2 预测结果不一致 2.LLama 的 tokenizer 和 titoken 本质区别 3.特定的domain用self-instruct 的效果 4.大模型SFT阶段训练不稳定的探索

[20231125](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231125.md)
* 对 AI Safety / AI open source 以及 large scale AI deployment 的看法
* 轻量方法动态压缩序列
* 论文分享：1. Transformer升级之路：15、Key归一化助力长度外推 2. Component-Wise Gradient Norm Clipping 3. Superalignment 4. Detecting Pretraining Data from Large Language Models
* 讨论： 1. 召回向量 & RAG 2. Claude 2.1上下文信息提取能力 3.Medusa 框架 & lookahead decoding 4. LLM局域信息

[20231119](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231119.md)
* Learning Rate 和 Batch Size 的关系
* 多机多卡并行方案
* Grok-1 中匈牙利考试数据集
* 推荐论文的 Agent
* RNN 类模型
* 涌现能力的原理，小模型可以吗？

[20231112](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231112.md)
* 为什么大模型普遍选用更宽而不是更高的模型架构
* 如何实现知识更新
* 复读机问题的原因与解决
* 关于LLM外推
* 位数越多GPT的加法正确率越低

[20231022](https://github.com/LLaMafia/llamafia.github/blob/main/Log/compression.md) Compression Theory. [讨论录像](https://ed-ac-uk.zoom.us/rec/play/AcFcfuRIJXqjEkoIClzmtZQcN88n5vnwRZmkYB2Lr8R8PPPGFabyfvpj4NyaDlvNt87dP0PmVi9WNEqw.Fm5W6IqIWmmiPIYA?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https://ed-ac-uk.zoom.us/rec/share/zxLddFhtjkKkpyqHHvb9kvU34UGqmDpPU_N4OJ7OOaTZl6ek57DASt6OrcEorATt.CPq6Omm-oTt3K4hT)
* Arithmetic Coding 算法
* 语言模型是无损压缩器
* 压缩得越好，模型越有可能恢复数据的生成过程
* 为什么智能是一种副产物：过度优化的问题

## Contact

llamafia.agi@gmail.com
