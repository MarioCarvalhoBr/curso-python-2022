def somar(formulario):
    num1 = float(formulario.txt_num1.text())
    num2 = float(formulario.txt_num2.text())
    soma = num1 + num2
    formulario.lbl_resultado.setText(f"{num1} + {num2} == {soma}")
