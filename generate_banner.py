#!/usr/bin/env python3
"""Generate the NextG-Sec 2026 workshop banner image."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 300

# Colors
BG_TOP    = (10, 22, 55)      # dark navy
BG_BOTTOM = (18, 38, 80)      # slightly lighter navy
ACCENT    = (0, 174, 219)     # cyan accent line
TITLE     = (0, 174, 219)     # cyan title
WHITE     = (255, 255, 255)
SUBWHITE  = (210, 230, 255)   # slightly off-white for subtitle

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def make_gradient(width, height, top_color, bottom_color):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        t = y / (height - 1)
        r = int(top_color[0] * (1 - t) + bottom_color[0] * t)
        g = int(top_color[1] * (1 - t) + bottom_color[1] * t)
        b = int(top_color[2] * (1 - t) + bottom_color[2] * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img


def centered_x(draw, text, font, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    return (width - (bbox[2] - bbox[0])) // 2


img = make_gradient(WIDTH, HEIGHT, BG_TOP, BG_BOTTOM)
draw = ImageDraw.Draw(img)

# Top accent bar
ACCENT_H = 4
draw.rectangle([(0, 0), (WIDTH, ACCENT_H)], fill=ACCENT)

# Fonts
font_title    = ImageFont.truetype(FONT_BOLD, 62)
font_subtitle = ImageFont.truetype(FONT_REG,  28)
font_footer   = ImageFont.truetype(FONT_REG,  20)

# Title
title = "NextG-Sec 2026"
tx = centered_x(draw, title, font_title, WIDTH)
draw.text((tx, 48), title, font=font_title, fill=TITLE)

# Subtitle
subtitle = "NextG Networks Cryptography and Security Workshop"
sx = centered_x(draw, subtitle, font_subtitle, WIDTH)
draw.text((sx, 130), subtitle, font=font_subtitle, fill=WHITE)

# Footer
footer = "Co-located with ACNS 2026  \u2022  June 23, 2026  \u2022  Stony Brook University"
fx = centered_x(draw, footer, font_footer, WIDTH)
draw.text((fx, 230), footer, font=font_footer, fill=SUBWHITE)

out = "images/nextg-sec-banner.jpg"
img.save(out, "JPEG", quality=95)
print(f"Saved {out}  ({WIDTH}x{HEIGHT})")
