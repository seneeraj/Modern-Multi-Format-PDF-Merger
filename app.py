import streamlit as st
from streamlit_sortables import sort_items
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import fitz
import os
import img2pdf


# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="Modern PDF Merger",
    page_icon="📄",
    layout="wide"
)


# ========================================
# CREATE REQUIRED DIRECTORIES
# ========================================

TEMP_DIR = "temp"
OUTPUT_DIR = "output"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ========================================
# HELPER FUNCTIONS
# ========================================

def image_to_pdf(image_path, output_pdf):

    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(image_path))


def text_to_pdf(text_path, output_pdf):

    c = canvas.Canvas(output_pdf, pagesize=letter)

    with open(text_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    y = 750

    for line in lines:

        c.drawString(40, y, line.strip())

        y -= 20

        if y < 50:
            c.showPage()
            y = 750

    c.save()


def process_file(uploaded_file):

    filename = uploaded_file.name
    extension = filename.split(".")[-1].lower()

    temp_input_path = os.path.join(TEMP_DIR, filename)

    # Save uploaded file
    with open(temp_input_path, "wb") as f:
        f.write(uploaded_file.read())

    # ====================================
    # PDF FILE
    # ====================================

    if extension == "pdf":

        return temp_input_path

    # ====================================
    # IMAGE FILES
    # ====================================

    elif extension in ["jpg", "jpeg", "png"]:

        output_pdf = os.path.join(
            TEMP_DIR,
            filename + ".pdf"
        )

        image_to_pdf(temp_input_path, output_pdf)

        return output_pdf

    # ====================================
    # TEXT FILES
    # ====================================

    elif extension == "txt":

        output_pdf = os.path.join(
            TEMP_DIR,
            filename + ".pdf"
        )

        text_to_pdf(temp_input_path, output_pdf)

        return output_pdf

    # ====================================
    # OFFICE FILES PLACEHOLDER
    # ====================================

    elif extension in ["docx", "xlsx", "pptx"]:

        st.warning(
            f"⚠ {filename} uploaded successfully. "
            "Office conversion will be added in next version."
        )

        return None

    # ====================================
    # UNSUPPORTED
    # ====================================

    else:

        st.error(f"Unsupported file format: {filename}")

        return None


# ========================================
# PDF MERGING FUNCTION
# ========================================

def merge_pdfs(pdf_list, output_path):

    merged_pdf = fitz.open()

    for pdf in pdf_list:

        current_pdf = fitz.open(pdf)

        merged_pdf.insert_pdf(current_pdf)

        current_pdf.close()

    merged_pdf.save(output_path)
    merged_pdf.close()


# ========================================
# MAIN UI
# ========================================

st.title("📄 Modern Multi-Format PDF Merger")

st.markdown(
    """
Upload multiple files, rearrange them,
and merge everything into one PDF.
"""
)


# ========================================
# FILE UPLOADER
# ========================================

uploaded_files = st.file_uploader(
    "Drag and drop files here",
    accept_multiple_files=True,
    type=[
        "pdf",
        "jpg",
        "jpeg",
        "png",
        "txt",
        "docx",
        "xlsx",
        "pptx"
    ]
)


# ========================================
# FILE SORTING
# ========================================

if uploaded_files:

    st.subheader("📂 Rearrange File Sequence")

    file_names = [file.name for file in uploaded_files]

    sorted_items = sort_items(
        file_names,
        direction="vertical"
    )

    st.subheader("📋 Final Sequence")

    for i, item in enumerate(sorted_items, start=1):

        st.write(f"{i}. {item}")

    # ====================================
    # OUTPUT FILE NAME
    # ====================================

    output_name = st.text_input(
        "Output PDF Name",
        value="merged_output"
    )

    # ====================================
    # MERGE BUTTON
    # ====================================

    if st.button("🚀 Merge Files"):

        ordered_files = []

        for item in sorted_items:

            for file in uploaded_files:

                if file.name == item:

                    ordered_files.append(file)

        pdf_paths = []

        progress = st.progress(0)

        total_files = len(ordered_files)

        # ====================================
        # PROCESS FILES
        # ====================================

        for index, uploaded_file in enumerate(ordered_files):

            processed_pdf = process_file(uploaded_file)

            if processed_pdf:

                pdf_paths.append(processed_pdf)

            progress.progress((index + 1) / total_files)

        # ====================================
        # MERGE PDFs
        # ====================================

        if pdf_paths:

            final_output_path = os.path.join(
                OUTPUT_DIR,
                output_name + ".pdf"
            )

            merge_pdfs(pdf_paths, final_output_path)

            st.success("✅ PDF Merged Successfully!")

            with open(final_output_path, "rb") as pdf_file:

                st.download_button(
                    label="⬇ Download Final PDF",
                    data=pdf_file,
                    file_name=output_name + ".pdf",
                    mime="application/pdf"
                )


# ========================================
# FOOTER
# ========================================

st.markdown("---")

st.markdown(
    """
### Features Included

✅ Multi-file upload  
✅ Drag-and-drop ordering  
✅ Image to PDF conversion  
✅ TXT to PDF conversion  
✅ PDF merging  
✅ Acrobat-safe PDFs  
✅ Modern UI  
✅ Download final PDF  
"""
)