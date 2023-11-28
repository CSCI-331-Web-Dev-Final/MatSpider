from django.shortcuts import render
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import urllib, base64

# def response(request):
#     # Check if the form has been submitted
#     if request.method == 'POST':
#         input_data = request.POST.get('input_data', '')  # Get user input from the form

#         # Generate Matplotlib graph based on user input
#         fig, ax = plt.subplots()
#         # Use 'input_data' to customize the graph (replace with your logic)
#         ax.plot([1, 2, 3, 4, 5], [int(input_data) * i for i in [1, 2, 3, 4, 5]])
#         ax.set_title(f'Matplotlib Graph for Input: {input_data}')

#         # Convert Matplotlib figure to PNG image
#         canvas = FigureCanvas(fig)
#         buf = io.BytesIO()
#         canvas.print_png(buf)
#         data = base64.b64encode(buf.getbuffer()).decode('utf-8')
#         plt.close(fig)

#         # Pass the data to the template
#         context = {'image_data': data}

#         return render(request, 'response.html', context)

#     # Initial rendering without form submission
#     return render(request, 'response.html', {'image_data': None})

def response(request):
    if request.method == 'POST':
        # Process the form data
        input_data = request.POST.get('input_data')

        # Generate a Matplotlib plot (replace this with your actual plot logic)
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.title('Example Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Save the plot to a BytesIO object
        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        plt.close()

        # Convert the image stream to base64
        image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

        # Pass the base64-encoded image to the template
        return render(request, 'response.html', {'image_base64': image_base64})

    return render(request, 'response.html')

