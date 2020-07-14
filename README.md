# Data_Shanghai_Plume_Plot

> 2017年12月，中国海洋大学姚小红课题组、上海交通大学彭仲仁课题组与天璇无人机公司合作，于上海进行空气污染观测，本文是对数据的说明。

### 1. 背景介绍

&nbsp; 一个热力学系统是趋向于熵增的。排放到大气中的污染物，本来就趋向于扩散和分子间距离增大。所谓的污染物累积，是因为物质在空间上的分布不均匀 (集中分布在近地面)。 这种污染天气可以看作是一种熵减现象。根据热力学第二定律，如果是想让熵减，变无序为有序，需要做功，需要吸收能量。而做功过程，其实发生在污染天气发生前的清洁蓝天。“福兮祸之所伏”，在晴空阳光照射下，大量气体转化为超细颗粒物，这些颗粒物又作为载体继续吸纳污染物。因此在污染天气发生之后，再进行的排放源控制是效率很低的方式。往往污染天气的消失只是因为冷空气过境、大风吹走了雾霾或者强降雨天气使污染物降落在地面上。

![气体团簇向不同直径的颗粒物的转变。](https://upload-images.jianshu.io/upload_images/17085473-312e62cba465670a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&nbsp; 环保部门每小时发布的AQI各项污染物浓度是质量浓度(对于颗粒物是µg/m<sup>3</sup>)。但是真正决定颗粒物对人体健康影响的参数是数浓度 (个/cm<sup>3</sup>)。由球形粒子的质量公式 m=ρV= 4ρR<sup>3</sup> /3，可知：PM<sub>2.5</sub>，亦即2500 纳米(nm) 以下的颗粒物的质量，是50纳米颗粒物的一万倍以上。500纳米以下的颗粒物约占80%的颗粒物总数量，能穿透肺泡膜；而微米级别颗粒物约占90%的质量。10000个/cm<sup>3</sup> 。在污染天气，能见度较低。这是因为颗粒物经过米氏散射可见光造成，而这种散射需要颗粒物的粒径接近或大于可见光波长，也就是说粒径较大的微米(µm)级别的颗粒物占据主导。所以雾霾天气的颗粒物数浓度反而不高。

&nbsp; 由此可见，新生成的纳米颗粒物才是污染天气的前奏，就像2020年1月武汉出现的那十几例新冠肺炎疫情一样。在污染物质量浓度爆发后再去控制排放源，为时已晚。在污染源头去捕捉纳米颗粒物的生成和增长过程，对理解大气细颗粒物PM<sub>2.5</sub>造成的空气污染有重要意义。


### 2. 方法论 

&nbsp; 测定纳米颗粒物的数浓度一般使用电化学法。其原理是先将有机溶剂加热为蒸汽，蒸汽在颗粒物表面达到超饱和凝结。达到超饱和后，根据开尔文效应，有机蒸汽的凝结就和湿度没有关系了，这时主要是颗粒物的粒径对凝结起主要作用; 之所以有个“电”字，是因为接下来，仪器将气流通过接上电流的正极和负极之间。我们知道，一个物质受到电场力的大小是和其质量和所加电荷有关，而电场力又直接决定了物质的运动轨迹。也就是说，大粒径的颗粒物运动轨迹较长，落到较远位置，细粒径颗粒物运动轨迹较短，落到较近的位置，从而达到分别计数的目的。最终计算不同粒径段的颗粒物数浓度时，开尔文效应和电场力效应这两种机理都考虑在内。代表性仪器是SMPS(Scanning Mobility Particle Sizer)。

&nbsp; 电化学法测量的粒径谱可以达到10 nm的级别，这基本是现在仪器厂商的极限。电化学方法是经典物理公式的完美实现，但是放电装置非常脆弱，SMPS仪器必须在保证放电可靠性和电荷稳定性的前提下实现体积的最小化，确实是两难处境。而且，仪器测量的分辨率一般是秒级别，这么强大的放电频率很容易使仪器的放电装置短时间内报废。电化学法的测量误差是分为系统性误差和随机性误差，和仪器的配件使用寿命有关。例如某个粒径段（通常是纳米级别）的颗粒物在短时间内突然上升-下降-上升了好几倍，而其他粒径段无异常，这是随机性误差。而系统性误差主要来源于计算公式中对气溶胶密度的设定。本次测量设定为**1.2 g/cc**。实际排放源的气溶胶密度要大于该值，但是高空处的气溶胶密度又小于该值。

### 3. 八次测量实验结果分析 

![2017-12-19 in an urban site.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/2017-12-19%20in%20an%20urban%20site.png)

![TN versus GMD, 2017-12-19 in an urban site.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%202017-12-19%20in%20an%20urban%20site.png)

![2017-12-21 in a road site.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/2017-12-21%20in%20a%20road%20site.png)

![TN versus GMD, 2017-12-21 in a road site.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%202017-12-21%20in%20a%20road%20site.png)

![Flight-1 in 2017-12-21 AM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/Flight-1%20in%202017-12-21%20AM.png)

![TN versus GMD, Flight-1 in 2017-12-21 AM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%20Flight-1%20in%202017-12-21%20AM.png)

![Flight-2 in 2017-12-21 PM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/Flight-2%20in%202017-12-21%20PM.png)

![TN versus GMD, Flight-2 in 2017-12-21 PM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%20Flight-2%20in%202017-12-21%20PM.png)

![Flight-3 in 2017-12-22 AM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/Flight-3%20in%202017-12-22%20AM.png)

![TN versus GMD, Flight-3 in 2017-12-22 AM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%20Flight-3%20in%202017-12-22%20AM.png)

![Flight-4 in 2017-12-22 AM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/Flight-4%20in%202017-12-22%20AM.png)

![TN versus GMD, Flight-4 in 2017-12-22 AM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%20Flight-4%20in%202017-12-22%20AM.png)

![Flight-5 in 2017-12-22 PM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/Flight-5%20in%202017-12-22%20PM.png)

![TN versus GMD, Flight-5 in 2017-12-22 PM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%20Flight-5%20in%202017-12-22%20PM.png)

![Flight-6 in 2017-12-22 PM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/Flight-6%20in%202017-12-22%20PM.png)

![TN versus GMD, Flight-6 in 2017-12-22 PM.](https://github.com/Limin-Feng1993/Data_Shanghai_Plume_Plot/raw/master/Fig/TN%20versus%20GMD%2C%20Flight-6%20in%202017-12-22%20PM.png)

### 4. 结论与展望 
