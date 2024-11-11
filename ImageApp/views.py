from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ImageDisplay


def index(request):
    if request.method == 'POST':
        # Handle multiple image uploads
        for key, file in request.FILES.items():
            if key.startswith('image_'):  # Check for image field names like 'image_1', 'image_2', etc.
                # Create a new ImageDisplay object for each uploaded file
                ImageDisplay.objects.create(image=file)

        return redirect('index')  # Redirect to the same page to display updated images

    else:
        fm = ImageForm()

    x = ImageDisplay.objects.all()
    return render(request, 'upload_img.html', {'form': fm, 'x': x})
