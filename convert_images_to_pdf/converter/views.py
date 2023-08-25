from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def convert_images_to_pdf(image_files):
    output = io.BytesIO()
    c = canvas.Canvas(output, pagesize=letter)

    for image_file in image_files:
        img = Image.open(image_file)
        img_width, img_height = img.size
        pdf_width, pdf_height = letter

        if img_width > pdf_width or img_height > pdf_height:
            img.thumbnail((pdf_width, pdf_height))

        img_bytes = image_file.read()
        img = Image.open(io.BytesIO(img_bytes))
        c.drawImage(img, 0, 0, width=img.width, height=img.height)
        c.showPage()

    c.save()
    return output.getvalue()


def image_to_pdf(request):
    if request.method == "POST":
        uploaded_images = request.FILES.getlist("images")
        pdf_bytes = convert_images_to_pdf(uploaded_images)

        response = HttpResponse(pdf_bytes, content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response

    return render(request, "image_to_pdf.html")
