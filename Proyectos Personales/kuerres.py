import qrcode

# Enlace del grupo de WhatsApp
whatsapp_group_link = "https://forms.gle/qjVgLjhutB12wJ9h9"

# Generar el código QR
qr = qrcode.make(whatsapp_group_link)

# Guardar el código QR como una imagen
qr.save("JuventudesExternos.png")

print("¡Código QR generado y guardado como grupo_whatsapp_qr.png!")
