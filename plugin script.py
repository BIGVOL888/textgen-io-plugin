import gradio as gr

def setup():
    with gr.Blocks() as demo:
        gr.Markdown("# Textgen I/O Plugin")
        inp = gr.Textbox(label="輸入 JSON 或指令")
        out = gr.Textbox(label="模型輸出結果")

        def process(input_text):
            # TODO: 放入你的 I/O 處理邏輯
            return f"你輸入了：{input_text}"

        btn = gr.Button("送出")
        btn.click(fn=process, inputs=inp, outputs=out)
    return demo

EXTENSION_UI = setup()
