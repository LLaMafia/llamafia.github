第一步先在 https://aistudio.google.com/app/apikey 获取自己的 API Key

Gemini API 最便宜的一档是是不要钱的，直接 free tier 就行。具体的 rate limite 是
* 15 RPM (requests per minute)
* 1 million TPM (tokens per minute)
* 1,500 RPD (requests per day)

然后需要构建一个 `example_inputs` 放入会议记录

然后 
```bash
pip install -q -U google-generativeai
export GOOGLE_API_KEY=<your-api-key>
python summarize.py
```

在 `example_outputs/` 里面是示例总结报告，这份报告对应的 prompt 为 `libprompt/gemini_sum.prompt`

TODO: 试一试其他模型

