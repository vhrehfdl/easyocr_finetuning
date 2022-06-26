# easyocr_finetuning
This repository is a code that fine-tunes the text recognitino model of easy ocr, builds it, and uses it.
  
You can use it by opening easyocr_finetuning.ipynb in colab and running the cell.


## 1. Clone easyocr-finetuning repository 
Clone the github repository.


## 2.Set Environment
If the problem persists even after configuring the environment, click Restart Runtime and try again.


## 3.Make train data
To use ai hub data, you only need to use 3-1.   
If there is no ai hub data, use 3-2 to create the data.

### 3-1. Using AI hub OCR data
- https://aihub.or.kr/node/33987
- It uses AI hub OCR data to crop text and transforms the data into a learnable form.

### 3-2. Generate Korean text image
If you do not use AI hub data, you can create your own data.  
If you want to use the data, you can run the collaboratory cell and skip it if you don't want to.

## 4.Transform image and text to data
Only ai hub data is used here.   
(If you want to use the Korean data created in 3-2, combine the folders into one.)

## 5.Fine tuning
Fine tuning proceeds when the cell of the collaboration is executed.
You can check the learning log by looking at the saved_models folder.
When learning is achieved, stop the cell and start the next cell.

## 6. Apply Fine tuning model to easy ocr 
Import and use the fine tuning model as a custom path.

## 7. Evaluation
Performance is measured based on how many cropped images are fitted.

