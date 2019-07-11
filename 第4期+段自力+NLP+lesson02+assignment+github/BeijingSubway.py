# coding=gbk
from collections import defaultdict

city_connection = defaultdict(list)
# citys = ['苹果园', '古城', '八角游乐园', '八宝山', '玉泉路', '五棵松', '万寿路', '公主坟', '军事博物馆', '木樨地', '南礼士路', '复兴门', '西单', '天安门西', '天安门东', '王府井', '东单', '建国门', '永安里', '国贸', '大望路', '四惠', '四惠东', '西直门', '车公庄', '阜成门', '长椿街', '宣武门', '和平门', '前门', '崇文门', '北京站', '朝阳门', '东四十条', '东直门', '雍和宫', '安定门', '鼓楼大街', '积水潭', '安河桥北', '北宫门', '西苑', '圆明园', '北京大学东门', '中关村', '海淀黄庄', '人民大学', '魏公村', '国家图书馆', '动物园', '新街口', '平安里', '西四', '灵境胡同', '菜市口', '陶然亭', '北京南站', '马家堡', '角门西', '公益西桥', '天通苑北', '天通苑', '天通苑南', '立水桥', '立水桥南', '北苑路北', '大屯路东', '惠新西街北口', '惠新西街南口', '和平西桥', '和平里北街', '北新桥', '张自忠路', '东四', '灯市口', '磁器口', '天坛东门', '蒲黄榆', '刘家窑', '宋家庄', '海淀五路居', '慈寿寺', '花园桥', '白石桥南', '车公庄西', '北海北', '南锣鼓巷', '东大桥', '呼家楼', '金台路', '十里堡', '青年路', '褡裢坡', '黄渠', '常营', '草房', '物资学院路', '通州北关', '通运门', '北运河西', '北运河东', '郝家府', '东夏园', '潞城', '北京西站', '湾子', '达官营', '广安门内', '虎坊桥', '珠市口', '桥湾', '广渠门内', '广渠门外', '双井', '九龙山', '大郊亭', '百子湾', '化工', '南楼梓庄', '欢乐谷景区', '垡头', '双合', '焦化厂', '朱辛庄', '育知路', '平西府', '回龙观东大街', '霍营', '育新', '西小口', '永泰庄', '林萃桥', '森林公园南门', '奥林匹克公园', '奥体中心', '北土城', '安华桥', '安德里北街', '什刹海', '白堆子', '六里桥东', '六里桥', '七里庄', '丰台东大街', '丰台南路', '科怡路', '丰台科技园', '郭公庄', '巴沟', '苏州街', '知春里', '知春路', '西土城', '牡丹园', '健德门', '安贞门', '芍药居', '太阳宫', '三元桥', '亮马桥', '农业展览馆', '团结湖', '金台夕照', '劲松', '潘家园', '十里河', '分钟寺', '成寿寺', '石榴庄', '大红门', '角门东', '草桥', '纪家庙', '首经贸', '丰台站', '泥洼', '西局', '莲花桥', '西钓鱼台', '车道沟', '长春桥', '火器营', '大钟寺', '五道口', '上地', '西二旗', '龙泽', '回龙观', '北苑', '望京西', '光熙门', '柳芳', '张郭庄', '园博园', '大瓦窑', '郭庄子', '大井', '陶然桥', '永定门外', '景泰', '方庄', '南八里庄', '北工大西门', '平乐园', '红庙', '朝阳公园', '枣营', '东风北桥', '将台', '高家园', '望京南', '阜通', '望京', '东湖渠', '来广营', '善各庄', '清华东路西口', '六道口', '北沙滩', '安立路', '关庄', '望京东', '崔各庄', '马泉营', '孙河', '国展', '花梨坎', '后沙峪', '南法信', '石门', '顺义', '俸伯', '高碑店', '传媒大学', '双桥', '管庄', '八里桥', '通州北苑', '果园', '九棵树', '梨园', '临河里', '土桥', '昌平西山口', '十三陵景区', '昌平', '昌平东关', '北邵洼', '南邵', '沙河高教园', '沙河', '巩华城', '生命科学园', '肖村', '小红门', '旧宫', '亦庄桥', '亦庄文化园', '万源街', '荣京东街', '荣昌东街', '同济南路', '经海路', '次渠南', '次渠', '新宫', '西红门', '高米店北', '高米店南', '枣园', '清源路', '黄村西大街', '黄村火车站', '义和庄', '生物医药基地', '天宫院', '大葆台', '稻田', '长阳', '篱笆房', '广阳城', '良乡大学城北', '良乡大学城', '良乡大学城西', '良乡南关', '苏庄', 'T3航站楼', 'T2航站楼']
# city_setcions = ['苹果园――古城', '古城――八角游乐园', '八角游乐园――八宝山', '八宝山――玉泉路', '玉泉路――五棵松', '五棵松――万寿路', '万寿路――公主坟', '公主坟――军事博物馆', '军事博物馆――木樨地', '木樨地――南礼士路', '南礼士路――复兴门', '复兴门――西单', '西单――天安门西', '天安门西――天安门东', '天安门东――王府井', '王府井――东单', '东单――建国门', '建国门――永安里', '永安里――国贸', '国贸――大望路', '大望路――四惠', '四惠――四惠东', '西直门――车公庄', '车公庄――阜成门', '阜成门――复兴门', '复兴门――长椿街', '长椿街――宣武门', '宣武门――和平门', '和平门――前门', '前门――崇文门', '崇文门――北京站', '北京站――建国门', '建国门――朝阳门', '朝阳门――东四十条', '东四十条――东直门', '东直门――雍和宫', '雍和宫――安定门', '安定门――鼓楼大街', '鼓楼大街――积水潭', '积水潭――西直门', '安河桥北――北宫门', '北宫门――西苑', '西苑――圆明园', '圆明园――北京大学东门', '北京大学东门――中关村', '中关村――海淀黄庄', '海淀黄庄――人民大学', '人民大学――魏公村', '魏公村――国家图书馆', '国家图书馆――动物园', '动物园――西直门', '西直门――新街口', '新街口――平安里', '平安里――西四', '西四――灵境胡同', '灵境胡同――西单', '西单――宣武门', '宣武门――菜市口', '菜市口――陶然亭', '陶然亭――北京南站', '北京南站――马家堡', '马家堡――角门西', '角门西――公益西桥', '天通苑北――天通苑', '天通苑――天通苑南', '天通苑南――立水桥', '立水桥――立水桥南', '立水桥南――北苑路北', '北苑路北――大屯路东', '大屯路东――惠新西街北口', '惠新西街北口――惠新西街南口', '惠新西街南口――和平西桥', '和平西桥――和平里北街', '和平里北街――雍和宫', '雍和宫――北新桥', '北新桥――张自忠路', '张自忠路――东四', '东四――灯市口', '灯市口――东单', '东单――崇文门', '崇文门――磁器口', '磁器口――天坛东门', '天坛东门――蒲黄榆', '蒲黄榆――刘家窑', '刘家窑――宋家庄', '海淀五路居――慈寿寺', '慈寿寺――花园桥', '花园桥――白石桥南', '白石桥南――车公庄西', '车公庄西――车公庄', '车公庄――平安里', '平安里――北海北', '北海北――南锣鼓巷', '南锣鼓巷――东四', '东四――朝阳门', '朝阳门――东大桥', '东大桥――呼家楼', '呼家楼――金台路', '金台路――十里堡', '十里堡――青年路', '青年路――褡裢坡', '褡裢坡――黄渠', '黄渠――常营', '常营――草房', '草房――物资学院路', '物资学院路――通州北关', '通州北关――通运门', '通运门――北运河西', '北运河西――北运河东', '北运河东――郝家府', '郝家府――东夏园', '东夏园――潞城', '北京西站――湾子', '湾子――达官营', '达官营――广安门内', '广安门内――菜市口', '菜市口――虎坊桥', '虎坊桥――珠市口', '珠市口――桥湾', '桥湾――磁器口', '磁器口――广渠门内', '广渠门内――广渠门外', '广渠门外――双井', '双井――九龙山', '九龙山――大郊亭', '大郊亭――百子湾', '百子湾――化工', '化工――南楼梓庄', '南楼梓庄――欢乐谷景区', '欢乐谷景区――垡头', '垡头――双合', '双合――焦化厂', '朱辛庄――育知路', '育知路――平西府', '平西府――回龙观东大街', '回龙观东大街――霍营', '霍营――育新', '育新――西小口', '西小口――永泰庄', '永泰庄――林萃桥', '林萃桥――森林公园南门', '森林公园南门――奥林匹克公园', '奥林匹克公园――奥体中心', '奥体中心――北土城', '北土城――安华桥', '安华桥――安德里北街', '安德里北街――鼓楼大街', '鼓楼大街――什刹海', '什刹海――南锣鼓巷', '国家图书馆――白石桥南', '白石桥南――白堆子', '白堆子――军事博物馆', '军事博物馆――北京西站', '北京西站――六里桥东', '六里桥东――六里桥', '六里桥――七里庄', '七里庄――丰台东大街', '丰台东大街――丰台南路', '丰台南路――科怡路', '科怡路――丰台科技园', '丰台科技园――郭公庄', '巴沟――苏州街', '苏州街――海淀黄庄', '海淀黄庄――知春里', '知春里――知春路', '知春路――西土城', '西土城――牡丹园', '牡丹园――健德门', '健德门――北土城', '北土城――安贞门', '安贞门――惠新西街南口', '惠新西街南口――芍药居', '芍药居――太阳宫', '太阳宫――三元桥', '三元桥――亮马桥', '亮马桥――农业展览馆', '农业展览馆――团结湖', '团结湖――呼家楼', '呼家楼――金台夕照', '金台夕照――国贸', '国贸――双井', '双井――劲松', '劲松――潘家园', '潘家园――十里河', '十里河――分钟寺', '分钟寺――成寿寺', '成寿寺――宋家庄', '宋家庄――石榴庄', '石榴庄――大红门', '大红门――角门东', '角门东――角门西', '角门西――草桥', '草桥――纪家庙', '纪家庙――首经贸', '首经贸――丰台站', '丰台站――泥洼', '泥洼――西局', '西局――六里桥', '六里桥――莲花桥', '莲花桥――公主坟', '公主坟――西钓鱼台', '西钓鱼台――慈寿寺', '慈寿寺――车道沟', '车道沟――长春桥', '长春桥――火器营', '火器营――巴沟', '西直门――大钟寺', '大钟寺――知春路', '知春路――五道口', '五道口――上地', '上地――西二旗', '西二旗――龙泽', '龙泽――回龙观', '回龙观――霍营', '霍营――立水桥', '立水桥――北苑', '北苑――望京西', '望京西――芍药居', '芍药居――光熙门', '光熙门――柳芳', '柳芳――东直门', '张郭庄――园博园', '园博园――大瓦窑', '大瓦窑――郭庄子', '郭庄子――大井', '大井――七里庄', '七里庄――西局', '北京南站――陶然桥', '陶然桥――永定门外', '永定门外――景泰', '景泰――蒲黄榆', '蒲黄榆――方庄', '方庄――十里河', '十里河――南八里庄', '南八里庄――北工大西门', '北工大西门――平乐园', '平乐园――九龙山', '九龙山――大望路', '大望路――红庙', '红庙――金台路', '金台路――朝阳公园', '朝阳公园――枣营', '枣营――东风北桥', '东风北桥――将台', '将台――高家园', '高家园――望京南', '望京南――阜通', '阜通――望京', '望京――东湖渠', '东湖渠――来广营', '来广营――善各庄', '清华东路西口――六道口', '六道口――北沙滩', '北沙滩――奥林匹克公园', '奥林匹克公园――安立路', '安立路――大屯路东', '大屯路东――关庄', '关庄――望京西', '望京西――望京', '望京――望京东', '望京东――崔各庄', '崔各庄――马泉营', '马泉营――孙河', '孙河――国展', '国展――花梨坎', '花梨坎――后沙峪', '后沙峪――南法信', '南法信――石门', '石门――顺义', '顺义――俸伯', '四惠东――高碑店', '高碑店――传媒大学', '传媒大学――双桥', '双桥――管庄', '管庄――八里桥', '八里桥――通州北苑', '通州北苑――果园', '果园――九棵树', '九棵树――梨园', '梨园――临河里', '临河里――土桥', '昌平西山口――十三陵景区', '十三陵景区――昌平', '昌平――昌平东关', '昌平东关――北邵洼', '北邵洼――南邵', '南邵――沙河高教园', '沙河高教园――沙河', '沙河――巩华城', '巩华城――朱辛庄', '朱辛庄――生命科学园', '生命科学园――西二旗', '宋家庄――肖村', '肖村――小红门', '小红门――旧宫', '旧宫――亦庄桥', '亦庄桥――亦庄文化园', '亦庄文化园――万源街', '万源街――荣京东街', '荣京东街――荣昌东街', '荣昌东街――同济南路', '同济南路――经海路', '经海路――次渠南', '次渠南――次渠', '公益西桥――新宫', '新宫――西红门', '西红门――高米店北', '高米店北――高米店南', '高米店南――枣园', '枣园――清源路', '清源路――黄村西大街', '黄村西大街――黄村火车站', '黄村火车站――义和庄', '义和庄――生物医药基地', '生物医药基地――天宫院', '郭公庄――大葆台', '大葆台――稻田', '稻田――长阳', '长阳――篱笆房', '篱笆房――广阳城', '广阳城――良乡大学城北', '良乡大学城北――良乡大学城', '良乡大学城――良乡大学城西', '良乡大学城西――良乡南关', '良乡南关――苏庄', '东直门――三元桥', '三元桥――T3航站楼', 'T3航站楼――T2航站楼', 'T2航站楼――三元桥']
stationDistance = {'苹果园――古城': 2606, '古城――八角游乐园': 1921, '八角游乐园――八宝山': 1953, '八宝山――玉泉路': 1479, '玉泉路――五棵松': 1810, '五棵松――万寿路': 1778, '万寿路――公主坟': 1313, '公主坟――军事博物馆': 1172, '军事博物馆――木樨地': 1166, '木樨地――南礼士路': 1291, '南礼士路――复兴门': 424, '复兴门――西单': 1590, '西单――天安门西': 1217, '天安门西――天安门东': 925, '天安门东――王府井': 852, '王府井――东单': 774, '东单――建国门': 1230, '建国门――永安里': 1377, '永安里――国贸': 790, '国贸――大望路': 1385, '大望路――四惠': 1673, '四惠――四惠东': 1714, '西直门――车公庄': 909, '车公庄――阜成门': 960, '阜成门――复兴门': 1832, '复兴门――长椿街': 1234, '长椿街――宣武门': 929, '宣武门――和平门': 851, '和平门――前门': 1171, '前门――崇文门': 1634, '崇文门――北京站': 1023, '北京站――建国门': 945, '建国门――朝阳门': 1763, '朝阳门――东四十条': 1027, '东四十条――东直门': 824, '东直门――雍和宫': 2228, '雍和宫――安定门': 794, '安定门――鼓楼大街': 1237, '鼓楼大街――积水潭': 1766, '积水潭――西直门': 1899, '安河桥北――北宫门': 1363, '北宫门――西苑': 1251, '西苑――圆明园': 1672, '圆明园――北京大学东门': 1295, '北京大学东门――中关村': 887, '中关村――海淀黄庄': 900, '海淀黄庄――人民大学': 1063, '人民大学――魏公村': 1051, '魏公村――国家图书馆': 1658, '国家图书馆――动物园': 1517, '动物园――西直门': 1441, '西直门――新街口': 1025, '新街口――平安里': 1100, '平安里――西四': 1100, '西四――灵境胡同': 869, '灵境胡同――西单': 1011, '西单――宣武门': 815, '宣武门――菜市口': 1152, '菜市口――陶然亭': 1200, '陶然亭――北京南站': 1643, '北京南站――马家堡': 1480, '马家堡――角门西': 827, '角门西――公益西桥': 989, '天通苑北――天通苑': 939, '天通苑――天通苑南': 965, '天通苑南――立水桥': 1544, '立水桥――立水桥南': 1305, '立水桥南――北苑路北': 1286, '北苑路北――大屯路东': 3000, '大屯路东――惠新西街北口': 1838, '惠新西街北口――惠新西街南口': 1122, '惠新西街南口――和平西桥': 1025, '和平西桥――和平里北街': 1059, '和平里北街――雍和宫': 1151, '雍和宫――北新桥': 866, '北新桥――张自忠路': 791, '张自忠路――东四': 1016, '东四――灯市口': 848, '灯市口――东单': 945, '东单――崇文门': 821, '崇文门――磁器口': 876, '磁器口――天坛东门': 1183, '天坛东门――蒲黄榆': 1900, '蒲黄榆――刘家窑': 905, '刘家窑――宋家庄': 1670, '海淀五路居――慈寿寺': 1508, '慈寿寺――花园桥': 1431, '花园桥――白石桥南': 1166, '白石桥南――车公庄西': 1664, '车公庄西――车公庄': 887, '车公庄――平安里': 1443, '平安里――北海北': 1321, '北海北――南锣鼓巷': 1349, '南锣鼓巷――东四': 1937, '东四――朝阳门': 1399, '朝阳门――东大桥': 1668, '东大桥――呼家楼': 845, '呼家楼――金台路': 1450, '金台路――十里堡': 2036, '十里堡――青年路': 1282, '青年路――褡裢坡': 3999, '褡裢坡――黄渠': 1238, '黄渠――常营': 1854, '常营――草房': 1405, '草房――物资学院路': 2115, '物资学院路――通州北关': 2557, '通州北关――通运门': 1468, '通运门――北运河西': 1543, '北运河西――北运河东': 1599, '北运河东――郝家府': 929, '郝家府――东夏园': 1346, '东夏园――潞城': 1194, '北京西站――湾子': 935, '湾子――达官营': 734, '达官营――广安门内': 1874, '广安门内――菜市口': 1374, '菜市口――虎坊桥': 885, '虎坊桥――珠市口': 1205, '珠市口――桥湾': 869, '桥湾――磁器口': 1016, '磁器口――广渠门内': 1138, '广渠门内――广渠门外': 1332, '广渠门外――双井': 1241, '双井――九龙山': 1311, '九龙山――大郊亭': 781, '大郊亭――百子湾': 865, '百子湾――化工': 903, '化工――南楼梓庄': 1464, '南楼梓庄――欢乐谷景区': 906, '欢乐谷景区――垡头': 1679, '垡头――双合': 1304, '双合――焦化厂': 1021, '朱辛庄――育知路': 2318, '育知路――平西府': 1985, '平西府――回龙观东大街': 2056, '回龙观东大街――霍营': 1114, '霍营――育新': 1894, '育新――西小口': 1543, '西小口――永泰庄': 1041, '永泰庄――林萃桥': 2553, '林萃桥――森林公园南门': 2555, '森林公园南门――奥林匹克公园': 1016, '奥林匹克公园――奥体中心': 1667, '奥体中心――北土城': 900, '北土城――安华桥': 1018, '安华桥――安德里北街': 1274, '安德里北街――鼓楼大街': 1083, '鼓楼大街――什刹海': 1188, '什刹海――南锣鼓巷': 902, '国家图书馆――白石桥南': 1096, '白石桥南――白堆子': 943, '白堆子――军事博物馆': 1912, '军事博物馆――北京西站': 1398, '北京西站――六里桥东': 1170, '六里桥东――六里桥': 1309, '六里桥――七里庄': 1778, '七里庄――丰台东大街': 1325, '丰台东大街――丰台南路': 1585, '丰台南路――科怡路': 980, '科怡路――丰台科技园': 788, '丰台科技园――郭公庄': 1347, '巴沟――苏州街': 1110, '苏州街――海淀黄庄': 950, '海淀黄庄――知春里': 975, '知春里――知春路': 1058, '知春路――西土城': 1101, '西土城――牡丹园': 1330, '牡丹园――健德门': 973, '健德门――北土城': 1100, '北土城――安贞门': 1020, '安贞门――惠新西街南口': 982, '惠新西街南口――芍药居': 1712, '芍药居――太阳宫': 1003, '太阳宫――三元桥': 1759, '三元桥――亮马桥': 1506, '亮马桥――农业展览馆': 914, '农业展览馆――团结湖': 853, '团结湖――呼家楼': 1149, '呼家楼――金台夕照': 734, '金台夕照――国贸': 835, '国贸――双井': 1759, '双井――劲松': 1006, '劲松――潘家园': 1021, '潘家园――十里河': 1097, '十里河――分钟寺': 1804, '分钟寺――成寿寺': 1058, '成寿寺――宋家庄': 1677, '宋家庄――石榴庄': 1269, '石榴庄――大红门': 1244, '大红门――角门东': 1130, '角门东――角门西': 1254, '角门西――草桥': 1688, '草桥――纪家庙': 1547, '纪家庙――首经贸': 1143, '首经贸――丰台站': 1717, '丰台站――泥洼': 954, '泥洼――西局': 749, '西局――六里桥': 1584, '六里桥――莲花桥': 2392, '莲花桥――公主坟': 1016, '公主坟――西钓鱼台': 2386, '西钓鱼台――慈寿寺': 1214, '慈寿寺――车道沟': 1590, '车道沟――长春桥': 1205, '长春桥――火器营': 961, '火器营――巴沟': 1495, '西直门――大钟寺': 2839, '大钟寺――知春路': 1206, '知春路――五道口': 1829, '五道口――上地': 4866, '上地――西二旗': 2538, '西二旗――龙泽': 3623, '龙泽――回龙观': 1423, '回龙观――霍营': 2110, '霍营――立水桥': 4785, '立水桥――北苑': 2272, '北苑――望京西': 6720, '望京西――芍药居': 2152, '芍药居――光熙门': 1110, '光熙门――柳芳': 1135, '柳芳――东直门': 1769, '张郭庄――园博园': 1345, '园博园――大瓦窑': 4073, '大瓦窑――郭庄子': 1236, '郭庄子――大井': 2044, '大井――七里庄': 1579, '七里庄――西局': 845, '北京南站――陶然桥': 887, '陶然桥――永定门外': 1063, '永定门外――景泰': 1119, '景泰――蒲黄榆': 1025, '蒲黄榆――方庄': 1486, '方庄――十里河': 1618, '十里河――南八里庄': 1147, '南八里庄――北工大西门': 1276, '北工大西门――平乐园': 1128, '平乐园――九龙山': 897, '九龙山――大望路': 1780, '大望路――红庙': 708, '红庙――金台路': 894, '金台路――朝阳公园': 1085, '朝阳公园――枣营': 1221, '枣营――东风北桥': 2173, '东风北桥――将台': 1600, '将台――高家园': 1171, '高家园――望京南': 676, '望京南――阜通': 1168, '阜通――望京': 903, '望京――东湖渠': 1283, '东湖渠――来广营': 1100, '来广营――善各庄': 1364, '清华东路西口――六道口': 1144, '六道口――北沙滩': 1337, '北沙滩――奥林匹克公园': 1999, '奥林匹克公园――安立路': 1368, '安立路――大屯路东': 938, '大屯路东――关庄': 1087, '关庄――望京西': 2071, '望京西――望京': 1758, '望京――望京东': 1652, '望京东――崔各庄': 2295, '崔各庄――马泉营': 2008, '马泉营――孙河': 3309, '孙河――国展': 3386, '国展――花梨坎': 1615, '花梨坎――后沙峪': 3354, '后沙峪――南法信': 4576, '南法信――石门': 2712, '石门――顺义': 1331, '顺义――俸伯': 2441, '四惠东――高碑店': 1375, '高碑店――传媒大学': 2002, '传媒大学――双桥': 1894, '双桥――管庄': 1912, '管庄――八里桥': 1763, '八里桥――通州北苑': 1700, '通州北苑――果园': 1465, '果园――九棵树': 990, '九棵树――梨园': 1225, '梨园――临河里': 1257, '临河里――土桥': 776, '昌平西山口――十三陵景区': 1213, '十三陵景区――昌平': 3508, '昌平――昌平东关': 2433, '昌平东关――北邵洼': 1683, '北邵洼――南邵': 1958, '南邵――沙河高教园': 5357, '沙河高教园――沙河': 1964, '沙河――巩华城': 2025, '巩华城――朱辛庄': 3799, '朱辛庄――生命科学园': 2367, '生命科学园――西二旗': 5440, '宋家庄――肖村': 2631, '肖村――小红门': 1275, '小红门――旧宫': 2366, '旧宫――亦庄桥': 1982, '亦庄桥――亦庄文化园': 993, '亦庄文化园――万源街': 1728, '万源街――荣京东街': 1090, '荣京东街――荣昌东街': 1355, '荣昌东街――同济南路': 2337, '同济南路――经海路': 2301, '经海路――次渠南': 2055, '次渠南――次渠': 1281, '公益西桥――新宫': 2798, '新宫――西红门': 5102, '西红门――高米店北': 1810, '高米店北――高米店南': 1128, '高米店南――枣园': 1096, '枣园――清源路': 1200, '清源路――黄村西大街': 1214, '黄村西大街――黄村火车站': 987, '黄村火车站――义和庄': 2035, '义和庄――生物医药基地': 2918, '生物医药基地――天宫院': 1811, '郭公庄――大葆台': 1405, '大葆台――稻田': 6466, '稻田――长阳': 4041, '长阳――篱笆房': 2150, '篱笆房――广阳城': 1474, '广阳城――良乡大学城北': 2003, '良乡大学城北――良乡大学城': 1188, '良乡大学城――良乡大学城西': 1738, '良乡大学城西――良乡南关': 1332, '良乡南关――苏庄': 1330, '东直门――三元桥': 2999, '三元桥――T3航站楼': 18329, 'T3航站楼――T2航站楼': 7239, 'T2航站楼――三元桥': 20619}

