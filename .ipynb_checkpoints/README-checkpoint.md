# Submission: Curriculum Engineer position

## Table of Contents
1. [Building the docker image](#dockerimage)
2. [Docker run command](#dockerun)
3. [The exercise](#exercise)
4. [The src/ folder](#srcfolder)


## Building the docker image

To build the docker image cd using the terminal to the download directory (this directory), where the Dockerfile lives and type the docker build commnad:

`docker build -t deeplearn:v0.1 .`

where deeplearn is the image name and v0.1 is the tag.

## Docker run command

To launch the docker container, copy-paste the following docker run command. For it to work properly you must be in the folder as the Dockerfile for the folder mounting -v argument to work properly:

`docker run -it -v "$(pwd)":/mnt -p 8888:8888 -e JUPYTER_TOKEN=neuralnetwork --name cetask deeplearn:v0.1 `

When the docker container is launched, go to your web browser and type the URL: localhost:8888/. And when you asked to type the Jupyter Token type `neuralnetwork`, which is the Token we defined in the docker run command.

## The selected exercise

The selected exercise for this submission was "Implementing the ReLU activation function". The notebook for this exercise can be found at:

`/src/exercise/create_relu.ipynb`

Open the `create_relu.ipynb` notebook to continue with the exercise.

## src/ contents 

   * assets/: Images used in the create_relu.ipynb notebook as part of the exercise explanation.
   * exercise/: The main notebook exercise for this submission.
   * solution/: The main notebook but with exercise cell completed.
   * test_exercise/: testbook/pytest code to test the student's solution.