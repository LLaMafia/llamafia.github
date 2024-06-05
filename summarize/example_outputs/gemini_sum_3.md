##  模型能力和训练方法

**1. 7B 模型未来能力**: 7B 模型未来两年能否与 100B 模型效果相当
* **知识优化**: 知识量的优化空间仍然很大，无论绝对容量还是有用知识的存量 
* **领域专精**: 通过在不同领域数据前面添加区分领域的标签，可以增加 30% 的知识容量 
* **准确性**: 7B 模型有可能在回答准确性上达到 100B 模型的水平 

**2. 模型规模和能力**: 模型参数量级与能力之间的关系
* **视觉模型**: 视觉模型的参数量级较小，原因可能是视觉数据的信息量更少 
* **生成模型**: 生成模型需要较多参数，因为需要学习数据的分布 
* **编码器-解码器**:  在翻译和摘要任务中，较大的编码器被认为比解码器更重要 
* 相关引用：
  * **代码**: Codestral-22B 
  * **代码**: CodeQwen1.5-7B 

**3.  模型训练方式**:  模型训练方式
* **奖励模型**: 奖励模型的训练方式可以分为在线训练和离线训练
    * **在线训练**: 在线训练能够获得更高的效果上限，但需要更多的采样数据 
    * **离线训练**: 离线训练能够节省训练时间，但是效果可能不如在线训练好
    * **重要性采样**: 可以考虑使用重要性采样来替代 online 训练 
* **MoE**: MoE 模型的训练方式仍然存在一些问题
    * **效果**: MoE 模型的效果基本上只能和两倍 active params 的模型效果差不多 
    * **理论**: MoE 的 sparse 优化问题还需要基础理论的突破 

**4.  长序列训练**:  长序列训练的影响
* **训练效果**:  长序列训练是否能够提升模型性能，目前还没有明确的结论
* **序列维度的 scaling law**:  需要研究序列维度的 scaling law，以便更好地理解长序列训练的效果 
* 相关引用：
  * **文章**: [Compute-Optimal Context Size](https://manifestai.com/articles/compute-optimal-context-size/)

**5.  多模态模型**:  多模态模型的能力
* **视频理解**: 目前没有视频理解模型能够提取出不同技术和油耗下降信息 
* **多模态上下文学习**:  多模态模型可以通过多模态上下文学习解决人物一致性问题 
* **OCR**: Gemini Advanced OCR 在处理 LaTeX 内容时表现不佳，容易读错表格内容
* 相关引用：
  * **代码**: Chameleon

**6.  模型压缩**:  模型压缩技术
* **压缩榜单**:  RWKV 发布了模型压缩能力榜单
* **UncheatableEval**:  UncheatableEval 是一个模型压缩能力评估工具 
* 相关引用：
  * **代码**: UncheatableEval
  * **代码**: dolma

##  争议点

* **开源模型**: 开源模型是否应该包括训练数据和训练过程
* **模型评估**:  如何评估模型的性能
    * **Llamafia**: Llamafia 成为继 chatbot arena 后第二可用评估工具
    * **奖励模型**:  高质量的偏好数据对于提升奖励模型的性能至关重要
* **MoE**: MoE 模型是否能够取代 Dense 模型

## Quick Points

* **GPT-4o**:  GPT-4o 在纯文本逻辑推理方面表现出色
* **Gemini**:  Gemini 1.5 在复杂指令方面依然存在问题
* **H卡 FP8 训练**:  H 卡 FP8 训练的稳定性和效率仍然有待提升
* **RoPE**:  RoPE 底数的设计原则，更大的训练长度应该选择更大的底数
