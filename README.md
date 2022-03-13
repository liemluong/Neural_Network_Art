# AI Fashion
Authors: Aaliyah Hänni, Dwight Sablan, Liem Luong, Vanessa Joy Hsu

Sponsor: Tatiana Teppoeva

![](/Images/Website_Image.png?raw=true "Header pic")

### Introduction
Art and data science - on the surface it looks like there is no correlation between the two fields. Fashion and neural networks - the relationship between the two may not be clear. Travel back in time, the history of digital art and technology started in the ‘60s. In the old days, there were challenges with limited computing resources and the power to blend art and AI for a meaningful result. Any accomplishment at that time was considered a significant success in the art field. The intersection of art and data science has gained more popularity in recent years. In reality, art and fashion are the inspiration for people to come up with new pieces of art. Advanced machine learning in the data science field enables creativity to make this process more efficient and more accessible to the broader audience.

In the fashion industry there is constant demand for new and interesting design patterns, which can often be expensive and time consuming to create. Fashion designers are bound by their own internal biases and face limitations on the level of creativity and in-demand fashion that they can create within a given timeframe.

With advances in deep learning, neural networks can be used to alleviate some problems in this field by improving the level of creativity in design for both quantity and quality outputs. In this work, we implement a neural network model to generate new textile patterns for many fashion items. Our solutions and findings could be easily used by the non-tech savvy and will make designs more accessible for the broader audience.

### Data Pipeline
We will be using a dataset containing images of clothing patterns from a public github repository (https://github.com/lstearns86/clothing-pattern-dataset) for our minimum viable product. This dataset is free to use without restriction. It’s available to us in CSV format and consists of 2750 images of clothing patterns grouped into six classes: solid (419), striped (534), dotted (315), checkered (492), zigzag (407), and floral (582). In addition to the classes and images, the dataset comes with 8 other features: original width, original height, crop X, crop Y, crop width, crop height, and scales. These features will be used to reconstruct the images in the dataset. In addition to the images in the CSV file, the dataset also contains 400 fabric pattern images in PNG format, grouped into their respective patterns by folder location. We will be using Jupyter Notebooks to import and experiment with the dataset.

### Technology Framework
* PyTorch (back-end model)
* Django (front-end interface)
* Amazon AWS (hosting environment)

We consider two popular deep learning frameworks, TensorFlow and PyTorch. Ultimately, we decided to use PyTorch for our project given several considerations. Briefly, PyTorch is a popular deep learning framework that was developed by Facebook’s AI Research lab (FAIR) in 2016. It is an open source library for the Python programming language used to develop deep learning applications in computer vision and natural language processing. PyTorch has grown in popularity for its simplicity, ease of use, efficient memory usage, and flexibility. One of the main reasons we chose to use this library over TensorFlow is that it is integrated well with the Python language whereas TensorFlow is less of a pythonic framework and more of a new language. Additionally, performance in PyTorch is optimized automatically via parallelism where the intensive computational work during the training process is distributed among multiple CPU or GPU cores.

### Architecture
Our core architecture design includes two main components: Fabric Pattern Generator (component 1) and Segmentation & Masking (component 2). 

![](/Images/Project_Architecture.png?raw=true "Project architecture pic")

In component 1, we apply the Deep Convolutional Generative Adversarial Network (DCGAN) by training with various textile pattern datasets. The output of this component 1 will be a neural network generated image input for component 2. In component 2, another pre-trained neural network model will perform image segmentation of clothing patterns and mask the new pattern over the fashion items to produce a result.

### Model 
DCGAN Model is the architecture being used for fabric pattern generation in this project. The advantage of DCGAN is its continuous improvement between the Generator and Discriminator Networks by improving the performance while reducing the loss of both networks to produce the best fake images. Below is the neural network structure of the Generator Network and Discriminator Network 

![](/Images/DCGAN_architecture.png?raw=true "DCGAN architecture pic")

With the component 2 (Segmentation & Masking), we leverage the pre-trained model (Unet_2020-10-30). This model weights for clothe segmentation were trained over the Kaggle dataset - iMaterialist (Fashion) 2019 at FGVC6. 

### Website 
We intend on building a website as a “nice to have” feature. Upon completion of our model, should time allow, we will create a website that will allow users to interact with it. The first stage of this website will focus on pattern generation. We will allow users to customize their design preferences (e.g. stripes, florals) and output a pattern based on their inputs. They will be able to download the pattern as an image file to their own devices, and use it as they wish. Further “nice to have” features on our website will include visualizing the patterns on some items or on AI generated sewing patterns - given we are able to complete this model.

### Cited Sources
* Reading Sources:
  * How long does it take to manufacture custom clothing? Intrepid Sourcing & Services. (2021, December 3). Retrieved December 9, 2021, from https://intrepidsourcing.com/trade-wiki/how-long-does-it-take-to-manufacture-custom-clothing/.

  * Quick Answer: How Much Should I Charge For Designing Clothes? Outrightdigitalmedia.com. (n.d.). Retrieved December 9, 2021, from https://outrightdigitalmedia.com/qa/quick-answer-how-much-should-i-charge-for-designing-clothes.html. 

  * Stearns, L., Findlater, L., & Froehlich, J. E. (2018, October 8). Applying Transfer Learning to Recognize Clothing Patterns Using a Finger-Mounted Camera. 

* Model Sources:
  * Iglovikov, Vladimir. “Ternaus/cloths_segmentation: Code for Binary Segmentation of Cloths.” Code for Binary Segmentation of Various Cloths, GitHub, https://github.com/ternaus/cloths_segmentation. 

  * “DCGAN Tutorial.” DCGAN Tutorial - PyTorch Tutorials 1.10.1+cu102 Documentation, PyTorch, https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html.

* Data Sources:
  * lstearns86. (n.d.). Lstearns86/clothing-pattern-dataset: A large dataset containing images of clothing patterns. GitHub. Retrieved December 1, 2021, from https://github.com/lstearns86/clothing-pattern-dataset. 

  * Additional patterns from web-scraping the following sites:
Fashion Fabrics Club, https://www.fashionfabricsclub.com
Online Fabric Store, https://www.onlinefabricstore.com


