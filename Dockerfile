FROM praveen88/personalimages:myapp_1.0
WORKDIR /app
COPY flaskscripts /app
EXPOSE 5000
#CMD ["/bin/bash"]
CMD ["python","-u","/app/main.py"]
