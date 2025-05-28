def selamla(isim="isimsiz"): # selmala isimli 1 argümanlı ve argümanı varsayılan olarak atanmış ("isimsiz") bir fonksiyon tanımlanıyor. burada fonksiyon içine herhangi bir argüman gönderilemz ise fonksiyon varsayılan olarak tanımlanmış argümanı atar.
    print("Selam",isim) # ekrana bastırılıyor.

selamla() # fonksiyon argüman olmadan çağrılıyor ve bu durumda argüman gönderilemdiği için varsayılan argüman atanıyor.
# çıktı:
#Selam isimsiz

selamla("mehmet") # burada fonksiyon içine bir argüman gönderiliyor.
# çıktı:
#Selam mehmet

