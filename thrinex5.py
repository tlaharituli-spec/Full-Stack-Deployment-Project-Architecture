import os

# -----------------------------
# Project Structure
# -----------------------------

folders = [
    "capstone",
    "capstone/css",
    "capstone/js",
    "capstone/images"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# index.html
# -----------------------------

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>E-Commerce Product Catalog</title>

<link rel="stylesheet" href="css/style.css">

</head>

<body>

<header>

<h1>My Store</h1>

<nav>

<a href="#home">Home</a>
<a href="#products">Products</a>
<a href="#about">About</a>

</nav>

</header>

<main id="app">

</main>

<script src="js/app.js"></script>

</body>
</html>
"""

# -----------------------------
# CSS
# -----------------------------

style_css = """
body{

font-family:Arial;

margin:0;

background:#f4f4f4;

}

header{

background:#333;

color:white;

padding:20px;

display:flex;

justify-content:space-between;

align-items:center;

}

nav a{

color:white;

margin-left:20px;

text-decoration:none;

}

.grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:20px;

padding:20px;

}

.card{

background:white;

padding:20px;

border-radius:8px;

box-shadow:0 2px 5px rgba(0,0,0,.2);

}

button{

padding:10px;

cursor:pointer;

}
"""

# -----------------------------
# JavaScript
# -----------------------------

app_js = """
const app=document.getElementById("app");

const products=[

{
id:1,
name:"Laptop",
price:"$899"
},

{
id:2,
name:"Phone",
price:"$599"
},

{
id:3,
name:"Headphones",
price:"$199"
}

];

function home(){

app.innerHTML=`

<section>

<h2>Welcome</h2>

<p>Modern E-Commerce Demo</p>

</section>

`;

}

function catalog(){

let html='<section class="grid">';

products.forEach(product=>{

html+=`

<div class="card">

<h3>${product.name}</h3>

<p>${product.price}</p>

<button>Add to Cart</button>

</div>

`;

});

html+='</section>';

app.innerHTML=html;

}

function about(){

app.innerHTML=`

<section>

<h2>About</h2>

<p>Responsive Capstone Project</p>

</section>

`;

}

function router(){

const hash=location.hash || "#home";

switch(hash){

case "#products":

catalog();

break;

case "#about":

about();

break;

default:

home();

}

}

window.addEventListener("hashchange",router);

window.addEventListener("load",router);
"""

# -----------------------------
# README
# -----------------------------

readme = """
# Web Development Capstone

## Features

- Modular architecture
- Client-side routing
- Responsive layout
- Product catalog
- Ready for deployment

## Deployment

1. Upload folder to GitHub.
2. Connect repository to:
   - Vercel
   - Netlify
   - Render
3. Deploy.

"""

# -----------------------------
# vercel.json
# -----------------------------

vercel = """
{
  "cleanUrls": true
}
"""

# -----------------------------
# Write files
# -----------------------------

files = {
    "capstone/index.html": index_html,
    "capstone/css/style.css": style_css,
    "capstone/js/app.js": app_js,
    "capstone/README.md": readme,
    "capstone/vercel.json": vercel,
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

print("=" * 50)
print("Capstone project generated successfully!")
print("=" * 50)

print("""
Project Structure

capstone/
│
├── index.html
├── README.md
├── vercel.json
│
├── css/
│   └── style.css
│
├── js/
│   └── app.js
│
└── images/
""")
