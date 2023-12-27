from django.shortcuts import render
from PIL import Image
import qrcode
from io import BytesIO
import base64
from django.http import HttpResponse, HttpRequest
import io

def index(request):
    context = {}
    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "")
        qr_image = qrcode.make(qr_text, box_size=15)
        qr_image_pil = qr_image.get_image()
        
        # Save the QR code image to a BytesIO buffer as PNG
        buffer = io.BytesIO()
        qr_image_pil.save(buffer, format="PNG")
        
        # Get the image data as bytes
        qr_image_data = buffer.getvalue()
        
        # Encode the image data as base64
        qr_image_base64 = base64.b64encode(qr_image_data).decode()
        
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
        
        return render(request, 'index.html', context=context)
    
    return render(request, 'index.html', context=context)
