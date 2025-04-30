import gradio as gr

def setup():
    with gr.Blocks() as demo:
        with gr.Tab("I/O Plugin"):
            gr.Markdown("# ✅ 成功載入 I/O Plugin！")
            text = gr.Textbox(label="輸入")
            btn = gr.Button("送出")
            out = gr.Textbox(label="結果")

            def respond(t):
                return f"你輸入的是：{t}"

            btn.click(respond, inputs=text, outputs=out)
    return demo
