# AI Fashion
Authors: Aaliyah Hänni, Liem Luong, Vanessa Joy Hsu

Sponsor: Dr. Tatiana Teppoeva, Sr. Data & Applied Scientist at Microsoft

![](/Images/website.jpg?raw=true "Header pic")

### About
Generative adversarial networks (GANs) have been successfully used for various forms of image generation - including but not limited to photograph generation, text-to-image translation, and photograph editing. Our project aims to apply GANs to generate textile patterns in order to aid and inspire those who wish to create fashion items in physical and virtual worlds. GANs allow us to use two competing neural networks - a generator and a discriminator - to generate new synthetic patterns that can pass for real ones. 

In addition to pattern generating neural networks, we have created a platform in which users may test out different AI generated patterns on pre-selected fashion items or in photos of their own. This application utilizes a pre-trained object detection model that has been modified to apply patterns directly onto fashion items. This project serves as a proof of concept for how AI can be applied to enhance work in this specific area of fashion.

### Data Pipeline
We will be using a dataset containing images of clothing patterns from a public github repository (https://github.com/lstearns86/clothing-pattern-dataset). This dataset is free to use without restriction. It’s available to us in CSV format. In addition to the classes and images, the dataset comes with 8 other features: original width, original height, crop X, crop Y, crop width, crop height, and scales. These features will be used to reconstruct the images in the dataset. Also, additional patterns are collected from web-scraping the following sites: 
* Fashion Fabrics Club, https://www.fashionfabricsclub.com
* Online Fabric Store, https://www.onlinefabricstore.com 

The training datasets for DCGAN model are segregated into one of the 10 categories. These images are cleaned and standardized to the same height and width (224 x 224 pixels).

![](/Images/patterns.jpg?raw=true "Dataset pic")

### Technology Framework
* PyTorch (back-end model)
* Django (front-end interface)
* Amazon AWS (hosting environment)

We consider two popular deep learning frameworks, TensorFlow and PyTorch. Ultimately, we decided to use PyTorch for our project given several considerations. Briefly, PyTorch is a popular deep learning framework that was developed by Facebook’s AI Research lab (FAIR) in 2016. It is an open source library for the Python programming language used to develop deep learning applications in computer vision and natural language processing. PyTorch has grown in popularity for its simplicity, ease of use, efficient memory usage, and flexibility. One of the main reasons we chose to use this library over TensorFlow is that it is integrated well with the Python language whereas TensorFlow is less of a pythonic framework and more of a new language. Additionally, performance in PyTorch is optimized automatically via parallelism where the intensive computational work during the training process is distributed among multiple CPU or GPU cores.

### Architecture
Our core architecture design includes three main components: Fabric Pattern Generator Model (component 1), Resolution Enhancement Model (component 2) and Segmentation & Masking Model (component 3). 

![](/Images/AI_Fashion_Architecture.JPG?raw=true "Project architecture pic")

In component 1, we apply the Deep Convolutional Generative Adversarial Network (DCGAN) by training with various textile pattern datasets. The output of this component 1 will be a neural network generated image. This output will be converted into a super resolution in component 2 by the Super Resolution Generative Adversarial Network (SRGAN). In component 3, another pre-trained neural network model will perform image segmentation of clothing patterns and mask the new pattern over the fashion items to produce a result.

### Model 
Component 1: DCGAN Model is the architecture being used for fabric pattern generation in this project. The advantage of DCGAN is its continuous improvement between the Generator and Discriminator Networks by improving the performance while reducing the loss of both networks to produce the best fake images. Below is the neural network structure of the Generator Network and Discriminator Network of DCGAN

![](/Images/DCGAN_architecture.JPG?raw=true "DCGAN architecture pic")

Improving the model performance and reducing the loss are our objectives. We use the default Adam optimizer and Binary Cross Entropy loss from PyTorch.
![](/Images/loss_function.JPG?raw=true "Loss function pic")

Component 2: SRGAN Model is the architecture being used for resolution enhancment in this project. Below is the structure of the Generator Network and Discriminator Network of SRGAN

![](/Images/SRGAN_architecture.JPG?raw=true "SRGAN architecture pic")

The generator takes an input of low resolution image and then pass it through multiple layer of residual blocks instead of deep convolution networks because residual networks are easy to train and generate better results due to the fact that residual network has a type of connections called skip connections among the residual blocks. Each residual block contains two convolutional layers with small 3x3 kernels and 64 feature maps followed by a batch normalization and a Parametric ReLu as the activation function,The reason for choosing Parametric ReLu is because it is one of the best non-linear functions for this particular task of mapping low-resolution images to high-resolution images. The generator tries to upsample the image from low resolution to super resolution.

The main objective of the discriminator is to discriminate between real HR images and generated SR images. Its architecture in the paper is similar to DCGAN by using LeakyReLu as activation function. The initial starting convolutional size is 64 x 64, after each VBL block it is multiplied by 2 until we reach the 8x upscaling factor of 512 x 512. The result of 512 feature maps are followed by two convoluted and LeakyReLu and a sigmoid activation function. The sigmoid activation function in the end is used to obtain a probability for classification action


Component 3: Segmentation and Masking model, we leverage the pre-trained model (Unet_2020-10-30). This model weights for clothe segmentation were trained over the Kaggle dataset - iMaterialist (Fashion) 2019 at FGVC6. We refer the sample from Vladimir Iglovikov (Binary Segmentation of Cloths) to develop our component 3.

### Sample Output
Here is one sample of the final outputs we get from the application.
![](/Images/howitworks.jpg?raw=true "Result pic")

### Website 
Website: [http://ec2-52-43-157-77.us-west-2.compute.amazonaws.com:8000/generator](www.aifashion.link)

![](/Images/AI_Fashion_Longer_Short_Film_AdobeExpress.gif?raw=true "Result pic")

The AI Fashion website allows users to interact with the art generator and application. The user selects a pattern type from the options (e.g floral), the network generates an image of the selected pattern, and then the user either selects a default fashion item or uploads a picture of themselves. The final combination is then presented and the pattern or complete image can be down loaded. 

To run the django application locally, download the git repository and navigate to the folder /website/django_ec2_project. Then install requirements by running the following command:
```
python -m pip install -r requirements.txt
```

To run the django application locally, use the command: 

```
python manage.py runserver
```

### References
We also want to give a quick overview of all the great resources that we used to develop this work. Our project is built upon the great works of many people before us in this field. 
![](/Images/reference_cite.JPG?raw=true "reference citation pic")


