# Compression Theory for Large Language Models

Compression theory 或许是目前为止 LLM 最底层的理论，它的核心论点是只要压缩下一个 token 就可以通向 AGI；此理论被 OpenAI / DeepMind / Moonshot 等一线机构的研究者们深入讨论，具体的资料包括但不限于：

- DeepMind Jake Rae, [Compression for AGI](https://www.youtube.com/watch?v=dO4TPJkeaaU)
- OpenAI Ilya Sutskever, [An observation on generalization](https://www.notion.so/Compression-Theory-for-Language-Models-Clubhouse-Style-Discussion-01feb5447454458c83adad5aa9708b17?pvs=21)
- DeepMind Deletang et. al. [Language Modeling Is Compression](https://arxiv.org/pdf/2309.10668.pdf)
- Moonshot 周昕宇, [压缩下一个 token 通向超过人类的智能](https://zhuanlan.zhihu.com/p/619511222)

## Preliminary: Arithmetic coding
* [Arithmetic coding](https://en.wikipedia.org/wiki/Arithmetic_coding) 是一种无损编码数据的算法，它依赖一个概率模型
* 概率模型对数据的 likelihood 越高，arithmetic coding 压缩率越高

## Language modeling as lossless compression
* 语言模型对数据并不是有损压缩，而是无损
* 语言模型通过对数据做 arithmetic coding 来压缩数据
* gzip 的压缩率是 32%，200K 大小的 Transformer 有 30%，Chinchilla 7B 有 10.2%，70B 有 8.3%，参考 [Language Modeling Is Compression](https://abs.arxiv.org/abs/2309.10668) 这篇论文

## The more you compress, the more likely to get generative process
* 考虑随机数压缩，如果 Alice 用一个随机数生成器生成 400B 随机数，gzip 压缩到 30% 也有 100多 B
* 但是如果 Alice 只存随机数生成算法和种子，则只需要几十 k
* Generative process 和 data 的区别
  * Generative process 是一个随机过程，是生成数据的算法
  * data 是从算法中生成出来的数据
* 模型可以从数据中学会生成数据的算法
  * 参考 [Learning Transformer Programs](https://arxiv.org/abs/2306.01128) 这篇文章，可以从模型权重中逆编译出生成数据的算法
* Intelligence is a side product
  * 优化目标是压缩，得到的是智能
 
## Why intelligence has to be a side product: Goodhart's law
* 过度优化在 pretrain, SFT, RL 三个阶段普遍存在
  * Pretrain: 过拟合 C-Eval 这样的 Benchmark 并不体现模型能力
  * SFT: 过拟合 GSM8K 这样的 benchmark 并不增加模型数学
  * RLHF: 对一个固定的 reward model ，过度优化之后模型行为会很奇怪，参考 [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760) 以及 John Schulman 的 [ICML Talk](https://icml.cc/virtual/2023/invited-talk/21549)


