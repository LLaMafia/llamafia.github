##  大模型能力、模型架构与性能、长文本场景

**1.  GPT-4o 能力**:  讨论GPT-4o的能力表现
* **逻辑推理**  逻辑推理能力比 GPT-4 和 GPT-4-turbo 更强，在逻辑推理任务上的表现比 GPT-4 高 10%，F1 分数达到 80%
* **代码生成**  在代码生成方面表现不如 Claude
* **多模态 OCR**:  中文多模态 OCR 比之前更聪明 
* **中文语音对话**  实时语音对话功能可能已经消失，问题复杂时推理时间会增加
* **总体评价**  GPT-4o 的推理速度很赞，响应速度超出预期，但中文语音对话能力没有超过预期 

**2.  长文本场景**:  讨论长文本场景下模型的训练和部署
* **RoPE 底数**:   RoPE 的底数下界与训练长度有关，更大的训练长度应该选择更大的底数
* **数据依赖的 scaling law**:  数据依赖的 scaling law 能够在固定计算预算下，根据不同的数据进行模型 scaling 
* **长序列训练**:  长序列训练可以提升模型性能，但是缺乏相关研究和结论 
* 相关引用：
    * **文章**:  [Base of RoPE Bounds Context Length](https://kexue.fm/archives/10122)
    * **文章**:  [Data-dependent scaling laws: Exploring how datasets shape the performance of large language models](https://arxiv.org/abs/2405.16684)
    * **代码**:  OpenCompass (open compass 的朋友会有兴趣搞一搞？)

**3.  模型架构和性能**:  讨论模型架构和性能之间的关系
* **MoE**:   MoE 训练和使用成本更低，但在相同成本下效果比 dense 模型更好 
* **Dense 模型**:  Llama 等模型一直采用 dense 模型架构，原因可能是它们正在探索性能上限 
* **混合精度**:  FP8 训练还没有完全落地，稳定性和效率仍然有待提高

**4.  模型评价**: 讨论如何评价模型的性能 
* **Llamafia poll**:  Llamafia poll 是继 chatbot arena 之后第二可用的模型评价工具 
* **压缩能力**:  [UncheatableEval](https://huggingface.co/spaces/Jellyfish042/UncheatableEval) 提供了模型压缩能力榜单 

**5.  奖励模型**:  讨论奖励模型的训练
* **训练数据**:  高质量的偏好数据对于提升奖励模型性能至关重要 
* **训练阶段**:  奖励模型的训练通常分为多个阶段，包括数据预处理、模型训练和评估 
* **在线 vs 离线**:  在线训练能够获得更高的效果上限，但需要更多采样数据 
* **重要性采样**:  可以考虑使用重要性采样来替代在线训练

**6.  代码执行**:  讨论如何更有效地执行代码 
* **异步执行**:  可以使用异步执行来提高代码执行效率 
* **Chain-of-symbol prompting**:  可以使用 Chain-of-symbol prompting 来执行自然语言和代码混合的生成任务 
* **GPU 执行 Python**:  将 Python 代码迁移到 GPU 上可以减少 I/O 开销 

**7.  多模态模型**: 讨论多模态模型的能力
* **视频理解**:  当前的视频理解模型还不能完全提取不同技术和油耗下降的信息 
* **多模态上下文学习**:  多模态上下文学习可以解决人物一致性问题，以及其他单模态模型无法解决的问题

**8.  其他**: 
* **开源模型的定义**:  开源模型是否应该包括训练数据和训练过程
* **奖励模型的 scaling law**:  奖励模型是否有 scaling law
* **高考agent**:  构建可以考到 140 分的数学高考agent 

**争议点**:

* **开源模型**:  开源模型的定义，是否应该包括训练数据和训练过程
* **奖励模型**:  在线 vs 离线训练方式哪个更有效
* **MoE**:  MoE 架构是否比 dense 模型更有效
* **GPT-4o 的能力**: GPT-4o 的能力是否符合预期 

**Quick Points**:

*  模型压缩能力榜单: [UncheatableEval](https://huggingface.co/spaces/Jellyfish042/UncheatableEval) 提供了模型压缩能力榜单
*  Llamafia poll: Llamafia poll 是继 chatbot arena 之后第二可用的模型评价工具
*  奖励模型训练数据: 高质量的偏好数据对于提升奖励模型性能至关重要 
*  Chain-of-symbol prompting:  可以使用 Chain-of-symbol prompting 来执行自然语言和代码混合的生成任务 
*  GPU 执行 Python:  将 Python 代码迁移到 GPU 上可以减少 I/O 开销 
*  端侧模型: Claude 在代码生成方面表现出色
*  OpenCompass:  open compass 的朋友会有兴趣搞一搞？
*  数据依赖的 scaling law:  数据依赖的 scaling law 能够在固定计算预算下，根据不同的数据进行模型 scaling
*  长序列训练:  长序列训练可以提升模型性能，但是缺乏相关研究和结论

