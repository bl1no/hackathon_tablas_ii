PY_APP_IMAGE=mobile_channel/predictor:1.0.0
PY_APP_CONTAINER_NAME=mobile_predictor
PY_APP_PORT=8080
DATA_PATH=/data
TRAINNING_PATH=/trainning

# Build our image
docker build -t $PY_APP_IMAGE .

docker rm -f $PY_APP_CONTAINER_NAME

#Run our image again
docker run --name $PY_APP_CONTAINER_NAME -p $PY_APP_PORT:5000 -v $(pwd)/../data:$DATA_PATH -v $(pwd)/../trainning:$TRAINNING_PATH $PY_APP_IMAGE


