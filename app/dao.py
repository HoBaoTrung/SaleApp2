def load_loaiSanPhan():
    return[{
    "id":1, 'name':"Tablet"
},{
    "id":2, "name":"Iphone"
}]
    
def load_products(kw):
    products=[{
    "id":1, "name":"Iphone", "Price": 240000000,
    "image":"https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-den-thumb-600x600.jpg"
},{
    
    "id":2, "name":"Laptop", "Price": 240000000,
    "image":"https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-den-thumb-600x600.jpg"
   
},
{
    
    "id":3, "name":"Laptop", "Price": 300000000,
    "image":"https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-den-thumb-600x600.jpg"
   
},
{
    
    "id":4, "name":"Tablet", "Price": 240000000,
    "image":"https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-den-thumb-600x600.jpg"
   
},
{
    
    "id":5, "name":"Samsung", "Price": 240000000,
    "image":"https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-den-thumb-600x600.jpg"
   
},
]
    
    if kw:
        products=[p for p in products if p['name'].find(kw)>=0] 

    return products

