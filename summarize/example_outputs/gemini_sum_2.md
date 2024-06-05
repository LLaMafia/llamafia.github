## 大模型能力，评测方法，高考应用

**1. 大模型能力和评测方法**:  大模型在不同任务和领域的性能表现
* **7B 模型未来能力**:  7B 模型未来两年能否与 100B 模型效果相当
    * **知识优化**: 知识量的优化空间仍然很大，无论绝对容量还是有用知识的存量 
    * **领域专精**: 通过在不同领域数据前面添加区分领域的标签，可以增加 30% 的知识容量 
    * **准确性**: 7B 模型有可能在回答准确性上达到 100B 模型的水平 
    * 相关引用：
        * **文章**: [Understanding the performance gap between online and offline alignment algorithms](https://arxiv.org/abs/2405.08448) (Gadget)
* **模型规模和能力**: 模型参数量级与能力之间的关系
    * **视觉模型** 视觉模型的参数量级较小，原因可能是视觉数据的信息量更少 
    * **生成模型** 生成模型需要较多参数，因为需要学习数据的分布 
    * **编码器-解码器**  在翻译和摘要任务中，较大的编码器被认为比解码器更重要 
    * 相关引用：
        * **代码**: Codestral-22B 
        * **代码**: CodeQwen1.5-7B 
* **模型复杂度**:  模型倾向于使用复杂方式解题
    * **简单问题复杂化**: complexity based prompting 容易把简单问题带复杂 
    * **KL散度**:  GPT4o 推导 KL 散度的非负性，是不必要的复杂化 
    * 相关引用：
        * **文章**: [OlympiadBench: A Benchmark for Reasoning, Problem Solving, and Creativity in Mathematical Olympiad Problems](https://arxiv.org/pdf/2402.14008.pdf) 
    * **文章**: [When Language Models are Less Wrong: On the Necessity of Statistical Justification](https://x.com/liambolling/status/1792992186411430244?s=46&t=CKI7n9G54Thts9rTrC1n0Q) 
* **多模态模型**:  多模态模型在图像理解和推理任务中的表现 
    * **多模态 scaling law**:  Uni-modal 的 scaling law 力  molecules 对 scale 的利用很充分
    * **图像理解**: GPT4V 能识别出墨西哥湾流 
    * 相关引用：
        * **文章**: [Scaling Laws for Multimodal Language Models](https://arxiv.org/pdf/2301.03728.pdf)
* **分词对算术性能的影响**:  不同分词方案对模型算术性能的影响
    * **分词方案**:  训练 tokenizer 的数据选择不同的子集，会导致分词结果的差异 
    * **人工调整**:  需要考虑人工调整的部分 
    * **避免错误分词**: 调整格式可以避免错误分词，提升算术性能 
    * 相关引用：
        * **文章**: [Understanding the Performance Gap Between Online and Offline Alignment Algorithms](https://arxiv.org/abs/2405.08448) (Gadget)
        * **文章**: [On the Impact of Tokenization on Arithmetic Performance of Language Models](https://arxiv.org/abs/2305.14201) 

**2.  高考应用**:  大模型参加高考的可行性
* **高考agent**:  构建一个数学成绩能达到 140 分的 agent 
    * **真题训练**:  将前五年的真题作为 in-context example 进行训练
    * **instruction 和 reflection**:  Instruction 和 reflection 可以改善模型的成绩 
* **大模型参加高考**:  大模型参加高考的优势和劣势
    * **客观题**:  大模型在客观题方面可能取得较好的成绩
    * **主观题**:  主观题评分标准难以量化，大模型难以取得高分 
    * **科目差异**:  英语和语文可能更容易获得高分，理综和数学可能较难 

**3. 其他**
* **开源项目**:  推荐关于音频和文本翻译的开源项目 
* **long-context foundation models**:  举办一个 workshop 讨论 Long Context Foundation Models 
* **RLHF**:  开源 RLHF 框架 OpenRLHF 
    * **稳定性**:  OpenRLHF 框架比其他框架更加稳定 
    * **参考**:  参考了 TRLX 和 deepspeed-chat 的稳定性技巧 

**争议点**:
* **奖励模型训练方式**:  在线训练能够获得更高的效果上限，但需要更多的采样数据 
* **开源模型**:  开源模型是否应该包括训练数据和训练过程
* **模型 finetune**:  如何做到模型在某些知识上无法被 finetune 

**Quick points**:
* **Claude**:  Claude 在代码生成方面表现出色
* **GPT-4o**:  GPT-4o 在 Minecraft 中的表现丝滑 
* **GAU**:  ALibi 和 Nope 的外推能力为 0，比 Rope 还差
* **deepspeed stage 3**:  DeepSpeed Stage 3 微调 DeepSeek Code 33B 的效果比 Stage 2 差
* **In context learning**:  In Context Learning 是一种提示学习的方法
* **OlympiadBench**:  OlympiadBench 可以用于测试大模型解答数学题的能力 
* **GAOKAO-Bench**:  GAOKAO-Bench 可以用于测试大模型参加高考的能力 
* **模型安全性**:  模型公司需要考虑模型参加高考的安全性问题 
* **字体和卷面**:  高考评分会考虑字体和卷面整洁度 
