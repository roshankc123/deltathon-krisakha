# -*- coding: utf-8 -*-
"""Predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y8AQFaTu0IbmcGvKMORh_wa7c6hHeRn_
"""

import torchvision
import torch
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as T
import numpy as np
from sklearn.preprocessing import LabelEncoder
import torch.nn as nn
from torchvision.models import vgg16
from sklearn.model_selection import train_test_split
import torch.nn.functional as Fun
import cv2

device = 'cuda' if torch.cuda.is_available() else 'cpu'

transforms = T.Compose(
        [T.ToTensor(),
        T.Normalize(mean=[0.485,
           0.456, 0.406],std=[0.229, 0.224, 0.225])]
        )

    
def read_transform(img):
        f = img
        im = cv2.imread(f)
        im = cv2.resize(im, (224,224))
        im = transforms(im)
        return torch.tensor(im,dtype=torch.float).to(device)

def get_model(no_classes):
    model = torchvision.models.vgg16(pretrained=True)
    for param in model.features.parameters():
                   param.requires_grad = False
    model.avgpool = model.avgpool = nn.AdaptiveAvgPool2d(output_size=(1,1))
    model.classifier = nn.Sequential(nn.Flatten(),
                                   nn.Linear(512, 128),
                                   nn.ReLU(),
                                   nn.Dropout(0.2),
                                   nn.Linear(128, no_classes),
                                   nn.Sigmoid())

    return model.to(device)

def load_model(model_path, classes):
  model = get_model(classes)
  state_dict = torch.load(model_path)
  return model,state_dict

apple_classes = {'Apple___Apple_scab': 0,
 'Apple___Black_rot': 1,
 'Apple___Cedar_apple_rust': 2,
 'Apple___healthy': 3},

Maize_classes = {'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 0,
 'Corn_(maize)___Common_rust_': 1,
 'Corn_(maize)___Northern_Leaf_Blight': 2,
 'Corn_(maize)___healthy': 3},
 
Potato_classes ={'Potato___Early_blight': 0, 'Potato___Late_blight': 1, 'Potato___healthy': 2}

def predict(image, crop.lower()):
  img = read_transform(image)
  img = img.to(device)
  if crop=='rice':
    model, state_dict = load_model('/content/rice.pth', 3)
    model.load_state_dict(state_dict)
  elif crop == 'maize':
    model, state_dict = load_model('/content/maize.pth', 4)
    model.load_state_dict(state_dict)  
  elif crop=='apple':
    model, state_dict = load_model('/content/appple.pth', 4)
    model.load_state_dict(state_dict)
  elif crop=='potato';
    model, state_dict = load_model('/content/potato.pth', 3)
    model.load_state_dict(state_dict)
  output = model(img.unsqueeze_(0))
  pred, conf = output.max(-1)
  
  return conf.item(), pred

predict(image_path, crop)