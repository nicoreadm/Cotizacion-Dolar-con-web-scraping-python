def fcalculadora(blue,bna,mep,ccl,usdt,ingresar,vector):

  #CALCULADORA
  pes = ingresar
  
  #dolar blue
  peblue = round(float(pes) / float(blue[1]),2)

  #dolar bna
  pbna = round(float(pes) / float(bna[1]),2)
  

  #dolar mep
  pmep = round(float(pes) / float(mep[1]),2)

  #dolar ccl
  pccl = round(float(pes) / float(ccl[1]),2)
  
  #usdt
  pusdt= round(float(pes) / float(usdt[1]),2)
  vector[0] = str(peblue)
  vector[1] = str(pbna)
  vector[2] = str(pmep)  
  vector[3] = str(pccl)
  vector[4] = str(pusdt)