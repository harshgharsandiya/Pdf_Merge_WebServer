from flask import Flask, render_template, request, send_file
import PyPDF2
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge_pdfs', methods=['POST'])
def merge_pdfs():
    merged_pdf = PyPDF2.PdfMerger()
    files = request.files.getlist('files[]')

    for file in files:
        merged_pdf.append(file)

    output_file = 'output.pdf'
    merged_pdf.write(output_file)
    merged_pdf.close()

    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
