# playstation_demo

steps to automation

1. Clone this repo
2. Go to the repo folder
3. minikube start
4. eval $(minikube docker-env)
5. Create the docker image using the folling commands
     1. docker build -t {imageName}:{version} .  (Example : docker build -t psdemo:1.0.0 .)
6.Run the following kubctl commands to get the image into the k8 cluster
     1. kubectl apply -f {path_to_yaml_file} ==> yaml file is already provided in the github please update the image name as used in step 3 (Example : kubectl apply -f PSkube.yaml).
     2. kubectl expose deployment {metadata_name} --type=NodePort (Example : kubectl expose deployment psdemopod --type=NodePort)
     3. minikube service {metadata_name} --url (Example : minikube service ps-yml-1 --url)
7.Use the base url provided by minikube to call the apis.
