# =========================
# Pro-01-1 正式版脚本（环境声修正版）
# 基于 demo.docx 舞台化改编稿 v2
# =========================

# ---------- 自定义环境声通道 ----------
init python:
    renpy.music.register_channel("rain", mixer="sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("wind", mixer="sfx", loop=True, stop_on_mute=True)

# ---------- 角色定义 ----------
define y = Character("八云晓", color="#c8ffc8")
define n = Character(None)

# ---------- 过渡 ----------
define flash = Fade(0.08, 0.0, 0.12, color="#ffffff")

# ---------- 图片资源 ----------
image BG_P01_01 = "images/BG_P01_01_MountainPath_NightRain.png"
image BG_P01_02 = "images/BG_P01_02_MountainPath_UpperFog.png"
image BG_P01_03 = "images/BG_P01_03_HalfwayPavilion_Rain.png"

image CG_P01_01 = "images/CG_P01_01_InjuredYoungMan_OnSlope.png"

# ---------- FX资源（按demo清单预留） ----------
image FX_P01_FlashlightMask_01 = "images/FX_P01_FlashlightMask_01.png"
image FX_P01_FlashlightMask_02 = "images/FX_P01_FlashlightMask_02.png"

label start:

    # =========================
    # 舞台一：雨夜巡山
    # =========================

    scene BG_P01_01
    with fade

    play rain "audio/SE_P01_Rain_FineLoop.ogg"
    play wind "audio/SE_P01_Wind_ForestLight.ogg"

    n "雨下得人心烦。"
    n "不是那种痛快的大雨。"
    n "赤子山的雨，总是细细密密地挂在风里。顺着帽檐往下坠，打在睫毛上，又凉又黏。"
    n "手电打出去，光一碰到水汽就发白。照不了几米，前面就只剩一团散开的雾。"

    n "我把雨衣帽檐往下压了压，低头看了一眼脚边。"
    n "最边上那块石阶，果然又积了水。"

    y "……啧。"

    play sound "audio/SE_P01_WoodStep_Wet.ogg"
    n "我拿靴尖试了试着力点，从旁边绕过去。"
    n "雨水顺着木栈道往下淌。踩上去，声音闷得像陷进一层湿布里。"
    n "风从林子里钻出来，带着一股湿木头和腐叶沤在一起的味道。"

    play sound "audio/SE_P01_Radio_StaticShort.ogg"
    n "对讲机又抽风了。"

    y "喂……喂？"

    pause 0.2

    n "没反应。"
    n "这种天气最烦。"
    n "信号时有时无。上面写报告倒是轻巧，一句“夜间巡查照常进行”就能交代过去。"
    n "至于山路滑不滑，护栏顶不顶用，游客会不会脑子一热翻围栏拍雾景——"
    n "那都得算在我们头上。"

    n "我拍了两下，还是没声，只好先塞回腰侧。"
    n "今天轮我值后半夜。"
    n "景区傍晚因为天气预警封了几段山道。照规矩，封完还得再巡一遍：看有没有滞留的人，看警示灯和护栏有没有问题，顺便把那些喜欢拿自己命开玩笑的游客捞回来。"
    n "这种事每年都有人干。"
    n "出了事，还得我们去找。"

    scene BG_P01_02
    with dissolve

    n "我顺着山道往上走。"
    n "雨不算大，雾却比平时厚得多。"
    n "手电扫过去，路边警示牌只剩一团模糊的白影，连上面的红字都看不清。"
    n "再往前转一道弯，就是半山亭。"
    n "再往上，还有一片游客住的山庄区。平时这个点灯都该灭了，今天也黑着。"
    n "白天这里人最多。天气好的时候，游客能挤成一排拍照。"
    n "可一到这种天，它就只剩个黑影。四面漏风，孤零零杵在山路边上。"

    y "这鬼天气……"

    # =========================
    # 舞台二：半山亭前 / 发现异常
    # =========================

    scene BG_P01_03
    with dissolve

    # 雨和风继续保持
    play sound "audio/SE_P01_Pavilion_WindChimeWood.ogg"

    n "我把手电往前送了送。"
    n "光柱先照到亭檐。"
    n "再落到石阶。"

    pause 0.5

    n "然后，我停住了。"

    pause 0.5

    n "那地方本来不该有东西。"
    n "一开始，我还以为是游客落下的包，或者被风吹倒的牌子。"
    n "可那团黑影歪在亭外不远的缓坡边，轮廓不对。"
    n "长长一条，被雨压在地上。"

    pause 0.4

    n "我心里一沉。"
    n "手电光定住。"

    pause 0.3

    n "那是个人。"

    y "……该死。"

    play sound "audio/SE_P01_RunOnWetWood.ogg"
    n "我直接冲了过去。"
    n "木地板湿得发滑，我差点踩空，扶了一把亭柱才稳住，翻过护栏往坡下跳。"

    scene CG_P01_01
    with flash

    play sound "audio/SE_P01_ClothMove_Close.ogg"

    n "靠近以后，才看清。"
    n "男的，很年轻，最多二十出头。"
    n "人侧着倒在坡边，一条腿卡在灌木里。衣服被树枝刮破了几处，浑身都是泥水。"
    n "左边额角和脸侧有擦伤。血早让雨冲淡了，只剩下一条发暗的痕。"
    n "要不是这截灌木挡了一下，他大概已经滚下去了。"

    y "喂。"
    y "听得见吗？"

    pause 0.5

    n "没反应。"
    n "雨点打在他脸上，睫毛一动不动。"
    n "我伸手去探他颈侧。"
    n "指尖刚碰到皮肤，我心里才稍微松了一点。"
    n "还有脉。"
    n "弱得吓人，但还在。"

    y "行，还给我留了口气。"

    n "我先看了看他后脑和肩颈有没有明显伤口。"
    n "人冷得厉害，衣服湿透了贴在身上，跟从冰水里捞出来差不多。"
    n "我不敢乱挪，只能俯身贴近些，看他胸口还有没有起伏。"
    n "有。"
    n "很浅。"

    y "听得见我说话吗？"
    y "别在这儿睡，先撑着。"

    n "他的眉心，很轻地动了一下。"
    n "我刚要再叫，他忽然吸了一口很短的气，喉咙里挤出一点破碎的声音。"

    y "什么？"

    n "我立刻凑近。"

    y "你说什么？"

    n "他的嘴唇动了动。"
    n "声音轻得几乎听不见。"
    n "我没听清。"

    y "再说一遍——"

    pause 0.5

    n "可他只微微张了张口，再没出第二个音节。"
    n "雨声太大了。"

    play sound "audio/SE_P01_PhoneCall_WeakSignal.ogg"
    n "我没再耽误，掏出手机拨急救电话。"
    n "信号只剩一格，屏幕还在闪。"
    n "我一边报位置，一边用肩膀顶住手电，让光别乱晃。"

    y "赤子山东侧半山亭下方缓坡。"
    y "男性，二十岁左右，意识模糊，疑似坠落伤，生命体征还在……"
    y "对，现在雨大，路滑，你们从巡山道绕上来。"

    play sound "audio/SE_P01_Radio_Static_Long.ogg"
    n "挂断以后，我又拿对讲机去敲值班室。"

    y "值班室，听到回话。"
    y "半山亭这边有伤者。带急救包和担架上山。"
    y "入口那边先别再放人进来。"

    n "说完这些，我才重新低头看他。"
    n "脸白得一点血色都没有。睫毛被雨压湿，紧紧贴在皮肤上。"
    n "整个人安静得过头，像是只剩一口气勉强吊着。"

    play sound "audio/SE_P01_FarFootsteps_Approach.ogg"
    n "远处很快传来脚步声。"
    n "灯光也晃了上来。"

    y "这边！"

    stop rain fadeout 1.0
    stop wind fadeout 1.0

    return