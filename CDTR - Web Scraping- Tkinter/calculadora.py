def convertir_float(valor):
  valor = valor.replace('.','')
  valor= valor[::-1]
  i=0
  valor2=''
  for caracter in valor:
    valor2=valor2+caracter
    i+=1
    if i ==2:
      valor2=valor2+'.'

  valor2= valor2[::-1]
  return valor2

def fcalculadora(blue,bna,mep,ccl,usdt,ingresar,vector):

  #CALCULADORA
  pes = ingresar

  #convertir en float
  
  #blue
  fblue=convertir_float(blue[1])
  #bna
  fbna=convertir_float(bna[1])
  #mep
  fmep=convertir_float(mep[1])
  #ccl
  fccl=convertir_float(ccl[1])
  #usdt
  fusdt=convertir_float(usdt[1])

  #dolar blue
  peblue = round(float(pes) / float(fblue),2)

  #dolar bna
  pbna = round(float(pes) / float(fbna),2)

  #dolar mep
  pmep = round(float(pes) / float(fmep),2)

  #dolar ccl
  pccl = round(float(pes) / float(fccl),2)
  
  #usdt
  pusdt= round(float(pes) / float(fusdt),2)
  vector[0] = str(peblue)
  vector[1] = str(pbna)
  vector[2] = str(pmep)  
  vector[3] = str(pccl)
  vector[4] = str(pusdt)
