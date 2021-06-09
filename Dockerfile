FROM python:3.9.1
RUN pip3 install flask mysql-connector-python
WORKDIR /app
COPY flaskscripts /app
EXPOSE 5000
#CMD ["/bin/bash"]
CMD ["python","-u","/app/main.py"]
