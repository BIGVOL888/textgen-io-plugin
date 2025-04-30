import gradio as gr
import json
import os
import yaml

def setup():
    with gr.Blocks() as demo:
        gr.Markdown("## 📂 JSON / YAML 檔案解析插件")

        file_input = gr.File(label="上傳 JSON 或 YAML 檔案")
        output = gr.Textbox(label="解析結果", lines=20)

        def parse(file):
            try:
                suffix = os.path.splitext(file.name)[-1].lower()
                with open(file.name, "r", encoding="utf-8") as f:
                    if suffix == ".json":
                        data = json.load(f)
                    elif suffix in [".yaml", ".yml"]:
                        data = yaml.safe_load(f)
                    else:
                        return "❌ 不支援的檔案格式"
                return json.dumps(data, ensure_ascii=False, indent=2)
            except Exception as e:
                return f"❌ 錯誤：{str(e)}"

        file_input.change(fn=parse, inputs=[file_input], outputs=[output])

    return (demo, "🧩 I/O Plugin", "io_plugin_tab")