# 组成地铁站字典
# for city in citys:
#     for city_setcion in city_setcions:
#         if city_setcion.__contains__(city):
#             A1 = city_setcion.replace('――', '').replace(city, '').replace('——', '')
#             if not city_connection[A1].__contains__(city):
#                city_connection[A1].append(city)
#             if not city_connection[city].__contains__(A1):
#                if(len(A1)==1):
#                    A1=city+A1
#                city_connection[city].append(A1)
#
# print(city_connection)

city_connection = {'古城': ['苹果园', '八角游乐园'], '苹果园': ['古城'], '八角游乐园': ['古城', '八宝山'], '八宝山': ['八角游乐园', '玉泉路'], '玉泉路': ['八宝山', '五棵松'], '五棵松': ['玉泉路', '万寿路'], '万寿路': ['五棵松', '公主坟'], '公主坟': ['万寿路', '军事博物馆', '莲花桥', '西钓鱼台'], '军事博物馆': ['公主坟', '木樨地', '白堆子', '北京西站'], '莲花桥': ['公主坟', '六里桥'], '西钓鱼台': ['公主坟', '慈寿寺'], '木樨地': ['军事博物馆', '南礼士路'], '白堆子': ['军事博物馆', '白石桥南'], '北京西站': ['军事博物馆', '湾子', '六里桥东'], '南礼士路': ['木樨地', '复兴门'], '复兴门': ['南礼士路', '西单', '阜成门', '长椿街'], '西单': ['复兴门', '天安门西', '灵境胡同', '宣武门'], '阜成门': ['复兴门', '车公庄'], '长椿街': ['复兴门', '宣武门'], '天安门西': ['西单', '天安门东'], '灵境胡同': ['西单', '西四'], '宣武门': ['西单', '长椿街', '和平门', '菜市口'], '天安门东': ['天安门西', '王府井'], '王府井': ['天安门东', '东单'], '东单': ['王府井', '建国门', '灯市口', '崇文门'], '建国门': ['东单', '永安里', '北京站', '朝阳门'], '灯市口': ['东单', '东四'], '崇文门': ['东单', '前门', '北京站', '磁器口'], '永安里': ['建国门', '国贸'], '北京站': ['建国门', '崇文门'], '朝阳门': ['建国门', '东四十条', '东四', '东大桥'], '国贸': ['永安里', '大望路', '金台夕照', '双井'], '大望路': ['国贸', '四惠', '九龙山', '红庙'], '金台夕照': ['国贸', '呼家楼'], '双井': ['国贸', '广渠门外', '九龙山', '劲松'], '四惠': ['大望路', '四惠东', '东高碑店'], '九龙山': ['大望路', '双井', '大郊亭', '平乐园'], '红庙': ['大望路', '金台路'], '东': ['四惠', '六里桥', '望京'], '东高碑店': ['四惠'], '四惠东': ['四惠', '高碑店'], '高碑店': ['四惠东', '传媒大学'], '车公庄': ['西直门', '阜成门', '白石桥南西', '车公庄西', '平安里'], '西直门': ['车公庄', '积水潭', '动物园', '新街口', '大钟寺'], '积水潭': ['西直门', '鼓楼大街'], '动物园': ['西直门', '国家图书馆'], '新街口': ['西直门', '平安里'], '大钟寺': ['西直门', '知春路'], '白石桥南西': ['车公庄'], '西': ['车公庄', '望京', '良乡大学城'], '平安里': ['车公庄', '新街口', '西四', '北海北'], '和平门': ['宣武门', '前门'], '菜市口': ['宣武门', '陶然亭', '广安门内', '虎坊桥'], '前门': ['和平门', '崇文门'], '磁器口': ['崇文门', '天坛东门', '桥湾', '广渠门内'], '东四十条': ['朝阳门', '东直门'], '东四': ['朝阳门', '张自忠路', '朝阳门十条', '十条东直门', '灯市口', '南锣鼓巷'], '东大桥': ['朝阳门', '呼家楼'], '东直门': ['东四十条', '雍和宫', '柳芳', '三元桥'], '雍和宫': ['东直门', '安定门', '和平里北街', '北新桥'], '柳芳': ['东直门', '光熙门'], '三元桥': ['东直门', '太阳宫', '亮马桥', 'T3航站楼', 'T2航站楼'], '安定门': ['雍和宫', '鼓楼大街'], '和平里北街': ['雍和宫', '和平西桥'], '北新桥': ['雍和宫', '张自忠路'], '鼓楼大街': ['安定门', '积水潭', '安德里北街', '什刹海'], '安德里北街': ['鼓楼大街', '安华桥'], '什刹海': ['鼓楼大街', '南锣鼓巷'], '北宫门': ['安河桥北', '西苑'], '安河桥北': ['北宫门'], '西苑': ['北宫门', '圆明园'], '圆明园': ['西苑', '北京大学东门'], '北京大学东门': ['圆明园', '中关村'], '中关村': ['北京大学东门', '海淀黄庄'], '海淀黄庄': ['中关村', '人民大学', '苏州街', '知春里'], '人民大学': ['海淀黄庄', '魏公村'], '苏州街': ['海淀黄庄', '巴沟'], '知春里': ['海淀黄庄', '知春路'], '魏公村': ['人民大学', '国家图书馆'], '国家图书馆': ['魏公村', '动物园', '白石桥南'], '白石桥南': ['国家图书馆', '花园桥', '车公庄西', '白堆子'], '西四': ['平安里', '灵境胡同'], '北海北': ['平安里', '南锣鼓巷'], '陶然亭': ['菜市口', '北京南站'], '广安门内': ['菜市口', '达官营'], '虎坊桥': ['菜市口', '珠市口'], '北京南站': ['陶然亭', '马家堡', '陶然桥'], '马家堡': ['北京南站', '角门西'], '陶然桥': ['北京南站', '永定门外'], '角门西': ['马家堡', '公益西桥', '角门东', '草桥'], '公益西桥': ['角门西', '新宫'], '角门东': ['角门西', '大红门'], '草桥': ['角门西', '纪家庙'], '新宫': ['公益西桥', '西红门'], '天通苑': ['天通苑北', '天通苑北', '天通苑南', '南立水桥'], '天通苑北': ['天通苑'], '北': ['天通苑', '良乡大学城'], '南': ['天通苑', '立水桥', '次渠'], '南立水桥': ['天通苑'], '天通苑南': ['天通苑', '立水桥'], '立水桥': ['天通苑南', '立水桥南', '南北苑路北', '霍营', '北苑'], '南北苑路北': ['立水桥'], '霍营': ['立水桥', '回龙观东大街', '育新', '回龙观'], '北苑': ['立水桥', '立水桥南路北', '路北大屯路东', '望京西', '八里桥通州', '通州果园'], '立水桥南': ['立水桥', '北苑路北'], '北苑路北': ['立水桥南', '大屯路东'], '大屯路东': ['北苑路北', '惠新西街北口', '安立路', '关庄'], '惠新西街北口': ['大屯路东', '惠新西街南口'], '安立路': ['大屯路东', '奥林匹克公园'], '关庄': ['大屯路东', '望京西'], '惠新西街南口': ['惠新西街北口', '和平西桥', '安贞门', '芍药居'], '和平西桥': ['惠新西街南口', '和平里北街'], '安贞门': ['惠新西街南口', '北土城'], '芍药居': ['惠新西街南口', '太阳宫', '望京西', '光熙门'], '张自忠路': ['北新桥', '东四'], '朝阳门十条': ['东四'], '十条东直门': ['东四'], '南锣鼓巷': ['东四', '北海北', '什刹海'], '天坛东门': ['磁器口', '蒲黄榆'], '桥湾': ['磁器口', '珠市口'], '广渠门内': ['磁器口', '广渠门外'], '蒲黄榆': ['天坛东门', '刘家窑', '景泰', '方庄'], '刘家窑': ['蒲黄榆', '宋家庄'], '景泰': ['蒲黄榆', '永定门外'], '方庄': ['蒲黄榆', '十里河'], '宋家庄': ['刘家窑', '成寿寺', '石榴庄', '肖村'], '成寿寺': ['宋家庄', '分钟寺'], '石榴庄': ['宋家庄', '大红门'], '肖村': ['宋家庄', '小红门'], '慈寿寺': ['海淀五路居', '花园桥', '西钓鱼台', '车道沟'], '海淀五路居': ['慈寿寺'], '花园桥': ['慈寿寺', '白石桥南'], '车道沟': ['慈寿寺', '长春桥'], '车公庄西': ['白石桥南', '车公庄'], '呼家楼': ['东大桥', '金台路', '团结湖', '金台夕照'], '金台路': ['呼家楼', '十里堡', '红庙', '朝阳公园'], '团结湖': ['呼家楼', '农业展览馆'], '十里堡': ['金台路', '青年路'], '朝阳公园': ['金台路', '枣营'], '青年路': ['十里堡', '褡裢坡'], '褡裢坡': ['青年路', '黄渠'], '黄渠': ['褡裢坡', '常营'], '常营': ['黄渠', '草房'], '草房': ['常营', '物资学院路'], '物资学院路': ['草房', '通州北关'], '通州北关': ['物资学院路', '通运门'], '通运门': ['通州北关', '北运河西'], '北运河西': ['通运门', '北运河东'], '北运河东': ['北运河西', '郝家府'], '郝家府': ['北运河东', '东夏园'], '东夏园': ['郝家府', '潞城'], '潞城': ['东夏园'], '湾子': ['北京西站', '达官营'], '六里桥东': ['北京西站', '六里桥'], '达官营': ['湾子', '广安门内'], '珠市口': ['虎坊桥', '桥湾'], '广渠门外': ['广渠门内', '双井'], '劲松': ['双井', '潘家园'], '大郊亭': ['九龙山', '百子湾'], '平乐园': ['九龙山', '北工大西门'], '百子湾': ['大郊亭', '化工'], '化工': ['百子湾', '南楼梓庄'], '南楼梓庄': ['化工', '欢乐谷景区'], '欢乐谷景区': ['南楼梓庄', '垡头'], '垡头': ['欢乐谷景区', '双合'], '双合': ['垡头', '焦化厂'], '焦化厂': ['双合'], '育知路': ['朱辛庄', '平西府'], '朱辛庄': ['育知路', '巩华城', '生命科学园'], '巩华城': ['朱辛庄', '沙河'], '生命科学园': ['朱辛庄', '西二旗'], '平西府': ['育知路', '回龙观东大街'], '回龙观东大街': ['平西府', '霍营'], '育新': ['霍营', '西小口'], '回龙观': ['霍营', '龙泽', '平西府东大街', '东大街霍营'], '西小口': ['育新', '永泰庄'], '永泰庄': ['西小口', '林萃桥'], '林萃桥': ['永泰庄', '森林公园南门'], '森林公园南门': ['林萃桥', '奥林匹克公园'], '奥林匹克公园': ['森林公园南门', '奥体中心', '北沙滩', '安立路'], '奥体中心': ['奥林匹克公园', '北土城'], '北沙滩': ['奥林匹克公园', '六道口'], '北土城': ['奥体中心', '安华桥', '健德门', '安贞门'], '安华桥': ['北土城', '安德里北街'], '健德门': ['北土城', '牡丹园'], '六里桥': ['六里桥东', '北京西站东', '六里桥东', '七里庄', '西局', '莲花桥'], '北京西站东': ['六里桥'], '七里庄': ['六里桥', '丰台东大街', '大井', '西局'], '西局': ['六里桥', '七里庄', '泥洼'], '丰台东大街': ['七里庄', '丰台南路'], '大井': ['七里庄', '郭庄子'], '丰台南路': ['丰台东大街', '科怡路'], '科怡路': ['丰台南路', '丰台科技园'], '丰台科技园': ['科怡路', '郭公庄'], '郭公庄': ['丰台科技园', '大葆台'], '大葆台': ['郭公庄', '稻田'], '巴沟': ['苏州街', '火器营'], '火器营': ['巴沟', '长春桥'], '知春路': ['知春里', '西土城', '大钟寺', '五道口'], '西土城': ['知春路', '牡丹园'], '五道口': ['知春路', '上地'], '牡丹园': ['西土城', '健德门'], '太阳宫': ['芍药居', '三元桥'], '望京西': ['芍药居', '北苑', '关庄', '望京'], '光熙门': ['芍药居', '柳芳'], '亮马桥': ['三元桥', '农业展览馆'], 'T3航站楼': ['三元桥', 'T2航站楼'], 'T2航站楼': ['三元桥', 'T3航站楼'], '农业展览馆': ['亮马桥', '团结湖'], '潘家园': ['劲松', '十里河'], '十里河': ['潘家园', '分钟寺', '方庄', '南八里庄'], '分钟寺': ['十里河', '成寿寺'], '南八里庄': ['十里河', '北工大西门'], '大红门': ['石榴庄', '角门东'], '纪家庙': ['草桥', '首经贸'], '首经贸': ['纪家庙', '丰台站'], '丰台站': ['首经贸', '泥洼'], '泥洼': ['丰台站', '西局'], '长春桥': ['车道沟', '火器营'], '上地': ['五道口', '西二旗'], '西二旗': ['上地', '龙泽', '生命科学园'], '龙泽': ['西二旗', '回龙观'], '平西府东大街': ['回龙观'], '东大街霍营': ['回龙观'], '立水桥南路北': ['北苑'], '路北大屯路东': ['北苑'], '八里桥通州': ['北苑'], '通州果园': ['北苑'], '望京': ['望京西', '阜通', '北苑西', '西芍药居', '高家园南', '南阜通', '东湖渠', '关庄西', '望京西', '望京东', '东崔各庄'], '园博园': ['张郭庄', '大瓦窑'], '张郭庄': ['园博园'], '大瓦窑': ['园博园', '郭庄子'], '郭庄子': ['大瓦窑', '大井'], '永定门外': ['陶然桥', '景泰'], '北工大西门': ['南八里庄', '平乐园'], '枣营': ['朝阳公园', '东风北桥'], '东风北桥': ['枣营', '将台'], '将台': ['东风北桥', '高家园'], '高家园': ['将台', '望京南'], '望京南': ['高家园', '阜通'], '阜通': ['望京南', '望京'], '北苑西': ['望京'], '西芍药居': ['望京'], '高家园南': ['望京'], '南阜通': ['望京'], '东湖渠': ['望京', '来广营'], '关庄西': ['望京'], '东崔各庄': ['望京'], '来广营': ['东湖渠', '善各庄'], '善各庄': ['来广营'], '六道口': ['清华东路西口', '北沙滩'], '清华东路西口': ['六道口'], '望京东': ['望京', '崔各庄'], '崔各庄': ['望京东', '马泉营'], '马泉营': ['崔各庄', '孙河'], '孙河': ['马泉营', '国展'], '国展': ['孙河', '花梨坎'], '花梨坎': ['国展', '后沙峪'], '后沙峪': ['花梨坎', '南法信'], '南法信': ['后沙峪', '石门'], '石门': ['南法信', '顺义'], '顺义': ['石门', '俸伯'], '俸伯': ['顺义'], '传媒大学': ['高碑店', '双桥'], '双桥': ['传媒大学', '管庄'], '管庄': ['双桥', '八里桥'], '八里桥': ['管庄', '通州北苑'], '通州北苑': ['八里桥', '果园'], '果园': ['通州北苑', '苹古城', '九棵树'], '苹古城': ['果园'], '九棵树': ['果园', '梨园'], '梨园': ['九棵树', '临河里'], '临河里': ['梨园', '土桥'], '土桥': ['临河里'], '十三陵景区': ['昌平西山口', '昌平'], '昌平西山口': ['十三陵景区'], '昌平': ['十三陵景区', '西山口十三陵景区', '东关', '东关北邵洼', '昌平东关'], '西山口十三陵景区': ['昌平'], '东关': ['昌平'], '东关北邵洼': ['昌平'], '昌平东关': ['昌平', '北邵洼'], '北邵洼': ['昌平东关', '南邵'], '南邵': ['北邵洼', '沙河高教园'], '沙河高教园': ['南邵', '沙河'], '沙河': ['沙河高教园', '南邵高教园', '高教园', '巩华城'], '南邵高教园': ['沙河'], '高教园': ['沙河'], '小红门': ['肖村', '旧宫'], '旧宫': ['小红门', '亦庄桥'], '亦庄桥': ['旧宫', '亦庄文化园'], '亦庄文化园': ['亦庄桥', '万源街'], '万源街': ['亦庄文化园', '荣京东街'], '荣京东街': ['万源街', '荣昌东街'], '荣昌东街': ['荣京东街', '同济南路'], '同济南路': ['荣昌东街', '经海路'], '经海路': ['同济南路', '次渠南'], '次渠南': ['经海路', '次渠'], '次渠': ['次渠南', '经海路南', '次渠南'], '经海路南': ['次渠'], '西红门': ['新宫', '高米店北'], '高米店北': ['西红门', '高米店南'], '高米店南': ['高米店北', '枣园'], '枣园': ['高米店南', '清源路'], '清源路': ['枣园', '黄村西大街'], '黄村西大街': ['清源路', '黄村火车站'], '黄村火车站': ['黄村西大街', '义和庄'], '义和庄': ['黄村火车站', '生物医药基地'], '生物医药基地': ['义和庄', '天宫院'], '天宫院': ['生物医药基地'], '稻田': ['大葆台', '长阳'], '长阳': ['稻田', '篱笆房'], '篱笆房': ['长阳', '广阳城'], '广阳城': ['篱笆房', '良乡大学城北'], '良乡大学城北': ['广阳城', '良乡大学城'], '良乡大学城': ['良乡大学城北', '广阳城北', '良乡大学城北', '良乡大学城西', '西良乡南关'], '广阳城北': ['良乡大学城'], '西良乡南关': ['良乡大学城'], '良乡大学城西': ['良乡大学城', '良乡南关'], '良乡南关': ['良乡大学城西', '苏庄'], '苏庄': ['良乡南关']}

