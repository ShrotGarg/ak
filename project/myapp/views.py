from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def index(request):
    return render(request, 'myapp/index.html')

def execute_script(request):
    try:
        result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
        output = result.stdout
    except Exception as e:
        output = str(e)
    return HttpResponse(f"<pre>{output}</pre>")