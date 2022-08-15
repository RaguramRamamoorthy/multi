import streamlit as st
from PIL import Image
import torch
import torchvision
import numpy as np

# Load the model and set in eval
resnet18 = torchvision.models.resnet18(pretrained=True)
resnet18.fc = torch.nn.Linear(in_features=512, out_features=3)

resnet18.load_state_dict(torch.load('pages/covid_classifier.pt'))
resnet18.eval()

class_names = ['normal', 'viral', 'covid']

train_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize(size=(224, 224)),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

test_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize(size=(224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


def predict_image_class(image):
    # image = Image.open(image_path).convert('RGB')
    image = image.convert('RGB')
    image = test_transform(image)
    # Please note that the transform is defined already in a previous code cell
    image = image.unsqueeze(0)
    output = resnet18(image)[0]
    probabilities = torch.nn.Softmax(dim=0)(output)
    probabilities = probabilities.cpu().detach().numpy()
    predicted_class_index = np.argmax(probabilities)
    predicted_class_name = class_names[predicted_class_index]

    return probabilities, predicted_class_index, predicted_class_name


st.title("COVID 19 Detector App")
st.text("Upload a Chest X-Ray for diagnosis")

uploaded_file = st.file_uploader("Choose a Chest X-Ray....", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded X-ray image', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    probabilities, predicted_class_index, predicted_class_name = predict_image_class(image)
    st.write(predicted_class_name)

st.text("If you need Chest-Xray images for testing the App")
st.text("download a zip folder from here...")

with open("pages/images.zip", "rb") as fp:
    btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="pages/images.zip",
        mime="application/zip"
    )
