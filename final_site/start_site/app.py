from django.shortcuts import render
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import urllib, base64

def response(request):
    if request.method == 'GET':
        # Process the form data
        input_data = request.GET.get('input_data')

        # Generate a Matplotlib plot (replace this with your actual plot logic)
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.title('Example Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Save the plot to a BytesIO object
        image_stream = BytesIO()
        plt.savefig(output.jpg)
        plt.close()

        # Convert the image stream to base64
        image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

        # Pass the base64-encoded image to the template
        return render(request, 'response.html', {'image_base64': image_base64})

    return render(request, 'response.html')

