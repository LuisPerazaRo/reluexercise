FROM python:3.12-slim

RUN mkdir -p /mnt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Jupyter Notebook will run on
EXPOSE 8888

WORKDIR /mnt

# Command to run JupyterLab when the container starts
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--allow-root", "--ip=0.0.0.0"]

