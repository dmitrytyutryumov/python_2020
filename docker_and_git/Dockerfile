FROM python:3.7-slim
ARG prj_path=/opt/prj/
ENV PRJ_PATH=prj_path
WORKDIR $PRJ_PATH

COPY *.py $PRJ_PATH
ENTRYPOINT ["python"]
CMD ["-s"]
