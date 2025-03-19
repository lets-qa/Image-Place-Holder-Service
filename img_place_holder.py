from typing import Optional
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, Response

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage():
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>Lets.QA: Image Place Holder Service</title>
      </head>
      <body style="font-family: sans-serif; margin: 40px;">
        <h1>Lets.QA: Image Place Holder Service</h1>
        <p>
          This service generates placeholder images in SVG format for use in websites and prototypes.
          To use it, specify the desired dimensions in the URL and optional query parameters for text, 
          background color, and text color.
        </p>

        <h2>Basic Usage</h2>
        <ul>
          <li><strong>Dimensions</strong>: <code>/{width}x{height}</code> or <code>/{size}</code> for squares</li>
          <li><strong>Query Params</strong>:
            <ul>
              <li><code>?text=Your+Text</code></li>
              <li><code>?bg=cccccc</code> (background color in hex without #)</li>
              <li><code>?color=000000</code> (text color in hex without #)</li>
            </ul>
          </li>
        </ul>

        <h2>Examples</h2>
        <ul>
          <li>
            <a href="/300x100">/300x100</a> 
            &mdash; returns a 300 × 100 gray image with default text “300 x 100”.
          </li>
          <li>
            <a href="/400?text=Square%20Placeholder">/400?text=Square%20Placeholder</a> 
            &mdash; returns a 400 × 400 placeholder with custom text.
          </li>
          <li>
            <a href="/600x200?text=Hello+World&bg=ff0000&color=ffffff">
              /600x200?text=Hello+World&amp;bg=ff0000&amp;color=ffffff
            </a> 
            &mdash; returns a 600 × 200 placeholder with white text on a red background.
          </li>
        </ul>

         <div class="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-6">
        <h1 class="text-xl font-bold mb-4">Sample Placeholder Images:</h1>
        <div class="space-y-6">
            <!-- Leaderboard -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Leaderboard (728x90)</p>
                <img src="https://iph.lets.qa/728x90?text=HI+MOM+😊&bg=145DA0&color=ffffff" alt="Leaderboard" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/728x90?text=HI+MOM+😊&bg=145DA0&color=ffffff" alt="Leaderboard"&gt;
                </textarea>
            </div>
            <!-- Medium Rectangle -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Medium Rectangle (300x250)</p>
                <img src="https://iph.lets.qa/300x250" alt="Medium Rectangle" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/300x250" alt="Medium Rectangle"&gt;
                </textarea>
            </div>
            <!-- Large Rectangle -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Large Rectangle (336x280)</p>
                <img src="https://iph.lets.qa/336x280" alt="Large Rectangle" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/336x280" alt="Large Rectangle"&gt;
                </textarea>
            </div>
            <!-- Skyscraper -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Skyscraper (120x600)</p>
                <img src="https://iph.lets.qa/120x600" alt="Skyscraper" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/120x600" alt="Skyscraper"&gt;
                </textarea>
            </div>
            <!-- Wide Skyscraper -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Wide Skyscraper (160x600)</p>
                <img src="https://iph.lets.qa/160x600" alt="Wide Skyscraper" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/160x600" alt="Wide Skyscraper"&gt;
                </textarea>
            </div>
            <!-- Half Page -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Half Page (300x600)</p>
                <img src="https://iph.lets.qa/300x600" alt="Half Page" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/300x600" alt="Half Page"&gt;
                </textarea>
            </div>
            <!-- Banner -->
            <div class="flex flex-col items-center">
                <p class="font-semibold">Banner (468x60)</p>
                <img src="https://iph.lets.qa/468x60" alt="Banner" class="border rounded"><br />
                <textarea class="mt-2 w-full border p-2 text-sm" rows="2" readonly>
&lt;img src="https://iph.lets.qa/468x60" alt="Banner"&gt;
                </textarea>
            </div>
        </div>
    </div>

      </body>
    </html>    """
    return html_content

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.get("/{dimensions}")
def placeholder(
    dimensions: str,
    text: Optional[str] = Query(None),
    bg: str = Query(default="cccccc"),
    color: str = Query(default="000000")
):
    if "x" in dimensions:
        width_str, height_str = dimensions.split("x")
        width, height = int(width_str), int(height_str)
    else:
        width = height = int(dimensions)

    text_to_display = text or f"{width} x {height}"

    svg_content = generate_svg(width, height, bg, color, text_to_display)

    return Response(content=svg_content, media_type="image/svg+xml")

def generate_svg(width: int, height: int, bg: str, color: str, text: str) -> str:
    bg_color = f"#{bg}"
    text_color = f"#{color}"

    # You can customize the watermark text here
    watermark_text = "<a href='https://iph.lets.qa' target='_new' alt='Image generated by the Lets.QA: Image Place Holder Service'>iph.lets.qa</a>"
    # Adjust the opacity from 0.0 to 1.0 (semi-transparent is e.g. 0.4 or 0.5)
    watermark_opacity = 0.4

    # We'll place the watermark near the bottom-right, with a small margin
    # x-position = width - 10 for margin, y-position = height - 5 for margin
    # Using text-anchor="end" to align the text to the right
    # Using dominant-baseline="auto" or "central" based on preference
    svg_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg 
    width="{width}" 
    height="{height}" 
    viewBox="0 0 {width} {height}" 
    xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{bg_color}" />
  <text 
    x="50%" 
    y="50%"
    fill="{text_color}"
    font-size="20"
    text-anchor="middle"
    dominant-baseline="middle"
    font-family="sans-serif">
    {text}
  </text>
  <text
    x="{width - 10}"
    y="{height - 10}"
    fill="black"
    font-size="12"
    text-anchor="end"
    font-family="sans-serif"
    opacity="{watermark_opacity}">
    {watermark_text}
  </text>
</svg>
"""
    return svg_template
