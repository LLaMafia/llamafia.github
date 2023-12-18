# llamafia.github

LLaMafia 是一个中文前沿 AI / LLM 开源讨论空间。LLaMa 指 [LLaMA 模型](https://en.wikipedia.org/wiki/LLaMA)， Mafia 指[极客群体](https://en.wikipedia.org/wiki/PayPal_Mafia)，合起来叫 LLaMafia

LLaMafia 关注最扎实的工程和最前沿的科学，所有讨论基于第一性科学原理和第一手工程经验，鼓励 critical thinking, promote insightful work

在当下的时代，人们研究 AI 原因有很多，可以是追求产品价值，投资机会，学术资源，社会影响力

LLaMafia 研究 AI，是因为纯粹的热爱

## Tech Log
[20231217](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231217.md)
* 模型的 reverse curse，在 A is B 上训练能否泛化到 B is A
* 多轮对话，KV cache 的压缩
* MoE 与 LoRA 的关系, MoE 的 efficiency 

[20231213](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231213.md) 蒸馏方法的局限与 MOE [讨论录像](https://drive.google.com/file/d/11CSgSzk4XCz4Mj7jh1wu0CPpzrDLASnI/view)
* 当下 self-distill 方法的局限
* 为什么很少有 LLM soft-distll
* MOE 与 contiune training（见录像）

[20231210](https://github.com/LLaMafia/llamafia.github/blob/main/Log/20231210.md)
* MoE Evaluation: 讨论了在MoE模型评估中关于capacity设置的影响与策略。
* LLM外推能力: 模型在处理长文本和代码方面的外推能力及其局限性
* 自生成训练数据: 模型自我生成训练数据的方法、效果及潜在偏差
* 损失函数形状: 训练数据顺序对大型模型训练中损失函数形状的影响
* Mixtral和其他模型讨论: Mixtral-8x7b模型的性能、显存需求和推理速度，以及其他相关模型的讨论

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
