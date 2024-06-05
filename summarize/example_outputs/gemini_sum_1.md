##  大模型推理和部署

**1. 大模型推理优化**
* **模型架构优化**: 模型架构的创新比硬件优化更有前景，因为跨机器部署的长文本场景下推理成本过高
* **KV Cache**:  在 KV Cache 上进行优化，可以显著提升推理效率
* **模型部署**: 在 70B 模型 + 1M 上下文场景下，为了减少延迟，不得不跨机器部署，但通信开销仍然是瓶颈
* **机器间通信**:  目前机器间互联通信成本高昂，便宜高效的路径还在探索阶段
* **分布式注意力**:  分布式注意力机制不一定值得，与其硬去部署，不如把时间花在 KV Cache 上
* **推理成本**:  DeepSeekV2 可以开 batch size 16K，LLaMa3 只能开到 batch size 1536
* **TPU**:  TP2/4 比 TP8 更适合推理，TP8 的 allreduce 可能比较慢
* **DeepSeek-V2 优化**:  DeepSeek-V2 通过使用 6-bit 量化和提高 batch size 等方法，实现了 93% 的 KV Cache 压缩
* **DeepSeek-V2 架构**:  DeepSeek-V2 使用了 separate matrix (W^{DQ}) 来降维 query，而不是和 KV 一样使用同一个 matrix (W^{DKV})

**相关引用:**
* DeepSeekV2: https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite-Chat

**2.  大模型翻译能力**
* **翻译质量**:  ChatGPT3.5 和 DeepSeekV2 在翻译质量上没有明显区别，翻译腔依然很浓
* **翻译模型**:  一些工作正在探索使用 LLM 完成传统的英 <-> 中 翻译
* **翻译技巧**:  可以尝试使用 prompt 指示模型修改翻译结果，例如 “太西化了，太生硬了”
* **few-shot示例**:  可以考虑使用 dspy 优化 few-shot 示例

**3.  大模型开源**
* **开源定义**:  开源模型是否应该包括训练数据和训练过程，目前还没有统一的定义
* **开源模式**:  现在的开源模型更像是试用体验套装，大模型公司不可能像传统软件的开源一样把数据链路 infra 软件训练细节全给你
* **开放权重**:  开放权重模型更合理，因为大多数用户没有资源自己训练模型
* **训练方案**:  训练方案才是核心资产，比如 yi 

**相关引用:**
* Baichuan: https://huggingface.co/baichuan-inc/Baichuan-7B
* MAP-Neo: https://huggingface.co/collections/m-a-p/neo-models-66395a5c9662bb58d5d70f04

**4.  大模型训练**
* **大模型训练成本**:  训练一个 7B 级别的大模型，需要 256 卡训练一个月，2T tokens
* **模型训练规模**:  模型训练的规模和成本都非常高，目前只有少数机构能够承担

**5.  大模型应用**
* **视频理解**:  目前最好的开源视频理解模型是
* **Agent**:  OpenAI 可能在下周一发布 Agent
* **Interactive Games**:  OpenAI 可能在下周一发布 Interactive Games
* **Sora Access**: OpenAI 可能在下周一发布 Sora Access

**6.  硬件相关**
* **AMD HSA**:  AMD 的 HSA 技术类似统一内存，可以实现相对较大的显存
* **NVidia 方案**:  NVidia 的方案目前仍然是最优解
* **集群设计**:  大模型的训练与集群设计密切相关

**争议点**
* **开源模型定义**:  开源模型是否应该包括训练数据和训练过程
* **奖励模型训练**:  在线训练能够获得更高的效果上限，但需要更多的采样数据，可以使用重要性采样来替代在线训练

**Quick Points**
* **DeepSeek-V2 Lite 版本**:  DeepSeek-V2-Lite-Chat 是一个 SFT 模型，可以方便大家一起魔改 MLA
* **ROPE**:  ROPE 具备远程衰减的性质，但没有长度外推能力
* **大模型训练成本**:  大模型训练成本非常高，只有少数机构能够承担
* **集群通信**:  使用上百台机器训练时，集群之间网络通信可能会出现问题

