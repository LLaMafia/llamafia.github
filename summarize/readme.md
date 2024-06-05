第一步先在 https://aistudio.google.com/app/apikey 获取自己的 API Key

然后 
```bash
pip install -q -U google-generativeai
export GOOGLE_API_KEY=<your-api-key>
python summarize.py
```

在 `gemini_sum.md` 是一份示例总结报告，这份报告对应的 prompt 为 `libprompt/gemini_sum.prompt`

TODO: 试一试其他模型

