
import os
from openvino.inference_engine import IENetwork, IEPlugin

model_xml = "/home/tno/yolo/yolo_V3/openVino/yolov3_IR.xml"
model_bin = os.path.splitext(model_xml)[0] + ".bin"

net = IENetwork(model=model_xml, weights=model_bin)
#plugin = IEPlugin(device="MYRIAD")
