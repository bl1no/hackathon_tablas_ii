JUPYTER_IMAGE=mobile_channel/jupyter:1.0.0
JUPYTER_PORT=8888
WORK_HOME=/home/jovyan/work

# Build our image
docker build -t $JUPYTER_IMAGE .

#Delete all the images based on our custom image
docker ps -a | awk '{ print $1,$2 }' | grep $JUPYTER_IMAGE | awk '{print $1 }' | xargs -I {} docker rm -f {}

#Run our image again
docker run -p $JUPYTER_PORT:8888 -v $(pwd)/scripts:$WORK_HOME $JUPYTER_IMAGE


