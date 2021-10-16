dic={'Cierra Vega':175,'Alden Cantrell':180,'Kierra Gentry':165,'Pierre Cox':190}
dic1={}
for i in dic:
    if dic[i]>170 :
        dic1.update({i:dic[i]})
print(dic1)