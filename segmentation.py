
import torch
from UNET_model import UNET
import time
import glob
from matplotlib import pyplot as plt
import torchvision.transforms as transforms
import torchvision
import cv2

def segment(model_wt:str, file_path:str)->None:
    model = UNET(in_channels=3, out_channels=1).to('cuda')
    model.load_state_dict(torch.load(model_wt))

    model.eval()
    path = file_path
    #for name in glob.glob(path +  r'/*.jpg'):
    img = cv2.imread(path)
    img = cv2.resize(img, (160,160))
    

    # Convert the image to a PyTorch tensor
    transform = transforms.ToTensor()
    tensor = transform(img)

    # Add a batch dimension and convert the tensor to float
    tensor = tensor.unsqueeze(dim=0).float()  # Convert to float here

    # Ensure the tensor is on the same device as the model
    # If your model is on GPU, you should also move the tensor to GPU
    if torch.cuda.is_available():
        tensor = tensor.cuda()
        model = model.cuda()

    # Perform inference
    with torch.inference_mode():
        preds = torch.sigmoid(model(tensor))
        preds = (preds > 0.5).float()

        # Save the prediction image
        save_path = r'images\segmented_path.png'
        torchvision.utils.save_image(preds, save_path)
    return save_path