def transfer_stations_first(pathes):
    return sorted(pathes, key=len)

def transfer_as_much_possible(pathes):
    return sorted(pathes, key=len, reverse=True)

def shortest_path_first(pathes):
    if len(pathes) <= 1: return pathes

    def get_path_distnace(path):
        distance = 0
        for i in range(len(path) - 1):
            station_interval_name1 = path[i] + '――' + path[i + 1]
            station_interval_name2 = path[i] + '——' + path[i + 1]
            if stationDistance.get(station_interval_name1).__bool__():
                distance += stationDistance[station_interval_name1]
            if stationDistance.get(station_interval_name2).__bool__():
                distance += stationDistance[station_interval_name2]
        return distance
    return sorted(pathes, key=get_path_distnace)


# 深度优先
def search(start, destination, connection_grpah, sort_candidate):
    pathes = [[start]]
    visitied = set()

    while pathes:  # if we find existing pathes
        path = pathes.pop(0)
        froninter = path[-1]
        if froninter in visitied: continue
        successors = connection_grpah[froninter]

        for city in successors:
            if city in path: continue  # eliminate loop
            # depth first
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination: return new_path

        visitied.add(froninter)
        pathes = sort_candidate(pathes)  # 我们可以加一个排序函数 对我们的搜索策略进行控制


def pretty_print(cities):
    print('->'.join(cities))

# print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&-----RESULT-----&&&&&&&&&&&&&&&&&&&&&&')
# 尽量多的站
# pretty_print(search('苹果园', '芍药居', city_connection, sort_candidate=transfer_as_much_possible))
# 尽量少的站
# pretty_print(search('苹果园', '芍药居', city_connection, sort_candidate=transfer_stations_first))
# 距离最短
pretty_print(search('苹果园', '芍药居', city_connection, sort_candidate=shortest_path_first))