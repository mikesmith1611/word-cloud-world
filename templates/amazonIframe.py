from dash_html_components import Iframe, Div, Script, A, Img


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

