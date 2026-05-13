# 📄 Multiple File Formats -Merged in One PDF

A modern Streamlit-based application that allows users to:

- Upload multiple files
- Rearrange them in custom sequence
- Convert supported files into PDF
- Merge everything into a single PDF
- Download the final merged document

This project is designed for:

- Office automation
- Invoice merging
- Legal document preparation
- GST documentation
- Compliance workflows
- Personal document organization

---

# 🚀 Features

## ✅ Current Features

- Multi-file upload
- Drag-and-drop file arrangement
- Merge multiple PDFs
- Convert images to PDF
- Convert TXT files to PDF
- Acrobat-safe PDF generation
- Modern Streamlit UI
- Download merged PDF

---

# 📂 Supported File Formats

| Format | Support |
|---|---|
| PDF | ✅ |
| JPG | ✅ |
| JPEG | ✅ |
| PNG | ✅ |
| TXT | ✅ |
| DOCX | ⚠ Coming Soon |
| XLSX | ⚠ Coming Soon |
| PPTX | ⚠ Coming Soon |

---

# 🖥️ Technology Stack

## Frontend
- Streamlit

## PDF Processing
- PyMuPDF (fitz)
- img2pdf
- reportlab

## File Handling
- Python

---

# 📁 Project Structure

```text
merge_pdf_app/
│
├── app.py
├── requirements.txt
├── README.md
├── temp/
└── output/
```

---

# ⚙️ Installation

## Step 1 — Clone Project

```bash
git clone <your_repo_url>
cd merge_pdf_app
```

---

## Step 2 — Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application will open in browser:

```text
http://localhost:8501
```

---

# 📦 requirements.txt

```txt
streamlit
streamlit-sortables
PyMuPDF
Pillow
reportlab
python-docx
img2pdf
```

---

# 🧠 How It Works

## Workflow

```text
Upload Files
     ↓
Arrange Sequence
     ↓
Convert to PDF
     ↓
Merge PDFs
     ↓
Download Final PDF
```

---

# 📄 Current Conversion Support

## PDF
Directly merged.

## Images
Converted using:

- img2pdf

## TXT Files
Converted using:

- reportlab

---

# 🔒 PDF Stability

This application uses:

## PyMuPDF (fitz)

instead of older PDF merging libraries for:

- better stability
- Acrobat-safe PDFs
- fewer corruption issues
- faster processing

---

# ⚠ Known Limitations

Current version does NOT yet support:

- DOCX → PDF conversion
- XLSX → PDF conversion
- PPTX → PDF conversion

These features are planned for Version 2.

---

# 🛣️ Planned Features (Version 2)

## Office File Conversion

- DOCX → PDF
- XLSX → PDF
- PPTX → PDF

using:

- Microsoft Office automation
OR
- LibreOffice headless conversion

---

# 🌟 Future Enhancements

- Email merged PDF automatically
- Gmail SMTP integration
- Drag-and-drop preview cards
- PDF thumbnail previews
- OCR support
- Password-protected PDFs
- Watermarking
- Batch processing
- Folder watch automation
- Google Drive integration
- OneDrive integration
- AI document classification
- Cloud deployment support

---

# 📧 Email Automation (Upcoming)

Future versions will support:

```text
Merge PDF
   ↓
Send to Email Automatically
```

using:

- Gmail SMTP
- App Password authentication

---

# 🔐 Security Recommendation

For email automation:

- Use Gmail App Passwords
- Never hardcode real Gmail passwords
- Use environment variables or Streamlit secrets

---

# 📌 Recommended Environment

## Best Local Setup

- Windows 10/11
- Python 3.11+
- Virtual Environment
- Microsoft Office installed (future Office conversion support)

---

# 🤝 Contribution

Contributions, feature ideas, and improvements are welcome.

---

# 📜 License

This project is for educational and productivity purposes.

---

# 👨‍💻 Author

Developed using:

- Python
- Streamlit
- PyMuPDF

---

# ⭐ Version

## Current Version

```text
v1.0
```

## Status

```text
Working Stable Build
```