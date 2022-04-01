#função que será testada
def testa_numero (numero):
  return numero

#função que fará o teste na função testa_numero
def test_testa_numero():
  entrada = 3
  esperado = 3
  resultado = testa_numero(entrada)
  assert resultado == esperado


Vamos pegar um número inteiro, por exemplo: "1"
- Quando o número for múltiplo de 3, deve retornar "queijo"
- Quando o número for múltiplo de 5, deve retornar "goiabada"
- Quando o número for múltiplo de 3 e de 5, deve retornar "romeu e julieta"