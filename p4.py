semana_laboral = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print("semana laboral =", semana_laboral )
print("Dia 1 =", semana_laboral[4])
semana_laboral[4]="Sabado"

print("Semana_laboral= ", semana_laboral)
semana_laboral[4]="Viernes"

longitud_lista=len(semana_laboral)
print("Longitud= ", longitud_lista)

posicion = semana_laboral.index("Miercoles")
print("Posicion de miercoles= ", posicion)

semana_laboral.append("Sabado")
print("Semana laboral= ", semana_laboral)

del semana_laboral[4]
print("Semana laboral= ", semana_laboral)