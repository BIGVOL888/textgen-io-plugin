
import gradio as gr

def on_ui_tabs():
    with gr.Blocks() as demo:
        gr.Markdown("## ✅ 測試 Plugin 已載入")
        name = gr.Textbox(label="請輸入內容")
        out = gr.Textbox(label="回應")

        def reply(text):
            return f"你好 {text}，這是來自 textgen_io_plugin_fixed 的測試。"

        name.change(fn=reply, inputs=name, outputs=out)

    return [(demo, "🧩 Plugin 測試", "plugin_test_tab")]
