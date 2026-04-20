# =========================
# 公共定义
# =========================

# ---------- 自定义环境声通道 ----------
init python:
    renpy.music.register_channel("rain", mixer="sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("wind", mixer="sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("hum", mixer="sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("motion", mixer="sfx", loop=True, stop_on_mute=True)

# ---------- 角色定义 ----------
define y = Character("八云晓", color="#c8ffc8")
define n = Character(None)

# Pro-01-2 会用到的角色
define colleague_a = Character("同事A", color="#c8e6ff")
define colleague_b = Character("同事B", color="#c8e6ff")
define senior = Character("老前辈", color="#ffe0a8")
define desk_voice = Character("值班台", color="#ffd6f5")

# ---------- 过渡 ----------
define flash = Fade(0.08, 0.0, 0.12, color="#ffffff")