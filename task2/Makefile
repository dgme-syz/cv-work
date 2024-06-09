
PYTHON = python
DATAROOT = ./data/WIDER
VALDATA = ./data/WIDER/wider_face_split/wider_face_test_filelist.txt
VALDATASET = ./data/WIDER/WIDER_test/images
VALLIST = ./data/WIDER/wider_face_split/wider_face_test_filelist.txt
CHECKPOINT = ./weights/checkpoint_50.pth
PT = ./weights/yolov5n-face.pt


RES1 = ./results/tiny
RES2 = ./results/yolov5


exp1:
	python ./tiny-face/evaluate_model.py $(VALDATA) --dataset-root $(DATAROOT) --checkpoint $(CHECKPOINT) --split test --results_dir $(RES1)
exp2:
	python ./yolov5-face/test_widerface.py --weights $(PT) --save_folder $(RES2) --dataset_folder $(VALDATASET) --folder_pic $(VALLIST)
test1:
	cd ./widerface_evaluate/ && python ./setup.py build_ext --inplace && python ./evaluation.py -p ../$(RES1) -g ./ground_truth
test2:
	cd ./widerface_evaluate/ && python ./setup.py build_ext --inplace && python ./evaluation.py -p ../$(RES2) -g ./ground_truth
detect1:
	python ./tiny-face/detect_image.py --checkpoint ./weights/checkpoint_50.pth --output_path ./detect/tiny/ --image_path ./src 
detect2:
	python ./yolov5-face/detect_face.py --weights ./weights/yolov5n-face.pt --project ./detect/yolov5/ --source ./src --save-img --view-img
clean:
	rm -rf $(RES1) $(RES2)