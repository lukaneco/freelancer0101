txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)


html_code ="""<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:24px;line-height:107%;font-family:"Perpetua",serif;'>{name}</span><span style='font-size:24px;line-height:107%;font-family:"Perpetua",serif;'>, {greetings}</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:24px;line-height:107%;font-family:"Perpetua",serif;'>Relax! You&rsquo;ll be on the beach soon!</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style='font-size:32px;line-height:107%;font-family:"Perpetua",serif;'>Welcome to The Beach Club!</span></strong></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:21px;line-height:107%;font-family:"Perpetua",serif;'>We&rsquo;ll have everything ready for you at 4 PM on {deperture}</span><span style='font-size:24px;line-height:107%;font-family:"Perpetua",serif;'>.</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style='font-size:19px;font-family:"Perpetua",serif;'>Please have this email and your Driver&rsquo;s License out and ready to present to the attendant at the gate. They will scan the code below and your driver&rsquo;s license to confirm your reservation of:</span></strong></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style='font-size:11px;font-family:"Perpetua",serif;'>&nbsp;</span></strong></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style='font-size:21px;font-family:"Perpetua",serif;'>Unit {unit}&nbsp;from {arrival}&nbsp;&ndash; {deperture}.</span></strong></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style='font-size:11px;font-family:"Perpetua",serif;'>&nbsp;</span></strong></p>
<p style='margin-top:0cm;margin-right:-9.0pt;margin-bottom:8.0pt;margin-left:-22.5pt;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:19px;line-height:107%;font-family:"Perpetua",serif;'>Once you have registered at the gate you may use either of the entrance gates for the remainder of your stay. The system will recognize your vehicle automatically and open the gate.</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:11px;font-family:"Perpetua",serif;'>{qrcode}</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:11px;font-family:"Perpetua",serif;'>&nbsp;</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:11px;font-family:"Perpetua",serif;'>&nbsp;</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:19px;font-family:"Perpetua",serif;'>Thank you for your help to expedite the check in process.</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:19px;font-family:"Perpetua",serif;'>Soon you will be on the beach enjoying our beautiful resort.</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:11px;font-family:"Perpetua",serif;'>&nbsp;</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style='font-size:19px;line-height:107%;font-family:"Perpetua",serif;'>{saludation}</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><span style='font-size:19px;line-height:107%;font-family:"Perpetua",serif;'>&nbsp;</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;'><span style='font-size:19px;font-family:"Perpetua",serif;'>{contact}</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;'><span style='font-size:19px;font-family:"Perpetua",serif;'>{company_name}&nbsp;</span></p>
<p style='margin:0cm;font-size:15px;font-family:"Calibri",sans-serif;'><span style='font-size:19px;font-family:"Perpetua",serif;'>{phone}</span></p>"""

#txt1 = html_code.format(name = "John", unit = 36)

attachement = "exe works\qrcode001.png"
name = "luca"
greetings = "nice dick bro"
unit = "345sdfv"
arrival = "14/09/2020"
deperture = "15/09/2023"
saludation = "hasta la proximaa"
contact = "Pam Martin, REALTOR"
company_name = "Pam Martin - Keller Williams"
phone = "(251)269-8864 or (251)279-0717"

print(attachement.split("\\")[-1])
qrcode_html = "<img src='cid:"+attachement+"'> "

txt1 = html_code.format(name  =  name ,
                greetings = greetings,
                unit = unit,
                arrival = arrival,
                deperture = deperture,
                saludation = saludation,
                contact = contact,
                company_name = company_name,
                phone = phone,
                qrcode = qrcode_html)
# print(txt1)
Html_file= open("index.html","w")
Html_file.write(txt1)
Html_file.close()