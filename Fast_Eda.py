import gradio as gr
import polars as pl
import pygwalker as pyg

def analyze_data(file):
    if file is None:
        return "<p style='color: #666;'>👆 Faça upload de um arquivo para começar</p>", gr.update(visible=True)
    
    try:
        if file.name.endswith('.csv'):
            df = pl.read_csv(file.name)
        elif file.name.endswith('.xlsx'):
            df = pl.read_excel(file.name)
        elif file.name.endswith('.parquet'):
            df = pl.read_parquet(file.name)
        else:
            return "<p style='color: red;'>❌ Formato não suportado</p>", gr.update(visible=True)
        
        df_pandas = df.to_pandas()
        pyg_html = pyg.to_html(df_pandas)
        
        # Retorna o HTML e esconde o uploader
        return pyg_html, gr.update(visible=False)
        
    except Exception as e:
        return f"<p style='color: red;'>❌ Erro: {str(e)}</p>", gr.update(visible=True)

with gr.Blocks(title="Fast EDA", css="""
    .gradio-container {padding: 0 !important; margin: 0 !important;}
    #output_html {height: 100vh !important; margin: 0 !important;}
""") as demo:
    
    upload_section = gr.Column(visible=True, elem_id="upload_section")
    with upload_section:
        gr.Markdown("# 📊 Fast EDA - PyGWalker")
        file_input = gr.File(
            label="Upload da Base de Dados",
            file_types=['.csv', '.xlsx', '.parquet']
        )
    
    output_html = gr.HTML(elem_id="output_html")
    
    file_input.change(
        fn=analyze_data,
        inputs=file_input,
        outputs=[output_html, upload_section]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)