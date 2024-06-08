
PYTHON = python
DATAROOT = ./data/WIDER
VALDATA = ./data/WIDER/wider_face_split/wider_face_val_bbx_gt.txt
VALDATASET = ./data/WIDER/WIDER_val/images
VALLIST = ./data/WIDER/WIDER_val/wider_val.txt
CHECKPOINT = ./weights/checkpoint_50.pth
PT = ./weights/yolov5n-face.pt


RES1 = ./results/tiny
RES2 = ./results/yolov5


exp1:
	python ./tiny-face/evaluate_model.py $(VALDATA) --dataset-root $(DATAROOT) --checkpoint $(CHECKPOINT) --split val --results_dir $(RES1)
exp2:
	python ./yolov5-face/test_widerface.py --weights $(PT) --save_folder $(RES2) --dataset_folder $(VALDATASET) --folder_pic $(VALLIST)
test1:
	cd ./widerface_evaluate/ && python ./setup.py build_ext --inplace && python ./evaluation.py -p ../$(RES1) -g ./ground_truth
test2:
	cd ./widerface_evaluate/ && python ./setup.py build_ext --inplace && python ./evaluation.py -p ../$(RES2) -g ./ground_truth
clean:
	rm -rf $(RES1) $(RES2)