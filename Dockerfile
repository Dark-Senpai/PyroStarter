FROM artemisfowl004/vid-compress
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3","start.py"]
# note: I removed bash as it needs additional file ( with extension .sh )
# So, I directly added python3 for start.py file 

# 😀😀
