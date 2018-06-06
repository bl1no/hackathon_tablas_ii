PY_APP_IMAGE=mobile_channel/predictor:1.0.0
PY_APP_PORT=8080
WORK_HOME=/data

# Build our image
docker build -t $PY_APP_IMAGE .

#Delete all the images based on our custom image
docker ps -a | awk '{ print $1,$2 }' | grep $PY_APP_IMAGE | awk '{print $1 }' | xargs -I {} docker rm -f {}

#Run our image again
docker run -p $PY_APP_PORT:5000 -v $(pwd)/../data:$WORK_HOME $PY_APP_IMAGE


