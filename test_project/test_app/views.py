from django.http import HttpResponse
import os
from datetime import datetime
import subprocess

def htop_view(request):
    name = "Nagashree P"  # Replace with your full name
    username = os.getenv("USER", "unknown")
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1 | head -15")  # Gets the first 15 lines of the top command output
    return HttpResponse(f"""
    <html>
    <body>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre><strong>Top Output:</strong>\n{top_output}</pre>
    </body>
    </html>
    """)