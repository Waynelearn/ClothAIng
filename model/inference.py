import torch
import torchvision.models as models
from torchvision import transforms
from torch.autograd import Variable
from PIL import Image
import torch.nn as nn

MODEL_PATH = "model/atr-recognition-stage-2-resnet34.pkl"
DATA_PATH = ".\\"
CLASSES_PATH = ".\\attribute-classes.txt"

class ClassificationModel():
    
    def __init__(self):
        return
        
    def load(self, model_path, labels_path,  eval=False):
        self.model = torch.load(model_path)
        self.model = nn.Sequential(self.model)
        
        self.labels = open(labels_path, 'r').read().splitlines()
        
        if eval:
            print(model.eval())
        return
    
    def predict(self, image_path):
        
        device = torch.device("cpu")
        img = Image.open(image_path)
        
        test_transforms = transforms.Compose([transforms.Resize(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                           [0.229, 0.224, 0.225])
                                     ])
        
        image_tensor = test_transforms(img).float()
        image_tensor = image_tensor.unsqueeze_(0)
        inp = Variable(image_tensor)
        inp = inp.to(device)
        output = self.model(inp)
        index = output.data.cpu().numpy().argmax()
        return self.labels[index]

learner = ClassificationModel()
learner.load(MODEL_PATH, CLASSES_PATH)

import os

path = "instaPoster/pictures/resized"
files = os.listdir("instaPoster/pictures/resized")
num = len(files)
predictions = [learner.predict(f"instaPoster/pictures/resized/{name}") for name in files]
print(predictions)
with open("output.txt",'w') as f:
    for i in predictions:
        f.write(i)
        f.write("\n")


