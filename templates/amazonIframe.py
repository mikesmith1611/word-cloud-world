from dash_html_components import Iframe, Div, Script, A, Img



# style = dict(width="728", height="90", scrolling="no", display="block", margin="0 auto", border="0", marginwidth="0", style="border:none;", frameborder="0")
# src = "//rcm-na.amazon-adsystem.com/e/cm?o=1&p=48&l=ur1&category=kindlerotating&f=ifr&linkID=185d1a5564d07a87bccaee4b7f460bfe&t=1071a1-20&tracking_id=1071a1-20"

# amazonKindleRotating = Iframe(src=src, style=style)


# src="//rcm-na.amazon-adsystem.com/e/cm?o=1&p=48&l=ur1&category=musicandentertainmentrot&f=ifr&linkID=cbd8174ad9961eec20006d337295a29f&t=1071a1-20&tracking_id=1071a1-20" 

# amazonMusicRotatingWide = Iframe(src=src, style=style)


# src="//rcm-na.amazon-adsystem.com/e/cm?o=1&p=12&l=ur1&category=musicandentertainmentrot&f=ifr&linkID=a7a2545e9b5d2d9976577f07761ed15e&t=1071a1-20&tracking_id=1071a1-20"
# style = dict(width="300", height="250", scrolling="no", border="0", marginwidth="0", margin="0 auto", style="border:none;", frameborder="0")

# amazonMusicRotatingNarrow = Iframe(src=src, style=style)

style = dict(width="120", height="240", border="none", margin=0)
src="//ws-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=US&source=ac&ref=qf_sp_asin_til&ad_type=product_link&tracking_id=1071a1-20&marketplace=amazon&region=US&placement=B071ZTJWM7&asins=B071ZTJWM7&linkId=5970c6c787de8010ce62b8b6309ca1bc&show_border=false&link_opens_in_new_window=true&price_color=333333&title_color=0066c0&bg_color=ffffff"

amazonMusicProduct = Iframe(src=src, style=style)



img = Img(src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B071ZTJWM7&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=1071a1-20", style={"margin":"0 auto", "display": "block"})
a = A(img, target="_blank", href="https://www.amazon.com/gp/product/B071ZTJWM7/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B071ZTJWM7&linkCode=as2&tag=1071a1-20&linkId=3ec0629eca960378dc9f3d5e4de50601")
img2 = Img(src="//ir-na.amazon-adsystem.com/e/ir?t=1071a1-20&l=am2&o=1&a=B071ZTJWM7", width="1", height="1", alt="", style={"border": "none !important", "margin":"0px !important"})
amazonMusicProduct = Div([
    a,img2
])

img = Img(src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B00N28818A&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=1071a1-20", style={"margin":"0 auto", "display": "block"})
a = A(img, target="_blank", href="https://www.amazon.com/gp/product/B00N28818A/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00N28818A&linkCode=as2&tag=1071a1-20&linkId=188e6e60a5d7dc73a5b047453861d955")
img2 = Img(src="//ir-na.amazon-adsystem.com/e/ir?t=1071a1-20&l=am2&o=1&a=B00N28818A", width="1", height="1", alt="", style={"border": "none !important", "margin":"0px !important"})
amazonPrimeVideoProduct = Div([
    a,img2
])

