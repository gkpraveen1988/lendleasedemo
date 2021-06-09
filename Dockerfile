FROM myappnew:4.0
WORKDIR /app
COPY flaskscripts /app
EXPOSE 5000
#CMD ["/bin/bash"]
CMD ["python","-u","/app/main.py"]
