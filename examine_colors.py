# %%
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

# %%
# Function to extract H, S, L from HSL string
def parse_hsl(hsl_str):
    hsl_match = re.match(r"hsl\(([\d.]+),([\d.]+)%,([\d.]+)%\)", hsl_str)
    if hsl_match:
        return tuple(map(float, hsl_match.groups()))
    return None, None, None

# %%
colors = {
    "slate": [
        {"scale": 50, "hsl": "hsl(210,40%,98%)"},
        {"scale": 100, "hsl": "hsl(210,40%,96.1%)"},
        {"scale": 200, "hsl": "hsl(214.3,31.8%,91.4%)"},
        {"scale": 300, "hsl": "hsl(212.7,26.8%,83.9%)"},
        {"scale": 400, "hsl": "hsl(215,20.2%,65.1%)"},
        {"scale": 500, "hsl": "hsl(215.4,16.3%,46.9%)"},
        {"scale": 600, "hsl": "hsl(215.3,19.3%,34.5%)"},
        {"scale": 700, "hsl": "hsl(215.3,25%,26.7%)"},
        {"scale": 800, "hsl": "hsl(217.2,32.6%,17.5%)"},
        {"scale": 900, "hsl": "hsl(222.2,47.4%,11.2%)"},
        {"scale": 950, "hsl": "hsl(222.2,84%,4.9%)"},
    ],
    "gray": [
        {"scale": 50, "hsl": "hsl(210,20%,98%)"},
        {"scale": 100, "hsl": "hsl(220,14.3%,95.9%)"},
        {"scale": 200, "hsl": "hsl(220,13%,91%)"},
        {"scale": 300, "hsl": "hsl(216,12.2%,83.9%)"},
        {"scale": 400, "hsl": "hsl(217.9,10.6%,64.9%)"},
        {"scale": 500, "hsl": "hsl(220,8.9%,46.1%)"},
        {"scale": 600, "hsl": "hsl(215,13.8%,34.1%)"},
        {"scale": 700, "hsl": "hsl(216.9,19.1%,26.7%)"},
        {"scale": 800, "hsl": "hsl(215,27.9%,16.9%)"},
        {"scale": 900, "hsl": "hsl(220.9,39.3%,11%)"},
        {"scale": 950, "hsl": "hsl(224,71.4%,4.1%)"},
    ],
    "zinc": [
        {"scale": 50, "hsl": "hsl(0,0%,98%)"},
        {"scale": 100, "hsl": "hsl(240,4.8%,95.9%)"},
        {"scale": 200, "hsl": "hsl(240,5.9%,90%)"},
        {"scale": 300, "hsl": "hsl(240,4.9%,83.9%)"},
        {"scale": 400, "hsl": "hsl(240,5%,64.9%)"},
        {"scale": 500, "hsl": "hsl(240,3.8%,46.1%)"},
        {"scale": 600, "hsl": "hsl(240,5.2%,33.9%)"},
        {"scale": 700, "hsl": "hsl(240,5.3%,26.1%)"},
        {"scale": 800, "hsl": "hsl(240,3.7%,15.9%)"},
        {"scale": 900, "hsl": "hsl(240,5.9%,10%)"},
        {"scale": 950, "hsl": "hsl(240,10%,3.9%)"},
    ],
    "neutral": [
        {"scale": 50, "hsl": "hsl(0,0%,98%)"},
        {"scale": 100, "hsl": "hsl(0,0%,96.1%)"},
        {"scale": 200, "hsl": "hsl(0,0%,89.8%)"},
        {"scale": 300, "hsl": "hsl(0,0%,83.1%)"},
        {"scale": 400, "hsl": "hsl(0,0%,63.9%)"},
        {"scale": 500, "hsl": "hsl(0,0%,45.1%)"},
        {"scale": 600, "hsl": "hsl(0,0%,32.2%)"},
        {"scale": 700, "hsl": "hsl(0,0%,25.1%)"},
        {"scale": 800, "hsl": "hsl(0,0%,14.9%)"},
        {"scale": 900, "hsl": "hsl(0,0%,9%)"},
        {"scale": 950, "hsl": "hsl(0,0%,3.9%)"},
    ],
    "stone": [
        {"scale": 50, "hsl": "hsl(60,9.1%,97.8%)"},
        {"scale": 100, "hsl": "hsl(60,4.8%,95.9%)"},
        {"scale": 200, "hsl": "hsl(20,5.9%,90%)"},
        {"scale": 300, "hsl": "hsl(24,5.7%,82.9%)"},
        {"scale": 400, "hsl": "hsl(24,5.4%,63.9%)"},
        {"scale": 500, "hsl": "hsl(25,5.3%,44.7%)"},
        {"scale": 600, "hsl": "hsl(33.3,5.5%,32.4%)"},
        {"scale": 700, "hsl": "hsl(30,6.3%,25.1%)"},
        {"scale": 800, "hsl": "hsl(12,6.5%,15.1%)"},
        {"scale": 900, "hsl": "hsl(24,9.8%,10%)"},
        {"scale": 950, "hsl": "hsl(20,14.3%,4.1%)"},
    ],
    "red": [
        {"scale": 50, "hsl": "hsl(0,85.7%,97.3%)"},
        {"scale": 100, "hsl": "hsl(0,93.3%,94.1%)"},
        {"scale": 200, "hsl": "hsl(0,96.3%,89.4%)"},
        {"scale": 300, "hsl": "hsl(0,93.5%,81.8%)"},
        {"scale": 400, "hsl": "hsl(0,90.6%,70.8%)"},
        {"scale": 500, "hsl": "hsl(0,84.2%,60.2%)"},
        {"scale": 600, "hsl": "hsl(0,72.2%,50.6%)"},
        {"scale": 700, "hsl": "hsl(0,73.7%,41.8%)"},
        {"scale": 800, "hsl": "hsl(0,70%,35.3%)"},
        {"scale": 900, "hsl": "hsl(0,62.8%,30.6%)"},
        {"scale": 950, "hsl": "hsl(0,74.7%,15.5%)"},
    ],
    "orange": [
        {"scale": 50, "hsl": "hsl(33.3,100%,96.5%)"},
        {"scale": 100, "hsl": "hsl(34.3,100%,91.8%)"},
        {"scale": 200, "hsl": "hsl(32.1,97.7%,83.1%)"},
        {"scale": 300, "hsl": "hsl(30.7,97.2%,72.4%)"},
        {"scale": 400, "hsl": "hsl(27,96%,61%)"},
        {"scale": 500, "hsl": "hsl(24.6,95%,53.1%)"},
        {"scale": 600, "hsl": "hsl(20.5,90.2%,48.2%)"},
        {"scale": 700, "hsl": "hsl(17.5,88.3%,40.4%)"},
        {"scale": 800, "hsl": "hsl(15,79.1%,33.7%)"},
        {"scale": 900, "hsl": "hsl(15.3,74.6%,27.8%)"},
        {"scale": 950, "hsl": "hsl(13,81.1%,14.5%)"},
    ],
    "amber": [
        {"scale": 50, "hsl": "hsl(48,100%,96.1%)"},
        {"scale": 100, "hsl": "hsl(48,96.5%,88.8%)"},
        {"scale": 200, "hsl": "hsl(48,96.6%,76.7%)"},
        {"scale": 300, "hsl": "hsl(45.9,96.7%,64.5%)"},
        {"scale": 400, "hsl": "hsl(43.3,96.4%,56.3%)"},
        {"scale": 500, "hsl": "hsl(37.7,92.1%,50.2%)"},
        {"scale": 600, "hsl": "hsl(32.1,94.6%,43.7%)"},
        {"scale": 700, "hsl": "hsl(26,90.5%,37.1%)"},
        {"scale": 800, "hsl": "hsl(22.7,82.5%,31.4%)"},
        {"scale": 900, "hsl": "hsl(21.7,77.8%,26.5%)"},
        {"scale": 950, "hsl": "hsl(20.9,91.7%,14.1%)"},
    ],
    "yellow": [
        {"scale": 50, "hsl": "hsl(54.5,91.7%,95.3%)"},
        {"scale": 100, "hsl": "hsl(54.9,96.7%,88%)"},
        {"scale": 200, "hsl": "hsl(52.8,98.3%,76.9%)"},
        {"scale": 300, "hsl": "hsl(50.4,97.8%,63.5%)"},
        {"scale": 400, "hsl": "hsl(47.9,95.8%,53.1%)"},
        {"scale": 500, "hsl": "hsl(45.4,93.4%,47.5%)"},
        {"scale": 600, "hsl": "hsl(40.6,96.1%,40.4%)"},
        {"scale": 700, "hsl": "hsl(35.5,91.7%,32.9%)"},
        {"scale": 800, "hsl": "hsl(31.8,81%,28.8%)"},
        {"scale": 900, "hsl": "hsl(28.4,72.5%,25.7%)"},
        {"scale": 950, "hsl": "hsl(26,83.3%,14.1%)"},
    ],
    "lime": [
        {"scale": 50, "hsl": "hsl(78.3,92%,95.1%)"},
        {"scale": 100, "hsl": "hsl(79.6,89.1%,89.2%)"},
        {"scale": 200, "hsl": "hsl(80.9,88.5%,79.6%)"},
        {"scale": 300, "hsl": "hsl(82,84.5%,67.1%)"},
        {"scale": 400, "hsl": "hsl(82.7,78%,55.5%)"},
        {"scale": 500, "hsl": "hsl(83.7,80.5%,44.3%)"},
        {"scale": 600, "hsl": "hsl(84.8,85.2%,34.5%)"},
        {"scale": 700, "hsl": "hsl(85.9,78.4%,27.3%)"},
        {"scale": 800, "hsl": "hsl(86.3,69%,22.7%)"},
        {"scale": 900, "hsl": "hsl(87.6,61.2%,20.2%)"},
        {"scale": 950, "hsl": "hsl(89.3,80.4%,10%)"},
    ],
    "green": [
        {"scale": 50, "hsl": "hsl(138.5,76.5%,96.7%)"},
        {"scale": 100, "hsl": "hsl(140.6,84.2%,92.5%)"},
        {"scale": 200, "hsl": "hsl(141,78.9%,85.1%)"},
        {"scale": 300, "hsl": "hsl(141.7,76.6%,73.1%)"},
        {"scale": 400, "hsl": "hsl(141.9,69.2%,58%)"},
        {"scale": 500, "hsl": "hsl(142.1,70.6%,45.3%)"},
        {"scale": 600, "hsl": "hsl(142.1,76.2%,36.3%)"},
        {"scale": 700, "hsl": "hsl(142.4,71.8%,29.2%)"},
        {"scale": 800, "hsl": "hsl(142.8,64.2%,24.1%)"},
        {"scale": 900, "hsl": "hsl(143.8,61.2%,20.2%)"},
        {"scale": 950, "hsl": "hsl(144.9,80.4%,10%)"},
    ],
    "emerald": [
        {"scale": 50, "hsl": "hsl(151.8,81%,95.9%)"},
        {"scale": 100, "hsl": "hsl(149.3,80.4%,90%)"},
        {"scale": 200, "hsl": "hsl(152.4,76%,80.4%)"},
        {"scale": 300, "hsl": "hsl(156.2,71.6%,66.9%)"},
        {"scale": 400, "hsl": "hsl(158.1,64.4%,51.6%)"},
        {"scale": 500, "hsl": "hsl(160.1,84.1%,39.4%)"},
        {"scale": 600, "hsl": "hsl(161.4,93.5%,30.4%)"},
        {"scale": 700, "hsl": "hsl(162.9,93.5%,24.3%)"},
        {"scale": 800, "hsl": "hsl(163.1,88.1%,19.8%)"},
        {"scale": 900, "hsl": "hsl(164.2,85.7%,16.5%)"},
        {"scale": 950, "hsl": "hsl(165.7,91.3%,9%)"},
    ],
    "teal": [
        {"scale": 50, "hsl": "hsl(166.2,76.5%,96.7%)"},
        {"scale": 100, "hsl": "hsl(167.2,85.5%,89.2%)"},
        {"scale": 200, "hsl": "hsl(168.4,83.8%,78.2%)"},
        {"scale": 300, "hsl": "hsl(170.6,76.9%,64.3%)"},
        {"scale": 400, "hsl": "hsl(172.5,66%,50.4%)"},
        {"scale": 500, "hsl": "hsl(173.4,80.4%,40%)"},
        {"scale": 600, "hsl": "hsl(174.7,83.9%,31.6%)"},
        {"scale": 700, "hsl": "hsl(175.3,77.4%,26.1%)"},
        {"scale": 800, "hsl": "hsl(176.1,69.4%,21.8%)"},
        {"scale": 900, "hsl": "hsl(175.9,60.8%,19%)"},
        {"scale": 950, "hsl": "hsl(178.6,84.3%,10%)"},
    ],
    "cyan": [
        {"scale": 50, "hsl": "hsl(183.2,100%,96.3%)"},
        {"scale": 100, "hsl": "hsl(185.1,95.9%,90.4%)"},
        {"scale": 200, "hsl": "hsl(186.2,93.5%,81.8%)"},
        {"scale": 300, "hsl": "hsl(187,92.4%,69%)"},
        {"scale": 400, "hsl": "hsl(187.9,85.7%,53.3%)"},
        {"scale": 500, "hsl": "hsl(188.7,94.5%,42.7%)"},
        {"scale": 600, "hsl": "hsl(191.6,91.4%,36.5%)"},
        {"scale": 700, "hsl": "hsl(192.9,82.3%,31%)"},
        {"scale": 800, "hsl": "hsl(194.4,69.6%,27.1%)"},
        {"scale": 900, "hsl": "hsl(196.4,63.6%,23.7%)"},
        {"scale": 950, "hsl": "hsl(197,78.9%,14.9%)"},
    ],
    "sky": [
        {"scale": 50, "hsl": "hsl(204,100%,97.1%)"},
        {"scale": 100, "hsl": "hsl(204,93.8%,93.7%)"},
        {"scale": 200, "hsl": "hsl(200.6,94.4%,86.1%)"},
        {"scale": 300, "hsl": "hsl(199.4,95.5%,73.9%)"},
        {"scale": 400, "hsl": "hsl(198.4,93.2%,59.6%)"},
        {"scale": 500, "hsl": "hsl(198.6,88.7%,48.4%)"},
        {"scale": 600, "hsl": "hsl(200.4,98%,39.4%)"},
        {"scale": 700, "hsl": "hsl(201.3,96.3%,32.2%)"},
        {"scale": 800, "hsl": "hsl(201,90%,27.5%)"},
        {"scale": 900, "hsl": "hsl(202,80.3%,23.9%)"},
        {"scale": 950, "hsl": "hsl(204,80.2%,15.9%)"},
    ],
    "blue": [
        {"scale": 50, "hsl": "hsl(213.8,100%,96.9%)"},
        {"scale": 100, "hsl": "hsl(214.3,94.6%,92.7%)"},
        {"scale": 200, "hsl": "hsl(213.3,96.9%,87.3%)"},
        {"scale": 300, "hsl": "hsl(211.7,96.4%,78.4%)"},
        {"scale": 400, "hsl": "hsl(213.1,93.9%,67.8%)"},
        {"scale": 500, "hsl": "hsl(217.2,91.2%,59.8%)"},
        {"scale": 600, "hsl": "hsl(221.2,83.2%,53.3%)"},
        {"scale": 700, "hsl": "hsl(224.3,76.3%,48%)"},
        {"scale": 800, "hsl": "hsl(225.9,70.7%,40.2%)"},
        {"scale": 900, "hsl": "hsl(224.4,64.3%,32.9%)"},
        {"scale": 950, "hsl": "hsl(226.2,57%,21%)"},
    ],
    "indigo": [
        {"scale": 50, "hsl": "hsl(225.9,100%,96.7%)"},
        {"scale": 100, "hsl": "hsl(226.5,100%,93.9%)"},
        {"scale": 200, "hsl": "hsl(228,96.5%,88.8%)"},
        {"scale": 300, "hsl": "hsl(229.7,93.5%,81.8%)"},
        {"scale": 400, "hsl": "hsl(234.5,89.5%,73.9%)"},
        {"scale": 500, "hsl": "hsl(238.7,83.5%,66.7%)"},
        {"scale": 600, "hsl": "hsl(243.4,75.4%,58.6%)"},
        {"scale": 700, "hsl": "hsl(244.5,57.9%,50.6%)"},
        {"scale": 800, "hsl": "hsl(243.7,54.5%,41.4%)"},
        {"scale": 900, "hsl": "hsl(242.2,47.4%,34.3%)"},
        {"scale": 950, "hsl": "hsl(243.8,47.1%,20%)"},
    ],
    "violet": [
        {"scale": 50, "hsl": "hsl(250,100%,97.6%)"},
        {"scale": 100, "hsl": "hsl(251.4,91.3%,95.5%)"},
        {"scale": 200, "hsl": "hsl(250.5,95.2%,91.8%)"},
        {"scale": 300, "hsl": "hsl(252.5,94.7%,85.1%)"},
        {"scale": 400, "hsl": "hsl(255.1,91.7%,76.3%)"},
        {"scale": 500, "hsl": "hsl(258.3,89.5%,66.3%)"},
        {"scale": 600, "hsl": "hsl(262.1,83.3%,57.8%)"},
        {"scale": 700, "hsl": "hsl(263.4,70%,50.4%)"},
        {"scale": 800, "hsl": "hsl(263.4,69.3%,42.2%)"},
        {"scale": 900, "hsl": "hsl(263.5,67.4%,34.9%)"},
        {"scale": 950, "hsl": "hsl(261.2,72.6%,22.9%)"},
    ],
    "purple": [
        {"scale": 50, "hsl": "hsl(270,100%,98%)"},
        {"scale": 100, "hsl": "hsl(268.7,100%,95.5%)"},
        {"scale": 200, "hsl": "hsl(268.6,100%,91.8%)"},
        {"scale": 300, "hsl": "hsl(269.2,97.4%,85.1%)"},
        {"scale": 400, "hsl": "hsl(270,95.2%,75.3%)"},
        {"scale": 500, "hsl": "hsl(270.7,91%,65.1%)"},
        {"scale": 600, "hsl": "hsl(271.5,81.3%,55.9%)"},
        {"scale": 700, "hsl": "hsl(272.1,71.7%,47.1%)"},
        {"scale": 800, "hsl": "hsl(272.9,67.2%,39.4%)"},
        {"scale": 900, "hsl": "hsl(273.6,65.6%,32%)"},
        {"scale": 950, "hsl": "hsl(273.5,86.9%,21%)"},
    ],
    "fuchsia": [
        {"scale": 50, "hsl": "hsl(289.1,100%,97.8%)"},
        {"scale": 100, "hsl": "hsl(287,100%,95.5%)"},
        {"scale": 200, "hsl": "hsl(288.3,95.8%,90.6%)"},
        {"scale": 300, "hsl": "hsl(291.1,93.1%,82.9%)"},
        {"scale": 400, "hsl": "hsl(292,91.4%,72.5%)"},
        {"scale": 500, "hsl": "hsl(292.2,84.1%,60.6%)"},
        {"scale": 600, "hsl": "hsl(293.4,69.5%,48.8%)"},
        {"scale": 700, "hsl": "hsl(294.7,72.4%,39.8%)"},
        {"scale": 800, "hsl": "hsl(295.4,70.2%,32.9%)"},
        {"scale": 900, "hsl": "hsl(296.7,63.6%,28%)"},
        {"scale": 950, "hsl": "hsl(296.8,90.2%,16.1%)"},
    ],
    "pink": [
        {"scale": 50, "hsl": "hsl(327.3,73.3%,97.1%)"},
        {"scale": 100, "hsl": "hsl(325.7,77.8%,94.7%)"},
        {"scale": 200, "hsl": "hsl(325.9,84.6%,89.8%)"},
        {"scale": 300, "hsl": "hsl(327.4,87.1%,81.8%)"},
        {"scale": 400, "hsl": "hsl(328.6,85.5%,70.2%)"},
        {"scale": 500, "hsl": "hsl(330.4,81.2%,60.4%)"},
        {"scale": 600, "hsl": "hsl(333.3,71.4%,50.6%)"},
        {"scale": 700, "hsl": "hsl(335.1,77.6%,42%)"},
        {"scale": 800, "hsl": "hsl(335.8,74.4%,35.3%)"},
        {"scale": 900, "hsl": "hsl(335.9,69%,30.4%)"},
        {"scale": 950, "hsl": "hsl(336.2,83.9%,17.1%)"},
    ],
    "rose": [
        {"scale": 50, "hsl": "hsl(355.7,100%,97.3%)"},
        {"scale": 100, "hsl": "hsl(355.6,100%,94.7%)"},
        {"scale": 200, "hsl": "hsl(352.7,96.1%,90%)"},
        {"scale": 300, "hsl": "hsl(352.6,95.7%,81.8%)"},
        {"scale": 400, "hsl": "hsl(351.3,94.5%,71.4%)"},
        {"scale": 500, "hsl": "hsl(349.7,89.2%,60.2%)"},
        {"scale": 600, "hsl": "hsl(346.8,77.2%,49.8%)"},
        {"scale": 700, "hsl": "hsl(345.3,82.7%,40.8%)"},
        {"scale": 800, "hsl": "hsl(343.4,79.7%,34.7%)"},
        {"scale": 900, "hsl": "hsl(341.5,75.5%,30.4%)"},
        {"scale": 950, "hsl": "hsl(343.1,87.7%,15.9%)"},
    ],
}

