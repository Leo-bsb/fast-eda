# 📊 Fast EDA — PyGWalker + Gradio + Polars

[![Hugging Face Spaces](https://img.shields.io/badge/🚀%20Try%20the%20App-Hugging%20Face%20Spaces-blue?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/leo-bsb/Fast_Eda)

**Fast EDA** is a lightweight web app for **quick, visual exploratory data analysis (EDA)** directly in your browser.  
It uses **PyGWalker**, **Gradio**, and **Polars** to generate interactive dashboards from your uploaded datasets — all in seconds.

> ⚠️ **Note:** This is a **portfolio project** hosted on **Hugging Face Spaces (free tier)**.  
> Due to resource limits, it supports **small to medium datasets only**.

---

## 🌐 Live Demo

👉 **[Access Fast EDA on Hugging Face Spaces](https://huggingface.co/spaces/leo-bsb/Fast_Eda)**

Upload a `.csv`, `.xlsx`, or `.parquet` file and instantly explore your data interactively — no setup needed.

---

## 🧠 Key Features

- 📁 Supports `.csv`, `.xlsx`, and `.parquet` files  
- ⚡ Fast data loading powered by **Polars** (with automatic Pandas fallback)  
- 🧮 Auto-generated **PyGWalker** dashboards  
- 💻 Clean and responsive **Gradio** interface  
- 🧰 Perfect for **quick online data exploration**

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| Web UI | [Gradio](https://gradio.app/) |
| Data Engine | [Polars](https://pola.rs/) |
| Visualization | [PyGWalker](https://github.com/Kanaries/pygwalker) |
| Backend Language | Python 3.10+ |
| Hosting | [Hugging Face Spaces](https://huggingface.co/spaces) |

---

## 🗂️ Project Structure

```

fast-eda/
│
├── app.py                # Main application logic
├── requirements.txt      # Dependency list
└── README.md             # Project documentation

````

---

## ⚙️ Running Locally

If you prefer to run the app locally:

```bash
git clone https://github.com/Leo-bsb/fast-eda.git
cd fast-eda
pip install -r requirements.txt
python app.py
````

Then open [http://127.0.0.1:7860](http://127.0.0.1:7860) in your browser.

---

## 📦 Requirements

```
gradio==4.44.0
polars==1.11.0
pandas==2.2.3
pygwalker==0.4.8
pyarrow==18.0.0
openpyxl==3.1.5
fastexcel==0.11.6
```

> The app uses **Polars** for speed and efficiency.
> If a file format is not supported, it automatically falls back to **Pandas**.

---

## ⚡ Performance & Limitations

* Designed for **fast, lightweight EDA** in the browser
* Optimized for **datasets under ~30 MB** (due to Hugging Face free-tier limits)
* For larger datasets, clone and run locally for better performance

---

## 📸 Screenshot
<img width="1115" height="579" alt="Captura de tela de 2025-11-11 22-30-24" src="https://github.com/user-attachments/assets/72afff4e-abb4-4c05-85b2-c87e0d78d152" />

<img width="1124" height="645" alt="Captura de tela de 2025-11-11 22-34-12" src="https://github.com/user-attachments/assets/68c1c97c-343e-4ba0-9427-6e0302ac65fa" />


---

## 🧾 License

This project is distributed under the MIT License.
You can freely reuse or adapt it for your own data science portfolio.

---

## 👤 Author

**Leonardo Braga**
*Data Science and Artificial Intelligence student & intern*
🔗 [Hugging Face Spaces App](https://huggingface.co/spaces/leo-bsb/Fast_Eda)
💼 [GitHub Profile](https://github.com/Leo-bsb)


