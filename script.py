import gradio as gr
import json
import os

def on_ui_tabs():
    with gr.Blocks() as demo:
        gr.Markdown("## 📂 JSON / YAML 檔案讀取與預覽")

        file_input = gr.File(label="上傳 JSON 或 YAML")
        preview_output = gr.Textbox(label="📄 解析結果", lines=20)

        def parse_file(f):
            try:
                suffix = os.path.splitext(f.name)[-1].lower()
                with open(f.name, "r", encoding="utf-8") as fp:
                    if suffix == ".json":
                        data = json.load(fp)
                    elif suffix in [".yaml", ".yml"]:
                        import yaml
                        data = yaml.safe_load(fp)
                    else:
                        return "❌ 僅支援 .json / .yaml"
                return json.dumps(data, ensure_ascii=False, indent=2)
            except Exception as e:
                return f"錯誤：{str(e)}"

        file_input.change(fn=parse_file, inputs=[file_input], outputs=[preview_output])

    return [(demo, "🧩 I/O Plugin", "io_plugin_tab")]