# %%
# Flatten and parse data
data = []
for color_name, values in colors.items():
    for entry in values:
        h, s, l = parse_hsl(entry["hsl"])
        data.append({
            "color": color_name,
            "scale": entry["scale"],
            "hue": h,
            "saturation": s,
            "lightness": l
        })
df = pd.DataFrame(data)

# %%
# Plotting H, S, L vs scale for each color as a separate line

def hsl_to_rgb(h, s, l):
    # Custom HSL (0-360, 0-100, 0-100) to RGB (0-1, 0-1, 0-1)
    h = h / 360
    s = s / 100
    l = l / 100
    def hue2rgb(p, q, t):
        if t < 0: t += 1
        if t > 1: t -= 1
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: return p + (q - p) * (2/3 - t) * 6
        return p
    if s == 0:
        r = g = b = l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1/3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1/3)
    return (r, g, b)

fig, axes = plt.subplots(3, 1, figsize=(12, 14))

for color_name, group in df.groupby("color"):
    h, s, _ = group.iloc[0][["hue", "saturation", "lightness"]]
    rgb = hsl_to_rgb(h, s, 40)  # Use fixed lightness 40% for line color
    axes[0].plot(group["scale"], group["hue"], marker="o", label=color_name, color=rgb, linewidth=2)
    axes[1].plot(group["scale"], group["saturation"], marker="o", label=color_name, color=rgb, linewidth=2)
    axes[2].plot(group["scale"], group["lightness"], marker="o", label=color_name, color=rgb, linewidth=2)

axes[0].set_title("Hue vs Scale")
axes[1].set_title("Saturation vs Scale")
axes[2].set_title("Lightness vs Scale")
for ax in axes:
    ax.legend(loc="best", ncol=3, fontsize=9)
    ax.set_xlabel("Scale")
plt.tight_layout()
plt.show()
