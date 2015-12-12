import os
import os.path
from shutil import copy

file="D:\Program Files (x86)\Tencent\QQ\Plugin\Com.Tencent.Advertisement\Bundle.rdb"
if os.path.exists(file):
	os.remove(file)

else:
	print("no such file")
ad="D:\Program Files (x86)\Tencent\QQ\Plugin\Com.Tencent.Advertisement"
if not os.path.isdir(ad):
	pass
else:
	adv='D:\Program Files (x86)\Tencent\QQ\Plugin\Com.Tencent.Advertisement\_ad\Bundle.rdb'
	copy(adv,ad)
	print("have ad")
input()
