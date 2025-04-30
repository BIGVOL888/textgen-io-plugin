import gradio as gr
import json
import os
import yaml

# 主介面分頁建立
def setup():
    with gr.Blocks() as demo:
        gr.Markdown("## 📂 I/O Plugin｜JSON / YAML 資料上傳與解析")

        file_input = gr.File(label="上傳 JSON / YAML 檔案")
        output_box = gr.Textbox(label="解析結果", lines=20)

        def parse_file(file_obj):
            try:
                suffix = os.path.splitext(file_obj.name)[-1].lower()
                with open(file_obj.name, "r", encoding="utf-8") as f:
                    if suffix == ".json":
                        data = json.load(f)
                    elif suffix in [".yaml", ".yml"]:
                        data = yaml.safe_load(f)
                    else:
                        return "❌ 不支援的檔案格式"

                return json.dumps(data, ensure_ascii=False, indent=2)
            except Exception as e:
                return f"❌ 錯誤：{str(e)}"

        file_input.change(fn=parse_file, inputs=[file_input], outputs=[output_box])

    return (demo, "🧩 I/O Plugin", "io_plugin_tab")

# 以下為標準 plugin 擴充點接口（可擴充）
def input_modifier(text):
    return text

def output_modifier(text):
    return text

def history_modifier(history):
    return history

def bot_prefix_modifier(prefix):
    return prefix

def user_prefix_modifier(prefix):
    return prefix

def chat_input_modifier(text):
    return text
