# =========================
# Pro-01-2
# 抬人下山 / 值班室记录 / 得知姓名
# 基于 demo2.docx 舞台化改编稿 v2（最终呈现版标准）
# =========================

label p01_02:

    # =========================
    # 舞台一：同事赶到 / 现场转运
    # 地点：半山亭外 / 缓坡边
    # =========================

    scene BG_P01_04
    with dissolve

    play rain "audio/SE_P01_Rain_FineLoop.ogg"
    play wind "audio/SE_P01_Wind_ForestLight.ogg"
    play motion "audio/SE_P01_Footsteps_GroupApproach.ogg"

    colleague_a "看见了——"
    colleague_b "担架放哪？"
    senior "先别急着抬，看看颈部。"

    n "两个同事气喘吁吁跑过来，一个拎着急救包，一个抱着折叠担架，后面还跟着夜值的老前辈。"
    n "老头一看地上的人，眉头立刻拧起来。"

    senior "怎么摔成这样？"

    y "像是从上面滚下来的。"
    y "先别问了，固定颈部。"

    stop motion fadeout 0.2
    play sound "audio/SE_P01_Medkit_Open.ogg"

    n "几个人很快忙起来。"
    n "撑伞的撑伞，打灯的打灯，拆夹板的拆夹板。"

    play sound "audio/SE_P01_Rain_OnUmbrella.ogg"
    n "雨打在伞骨上，噼里啪啦一片。"

    senior "头别晃。"
    colleague_a "这边托一下。"
    colleague_b "腿卡住了，先把树枝拨开。"

    y "我来。"

    play sound "audio/SE_P01_Branches_Move.ogg"
    play sound "audio/SE_P01_ClothMove_WetClose.ogg"

    n "他一直没再睁眼。"
    n "脸上的水顺着鬓角往下淌，也不知道哪些是雨，哪些是冷汗。"
    n "我们合力把人抬上担架。"
    n "他在保温毯里很轻地抖了一下。"
    n "也不知道是冷，还是疼，或者只是在梦里挣扎。"

    play sound "audio/SE_P01_Stretcher_Lift.ogg"

    y "走，慢点。"
    y "下坡滑，别再给他摔第二次。"

    # =========================
    # 舞台二：雾雨中抬担架下山
    # 地点：下山栈道
    # =========================

    scene CG_P01_02
    with dissolve

    show FX_P01_RainOverlay_HeavyMist

    play motion "audio/SE_P01_GroupCarry_WetSteps.ogg"
    play wind "audio/SE_P01_Wind_ForestCold.ogg"

    n "担架被抬起来，灯光和脚步声一起往下挪。"
    n "半山亭很快退到身后，又被雾吞进去。"
    n "我走在旁边，替他们照着脚下。"
    n "雨还在下。"
    n "山风从林子里穿出来，吹得亭檐下挂着的木牌轻轻碰撞。"

    play sound "audio/SE_P01_WoodTag_ClinkFar.ogg"

    n "那声音碎得像玻璃渣。"
    n "我低头看了一眼担架上的人。"
    n "人还是没醒。"
    n "睫毛湿得一缕一缕地贴在皮肤上，脸白得几乎没了活气。"

    y "撑着点。"

    n "不知道他听没听见。"

    hide FX_P01_RainOverlay_HeavyMist
    stop motion fadeout 0.5

    # =========================
    # 舞台三：回到值班室 / 冷下来
    # 地点：景区值班室
    # =========================

    scene BG_P01_06
    with fade

    stop wind fadeout 0.5
    play rain "audio/SE_P01_Rain_MuffledOutside.ogg"
    play hum "audio/SE_P01_ComputerHum_Low.ogg"

    play sound "audio/SE_P01_Door_OpenClose_Office.ogg"

    n "等把人送下山，再回值班室，外头那股湿冷才后知后觉地一起找上来。"
    n "鞋里全是水，裤脚贴着小腿，凉得发僵。"
    n "右手虎口大概是刚才扶亭柱的时候蹭破了。平时不算什么，这会儿给雨一泡，开始隐隐发疼。"
    n "值班室不大。"
    n "门一推开，里面那股电器余热、旧纸张和速溶咖啡混在一起的味道就扑过来。"
    n "暖气不算足，但比外头强多了。"

    play sound "audio/SE_P01_Flashlight_OnDesk.ogg"

    n "我把门带上，摘了帽子。"
    n "雨水顺着发梢往下滴，很快就在地上砸出一小滩。"
    n "手电搁到桌上时滚了半圈，被我一把按住。"
    n "桌角堆着巡查记录本，电脑屏幕亮得刺眼。"

    senior "人送上车了。"

    y "嗯。"

    senior "命挺大。"

    n "活着送上车，和最后能不能活下来，本来就是两码事。"
    n "山里这种摔伤，最怕一开始还有气，后面内伤或者脑子出问题，抢都抢不回来。"
    n "现在说命大，还早。"

    play sound "audio/SE_P01_WaterPour_Hot.ogg"
    play sound "audio/SE_P01_PaperCup_SetDown.ogg"

    senior "先喝两口，脸都白了。"

    y "谢了。"

    n "热水一烫到掌心，我整个人才像慢慢活回来一点。"
    n "一口热水压下去，胸口那点发闷才散开。"

    senior "报告别忘了补。"
    senior "这种事最烦，但是也别忘。"

    y "确实。"

    # =========================
    # 舞台四：事故记录 / 名字落下
    # 地点：值班室 / 走廊
    # =========================

    scene BG_P01_07
    with dissolve

    play motion "audio/SE_P01_Keyboard_TypingLow.ogg"

    n "我把纸杯放到一边，坐下开电脑。"
    n "事故记录模板一跳出来，白底黑字，一格一格排得死板，光看着就烦。"
    n "时间。地点。发现过程。伤者状态。初步判断。"
    n "我盯着屏幕看了两秒，抬手抹了把脸，开始打字。"
    n "这种东西最磨人。"
    n "真出事的时候，人是连滚带爬往前冲；回过头写报告，却得把每一分钟都拆开摆平。"
    n "什么时候发现异常，第一眼看见什么，怎么确认生命体征，什么时候联系急救，什么时候通知值班室，什么时候转运。"
    n "漏一点都不行。"

    play sound "audio/SE_P01_Kettle_BoilLight.ogg"
    play sound "audio/SE_P01_Drops_OnFloor_Clothes.ogg"

    n "屋里很安静。"
    n "只剩键盘声、热水壶偶尔咕噜一响，还有我衣服往下滴水的声音。"
    n "窗玻璃让夜里的潮气糊住了，外头灰蒙蒙一片，什么也看不清。"
    n "写到“伤者身份”那一栏时，我停了一下。"
    n "刚发现人的时候哪有空问这个，身上也没来得及细翻，只能先写“待确认”。"
    n "顺手把“性别：男”“年龄：约二十岁”填进去。"

    stop motion fadeout 0.2
    play sound "audio/SE_P01_DeskPhone_Ring.ogg"

    n "刚敲完最后一个字，桌上的内线电话就响了。"

    play sound "audio/SE_P01_Phone_PickupHangup.ogg"

    y "喂？"

    desk_voice "晓哥，医院回登记信息了。"

    y "嗯，你说。"

    n "我把电话夹在肩上，一边听，一边往下记。"
    n "信息不多，很快就写完了。"

    y "还有别的吗？"

    desk_voice "暂时没有。医院那边说，后续情况等天亮再同步。"

    y "行，知道了。"

    play sound "audio/SE_P01_Phone_PickupHangup.ogg"

    pause 0.5

    n "电话挂断以后，我盯着刚写下来的名字看了两秒。"

    n "黑泽优。"

    senior "有名字了？"

    y "嗯。"

    senior "叫什么？"

    y "黑泽优。"

    senior "学生吗？"
    senior "大半夜跑那地方，也不知道图什么。"

    n "我没说话。"
    n "只把最后几行补完，按下保存。"

    play sound "audio/SE_P01_Computer_SaveBeep.ogg"

    n "电脑发出一声轻响，惨白的页面停在那里。"
    n "报告算是交代完了。"
    n "可今晚这事，好像也没真结束。只是被暂时塞进了表格里，压进了系统。"
    n "我靠在椅背上，闭了闭眼。"
    n "肩膀这时候才开始发沉。"
    n "值夜班本来就烦，再碰上这种事，剩下这半宿算是别想消停了。"

    senior "回去歇会儿吧。"
    senior "真有新消息，明早再看。"

    y "嗯。"

    play sound "audio/SE_P01_Cabinet_OpenClose.ogg"

    n "我站起来去翻柜子里的备用外套。"
    n "临走前，又回头看了一眼屏幕上那个名字。"
    n "希望这小子命硬点。"
    n "我心里这么想着，抬手关了屏幕，推门走了出去。"

    play sound "audio/SE_P01_Screen_OffSoft.ogg"
    play sound "audio/SE_P01_Door_OpenClose_Office.ogg"

    scene BG_P01_08
    with dissolve

    stop rain fadeout 0.5
    stop hum fadeout 0.5
    play hum "audio/SE_P01_Corridor_LightHum.ogg"

    n "走廊里比屋里更冷，灯一盏一盏亮过去，照得人眼睛发酸。"
    n "再过几个小时，天该亮了。"

    stop hum fadeout 1.0

    return